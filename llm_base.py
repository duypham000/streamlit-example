

# # pod_id = '0tb1ewp9rvw3or'
# # URL = "http://localhost:1234/v1"
# # openai.api_base = "http://localhost:1234/v1"  # point to the local server


# # def getResult(prompt):
# #     try:
# #         # completion = generate(prompt)
# #         completion = openai.Completion.create(
# #             model="local-model",
# #             prompt=prompt,
# #             max_tokens=1000,
# #         )
# #         with open("log.txt", "a", encoding="utf-8") as f:
# #             res = completion["choices"][0]["text"]

# #             f.write("\n\n=========prompt=========\n" + prompt)
# #             f.write(
# #                 # +"\n\n=========json=========\n"
# #                 # + completion.text
# #                 "\n\n=========result=========\n"
# #             )
# #             f.write(res)
# #         if len(re.findall(r"\[[^\]]*\]", res)) > 0:
# #             res = re.split(r"\[[^\]]*\]", res)[0]
# #         if res.count("[/ANS]") == 0:
# #             res = res.split("[/ANS]")[0]
# #         return res
# #     except:
# #         with open("log.txt", "a", encoding="utf-8") as f:
# #             f.write("\n\n=========json=========\n" + "ERROR server")
# #         return getResult(prompt)



# # def summ(type, text_to_summarize):
# #     match type:
# #         case 0:
# #             rule = RULE_KEYWORDS
# #             example = EXAMPLE_KEYWORDS
# #         case 1:
# #             rule = SUM_RULE_TITLE
# #             example = SUMEX_TITLE

# #     prompt = f"""
# #     {rule}

# #     {example}
# #     - {text_to_summarize}
# #     [/INST]

# #     Please give me the keywords that are present in this document and separate them with commas.
# #     Make sure you to only return the keywords and say nothing else. For example, don't say: 
# #     "The stocks extracted are"
# #     [ANS]
# #     """
# #     return getResult(prompt)


# print("limit 865\n")


# # def action(text_to_action):
# #     result_total_json = ""
# #     res_topic = "["
# #     ticker_res = '["'

# #     raw_res = (
# #         whp(text_to_action)
# #         .replace("Key points extracted:", "")
# #         .replace("Key points:", "")
# #     )
# #     split_res = re.sub(
# #         r"(\n+\s*[0-9][^0-9a-zA-Z]\s)|(\n+\s*[-]+\s)", "-----", "\n" + raw_res
# #     ).split("-----")
# #     # if len(split_res) < 2:
# #     #     split_res = re.findall(r"\n\s*[-]+\s.+", raw_res)
# #     split_res = [i for i in split_res if i != ""]
# #     for e in split_res:
# #         split_e = e.strip()
# #         if len(split_e.split()) > 0:
# #             res_topic += '"' + split_e + '",'
# #     res_topic = res_topic.rsplit(",", 1)[0] + "]"
# #     summText = " ".join(split_res)

# #     # f.write(whp(TEST))
# #     # f.write(re.split(r"\n", raw_res))
# #     raw_tks = getTicker(text_to_action)
# #     arr_ticker = checkTicker(raw_tks)
# #     # tks = raw_tks.strip()
# #     # arr_ticker = re.sub(
# #     #     r"(\n+\s*[0-9][^0-9a-zA-Z]\s)|(\n+\s*[-]+\s)", "-----", "\n" + tks
# #     # ).split("-----")
# #     # arr_ticker.pop(0)
# #     arr_ticker = [i for i in arr_ticker if i != ""]
# #     ticker_res += '","'.join(arr_ticker) + '"]'

# #     raw_title = []
# #     while len(raw_title) == 0:
# #         raw_title = re.findall(r"\".*?\"", getTitle(summText))
# #     res_title = ',"title" : ' + raw_title[0]

# #     mat_label = "- " + "\n- ".join(split_res).strip()
# #     arr_label = []
# #     while len(arr_label) != len(split_res):
# #         print(len(split_res))
# #         print(len(arr_label))
# #         raw_label = label(mat_label).strip()
# #         arr_label = re.findall("Info|Positive|Negative", raw_label)
# #     if arr_label.count("Positive") != 0:
# #         total_label = arr_label.count("Positive") / len(arr_label) * 10
# #     else:
# #         total_label = 10
# #     res_label = (
# #         ',"sentiment" : '
# #         + str(total_label)
# #         + ', "labels" : ["'
# #         + '","'.join(arr_label)
# #         + '"]}'
# #     )

# #     result_total_json += '{"tickers": '
# #     result_total_json += ticker_res
# #     result_total_json += ',"topics": '
# #     result_total_json += res_topic
# #     result_total_json += res_title
# #     result_total_json += res_label
# #     return result_total_json


# # with open("res.txt", "w", encoding="utf-8") as f:

# app = Flask(__name__)


# @app.route("/summ", methods=["POST"])
# def summary():
#     data = request.get_json()["text"]
#     resen = vi2en(data)
#     return jsonify(json.loads(action(resen))), 200


# if __name__ == "__main__":
#     app.run(debug=True)
