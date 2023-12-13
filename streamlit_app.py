import openai

# import altair as alt
# import numpy as np
# import pandas as pd
import streamlit as st
import re

# from llm_base import whp, getTicker, checkTicker, getTitle, label
from openai import OpenAI
from rules_settings import (
    # RULE_KEYWORDS,
    # EXAMPLE_KEYWORDS,
    # SUM_RULE_TITLE,
    # SUMEX_TITLE,
    RULE_TOPIC,
    TICKERS_RULE,
    TITLE_RULE,
    LABEL_RULE,
)
from examples import TEST_12
import requests
import re

# from streamlit_ws_localstorage import injectWebsocketCode, getOrCreateUID
# URL = "https://93p4x57c4lar2k-5000.proxy.runpod.net/v1"
URL = "http://localhost:1234/v1"
# openai.api_base = URL
# openai.api_key = "not-needed"  # no need for an API key

client = OpenAI(base_url=URL, api_key="not-needed")


def getResult(prompt):
    mss = "No message"
    st.write("\n\n=========Prompt=========\n\n" + prompt)
    try:
        # completion = generate(prompt)
        completion = client.completions.create(
            model="local-model",
            # messages=[
            #     {"role": "system", "content": "Perform the task to the best of your ability."},
            #     {"role": "user", "content": prompt},
            # ],
            prompt=prompt,
            # max_tokens=1000,
            temperature=0.7,
            # max_tokens=1500,
            stop=["<|im_end|>", "<|im_start|>"],
        )
        mss = str(completion)
        res = completion.choices[0].text

        st.write(
            # +"\n\n=========json=========\n"
            # + completion.text
            "\n\n=========Result=========\n\n"
        )
        st.write(res)
        if len(re.findall(r"<\|.*?\|>", res)) > 0:
            res = re.split(r"<\|.*?\|>", res)[0]
        return res
    except:
        st.write("\n\n=========ERROR server=========\n\n" + mss)
        return getResult(prompt)


def checkTicker(tickerSt):
    nouns_arr = re.split("[,\n0-9]", tickerSt)
    nouns_arr = [i for i in nouns_arr if i.strip() != ""]
    res_arr = []
    st.write("=========ticker=========\n\n")
    for nou in nouns_arr:
        response = requests.get(
            "https://api.simplize.vn/api/search/company/suggestions?q="
            + nou
            + "&t=&page=0&size=3"
        )
        res = None
        st.write("\n\n====" + nou + "=====\n\n")
        for r in response.json()["data"]:
            tkr_pos = len("".join(re.findall("<em>.+<\/em>", r["tickerHL"]))) / len(
                r["tickerHL"]
            )
            name_pos = len("".join(re.findall("<em>.+<\/em>", r["nameHL"]))) / len(
                r["nameHL"]
            )
            if (tkr_pos == 1) or (tickerSt.count(" ") > 0 and name_pos >= 0.66):
                res = r["ticker"]
                break
        st.write(str(res) + "-" + str(tkr_pos) + "-" + str(name_pos))
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
        f"{url}/completions",
        headers=headers,
        json=data,
    )
    return response


def trans_prompt(req):
    return f"""
    <|im_start|>system
    You are a professional interpreter from translate stock news from Vietnamese to English.
    Your response must always be in English.
    You only give the translation without any chat-based fluff.
    Only give the translation on your response, dont give me like "In this case" or something like that<|im_end|>\n
    <|im_start|>user
    translate this text to English:
    {req}<|im_end|>\n
    <|im_start|>assistant
    """


def vi2en(text_to_trans):
    result = ""
    for txt in text_to_trans.split("\n"):
        if len(txt.strip()) > 0:
            result += getResult(trans_prompt(txt.strip()))
    return result
    # return getResult(trans_prompt(text_to_trans.strip()))


def promptwhp(txt):
    return f"""
<|im_start|>system
{RULE_TOPIC}
Do not return any notes or explanations from your response.<|im_end|>\n
<|im_start|>user

Please extract key points from this text:
{txt}<|im_end|>\n

<|im_start|>assistant
"""


