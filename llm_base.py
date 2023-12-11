import openai
from rules_settings import (
    RULE_KEYWORDS,
    EXAMPLE_KEYWORDS,
    SUM_RULE_TITLE,
    SUMEX_TITLE,
    RULE_TOPIC,
    TICKERS_RULE,
    TITLE_RULE,
    LABEL_RULE,
)
import requests
import re
import urllib.parse
from flask import Flask, request, jsonify
import json

# pod_id = '0tb1ewp9rvw3or'
# URL = "http://localhost:1234/v1"
URL = "https://9z5q89i1s2u9lw-5000.proxy.runpod.net/v1"
# openai.api_base = "http://localhost:1234/v1"  # point to the local server
openai.api_base = URL
openai.api_key = ""  # no need for an API key


def checkTicker(tickerSt):
    nouns_arr = re.split("[,\n0-9]", tickerSt)
    nouns_arr = [i for i in nouns_arr if i != ""]
    res_arr = []
    for nou in nouns_arr:
        response = requests.get(
            "https://api.simplize.vn/api/search/company/suggestions?q="
            + nou
            + "&t=&page=0&size=3"
        )
        res = None
        for r in response.json()["data"]:
            tkr_pos = len("".join(re.findall("<em>.+<\/em>", r["tickerHL"]))) / len(
                r["tickerHL"]
            )
            name_pos = len("".join(re.findall("<em>.+<\/em>", r["nameHL"]))) / len(
                r["nameHL"]
            )
            if (tickerSt.count(" ") == 0 and tkr_pos == 1) or (
                tickerSt.count(" ") > 0 and name_pos >= 0.66
            ):
                res = r["ticker"]
                break
        if res != None:
            res_arr.append(res)
    return res_arr


def generate(prompt):
    headers = {
        "Content-Type": "application/json",
    }

    data = {
        "model": "local-model",
        "prompt": prompt,
        # "max_new_tokens": 1000,
        "max_tokens": 500,
        "top_k": 10,
        "top_p": 0.95,
        "typical_p": 0.95,
        "temperature": 0.1,
        "repetition_penalty": 1.03,
    }

    response = requests.post(
        f"{URL}/completions",
        headers=headers,
        json=data,
    )
    return response


def getResult(prompt):
    try:
        # completion = generate(prompt)
        completion = openai.Completion.create(
            model="local-model",
            prompt=prompt,
            max_tokens=1000,
        )
        with open("log.txt", "a", encoding="utf-8") as f:
            res = completion["choices"][0]["text"]

            f.write("\n\n=========prompt=========\n" + prompt)
            f.write(
                # +"\n\n=========json=========\n"
                # + completion.text
                "\n\n=========result=========\n"
            )
            f.write(res)
        if len(re.findall(r"\[[^\]]*\]", res)) > 0:
            res = re.split(r"\[[^\]]*\]", res)[0]
        if res.count("[/ANS]") == 0:
            res = res.split("[/ANS]")[0]
        return res
    except:
        with open("log.txt", "a", encoding="utf-8") as f:
            f.write("\n\n=========json=========\n" + "ERROR server")
        return getResult(prompt)


def trans_prompt(req):
    return f"""
    You are a professional interpreter from translating stock news. You are translating a news from Vietnamese to English.
    Your response must always be in English.
    You only give the translation without any chat-based fluff.
    Only give the translation on your response, dont give me like "In this case" or something like that

    [INST]translate this text to English:
    {req}
    [/INST]
    """


def vi2en(text_to_trans):
    result = ""
    for txt in text_to_trans.split("\n"):
        result += getResult(trans_prompt(txt.strip()))

    return result


# def summ(type, text_to_summarize):
#     match type:
#         case 0:
#             rule = RULE_KEYWORDS
#             example = EXAMPLE_KEYWORDS
#         case 1:
#             rule = SUM_RULE_TITLE
#             example = SUMEX_TITLE

#     prompt = f"""
#     {rule}

#     {example}
#     - {text_to_summarize}
#     [/INST]

#     Please give me the keywords that are present in this document and separate them with commas.
#     Make sure you to only return the keywords and say nothing else. For example, don't say: 
#     "The stocks extracted are"
#     [ANS]
#     """
#     return getResult(prompt)


def promptwhp(txt):
    return f"""
{RULE_TOPIC}
[INST]Please extract key points from this text:
- {txt}
[/INST]
Do not return any notes or explanations from your response.
[ANS]
        """