def whp(text_to_summarize):
    txt_word_count = len(text_to_summarize.split())
    ttl_word_count = len(promptwhp(text_to_summarize).split())
    # if ttl_word_count > 500:
    #     txtRes = text_to_summarize.split("\n")
    #     txt_arr = [""]
    #     i = 0
    #     for t in txtRes:
    #         if len(txt_arr[i].split()) + len(t.split()) <= 500:
    #             txt_arr[i] += t
    #         else:
    #             i += 1
    #             txt_arr.append("")
    #             txt_arr[i] += t
    #     totalRes = ""
    #     for t in txt_arr:
    #         totalRes += getResult(promptwhp(t)) + "\n"
    #     return totalRes
    print(txt_word_count)
    print(ttl_word_count)
    return getResult(promptwhp(text_to_summarize))


def label(text_to_summarize):
    prompt = f"""
<|im_start|>system
You are a financial expert.
You can labels financials text provided is Negative or Positive.
You only give the labels without any chat-based fluff.
Only give the labels on your response, dont give me like "In this case" or something like that
Do not return any notes or explanations at the end of your response.<|im_end|>\n
{LABEL_RULE}
<|im_start|>user
Please label each item:
{text_to_summarize}
<|im_end|>\n
<|im_start|>assistant
"""
    txt_word_count = len(text_to_summarize.split())
    ttl_word_count = len(prompt.split())
    print(txt_word_count)
    print(ttl_word_count)
    return getResult(prompt)


def getTitle(text_to_summarize):
    prompt = f"""
<|im_start|>system
{TITLE_RULE}
Do not return any notes or explanations at the end of your response.<|im_end|>\n
<|im_start|>user
Please give a title for this text:
{text_to_summarize}<|im_end|>\n
<|im_start|>assistant
    """
    txt_word_count = len(text_to_summarize.split())
    ttl_word_count = len(prompt.split())
    print(txt_word_count)
    print(ttl_word_count)
    return getResult(prompt)


def getTicker(text_to_summarize):
    prompt = f"""
<|im_start|>system
You are a financial expert.
You can find all stock from text.
You are to the point and only give the answer in isolation without any chat-based fluff.
Do not return any notes or explanations at the end of your response.<|im_end|>\n
<|im_start|>user
please give me all stocks from this text:
{text_to_summarize}<|im_end|>\n
<|im_start|>assistant
    """
    txt_word_count = len(text_to_summarize.split())
    ttl_word_count = len(prompt.split())
    print(txt_word_count)
    print(ttl_word_count)
    return getResult(prompt)


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
        r"(\n+\s*[0-9]+[^0-9a-zA-Z]\s)|(\n+\s*[-]+\s)", "-----", "\n" + raw_res
    ).split("-----")
    # if len(split_res) < 2:
    #     split_res = re.findall(r"\n\s*[-]+\s.+", raw_res)
    split_res = [
        i
        for i in split_res
        if i != ""
        and not i.__contains__("Key points")
        and not i.__contains__("key points")
    ]
    for e in split_res:
        split_e = e.strip()
        if len(split_e.split()) > 0:
            res_topic += '"' + split_e + '",'
    res_topic = res_topic.rsplit(",", 1)[0] + "]"
    summText = " ".join(split_res)

    # f.write(whp(TEST))
    # f.write(re.split(r"\n", raw_res))
    raw_tks = getTicker(text_to_action)
    # arr_ticker = checkTicker(raw_tks)
    arr_ticker = re.sub(
        r"(\n+\s*[0-9]+[^0-9a-zA-Z]\s)|(\n+\s*[-]+\s)", "-----", "\n" + raw_tks
    ).split("-----")
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


url = st.text_input("Url", URL)
txt = st.text_area("Text to analyze", TEST_12)
if st.button("Restart", type="primary"):
    # st.session_state.value = "Foo"
    st.rerun()
if st.button("Submit", type="primary"):
    # URL = url
    st.write("Waitting")
    if len(txt) > 0:
        st.write(action(vi2en(txt)))