def whp(text_to_summarize):
    txt_word_count = len(text_to_summarize.split())
    ttl_word_count = len(promptwhp(text_to_summarize).split())
    if ttl_word_count > 500:
        txtRes = text_to_summarize.split("\n")
        txt_arr = [""]
        i = 0
        for t in txtRes:
            if len(txt_arr[i].split()) + len(t.split()) <= 500:
                txt_arr[i] += t
            else:
                i += 1
                txt_arr.append("")
                txt_arr[i] += t
        totalRes = ""
        for t in txt_arr:
            totalRes += getResult(promptwhp(t)) + "\n"
        return totalRes
    print(txt_word_count)
    print(ttl_word_count)
    return getResult(promptwhp(text_to_summarize))


def label(text_to_summarize):
    prompt = f"""
    {LABEL_RULE}
[INST]Please label each item:
{text_to_summarize}
[/INST]
Do not return any notes or explanations at the end of your response.
[ANS]
    """
    txt_word_count = len(text_to_summarize.split())
    ttl_word_count = len(prompt.split())
    print(txt_word_count)
    print(ttl_word_count)
    return getResult(prompt)


def getTitle(text_to_summarize):
    prompt = f"""
{TITLE_RULE}
[INST]Please give a title for this text:
- {text_to_summarize}
[/INST]
Do not return any notes or explanations at the end of your response.
[ANS]
    """
    txt_word_count = len(text_to_summarize.split())
    ttl_word_count = len(prompt.split())
    print(txt_word_count)
    print(ttl_word_count)
    return getResult(prompt)


def getTicker(text_to_summarize):
    prompt = f"""
{TICKERS_RULE}
[INST]please give me all nouns about stock fron this text:
{text_to_summarize}
[/INST]
Your response must be from text provided.
You are to the point and only give the answer in isolation without any chat-based fluff.
Do not return any notes or explanations at the end of your response.
    [ANS]
    """
    txt_word_count = len(text_to_summarize.split())
    ttl_word_count = len(prompt.split())
    print(txt_word_count)
    print(ttl_word_count)
    return getResult(prompt)


print("limit 865\n")


def action(text_to_action):
    result_total_json = ""
    res_topic = "["
    ticker_res = '["'

    raw_res = (
        whp(text_to_action)
        .replace("Key points extracted:", "")
        .replace("Key points:", "")
    )
    split_res = re.sub(
        r"(\n+\s*[0-9][^0-9a-zA-Z]\s)|(\n+\s*[-]+\s)", "-----", "\n" + raw_res
    ).split("-----")
    # if len(split_res) < 2:
    #     split_res = re.findall(r"\n\s*[-]+\s.+", raw_res)
    split_res = [i for i in split_res if i != ""]
    for e in split_res:
        split_e = e.strip()
        if len(split_e.split()) > 0:
            res_topic += '"' + split_e + '",'
    res_topic = res_topic.rsplit(",", 1)[0] + "]"
    summText = " ".join(split_res)

    # f.write(whp(TEST))
    # f.write(re.split(r"\n", raw_res))
    raw_tks = getTicker(text_to_action)
    arr_ticker = checkTicker(raw_tks)
    # tks = raw_tks.strip()
    # arr_ticker = re.sub(
    #     r"(\n+\s*[0-9][^0-9a-zA-Z]\s)|(\n+\s*[-]+\s)", "-----", "\n" + tks
    # ).split("-----")
    # arr_ticker.pop(0)
    arr_ticker = [i for i in arr_ticker if i != ""]
    ticker_res += '","'.join(arr_ticker) + '"]'

    raw_title = []
    while len(raw_title) == 0:
        raw_title = re.findall(r"\".*?\"", getTitle(summText))
    res_title = ',"title" : ' + raw_title[0]

    mat_label = "- " + "\n- ".join(split_res).strip()
    arr_label = []
    while len(arr_label) != len(split_res):
        print(len(split_res))
        print(len(arr_label))
        raw_label = label(mat_label).strip()
        arr_label = re.findall("Info|Positive|Negative", raw_label)
    if arr_label.count("Positive") != 0:
        total_label = arr_label.count("Positive") / len(arr_label) * 10
    else:
        total_label = 10
    res_label = (
        ',"sentiment" : '
        + str(total_label)
        + ', "labels" : ["'
        + '","'.join(arr_label)
        + '"]}'
    )

    result_total_json += '{"tickers": '
    result_total_json += ticker_res
    result_total_json += ',"topics": '
    result_total_json += res_topic
    result_total_json += res_title
    result_total_json += res_label
    return result_total_json


# with open("res.txt", "w", encoding="utf-8") as f:

app = Flask(__name__)


@app.route("/summ", methods=["POST"])
def summary():
    data = request.get_json()["text"]
    resen = vi2en(data)
    return jsonify(json.loads(action(resen))), 200


if __name__ == "__main__":
    app.run(debug=True)
