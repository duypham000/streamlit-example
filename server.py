import google.generativeai as genai
import examples
import streamlit as st
import json

import rule_ex

# Or use `os.getenv('GOOGLE_API_KEY')` to fetch an environment variable.
GOOGLE_API_KEY = "AIzaSyCEupKbI7TZJRW_zhOOSmwUT6H2g-n4mWM"
# GOOGLE_API_KEY=userdata.get('GOOGLE_API_KEY')

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel("gemini-pro")
TEST_TEXT = examples.TEST_12


def prompt_topic(txt):
    return (
        """
You are a financial expert.
You are to the point and only give the answer in isolation without any chat-based fluff.
Your response must be JSON format.
Each key points must have 1 or 2 sentence and less than 255 character.
Your key points must be less than 10.
Dont mark response by anything. For example: "```json"
"""
        + rule_ex.LABEL
        + """
Q: Give me title and key points this text, each key points, give a label negative, positive, info or advertisement:
"""
        + txt
        + """
JSON:
    """
    )


def prompt_company(txt):
    return (
        """
You are a financial expert.
You are to the point and only give the answer in isolation without any chat-based fluff.
Your response must be JSON format.
Dont mark response by anything. For example: "```json"
Q: Find all company name and stock code from this text:
Hôm nay, mã chứng khoán của Công ty cổ phần Tập đoàn Hòa Phát ghi nhận giá trị giao dịch gần 1.500 tỷ đồng, cao nhất thị trường.
Hưng Thịnh Land gia hạn ngày tất toán 15 tháng cho 6 lô trái phiếu tổng mệnh giá 1.600 tỷ đồng, dời áp lực trả nợ sang tháng 11/2024.
Trước khi gia hạn, Tập đoàn Hưng Thịnh và các doanh nghiệp trong hệ sinh thái nhiều lần công bố thông tin về việc chậm thanh toán gốc và lãi trái phiếu. Lý do chung là thị trường tài chính, thị trường giao dịch bất động sản diễn biến không thuận lợi dẫn đến doanh nghiệp chưa thu xếp kịp nguồn tiền để thanh toán đúng hạn so với kế hoạch.
Một ngày sau khi công bố Chứng khoán LPBank cùng hai nhà đầu tư mua cổ phiếu, Hoàng Anh Gia Lai hủy thông tin với lý do "báo cáo sai sót".
JSON: {
    "tickers": [
        {
            "name": "Công ty cổ phần Tập đoàn Hòa Phát",
            "code": "HPG"
        },
        {
            "name": "Tập đoàn Hưng Thịnh",
            "code": "HTN"
        },
        {
            "name": "LPBank",
            "code": "LPB"
        },
        {
            "name": "Hoàng Anh Gia Lai",
            "code": "HAG"
        }
    }
Q: Find all company name and stock code from this text:
"""
        + txt
        + """
JSON:"""
    )


def prompt_ads(txt):
    return (
        """
You are a financial expert.
You are to the point and only give the answer in isolation without any chat-based fluff.
Your response must be JSON format.
Dont mark response by anything. For example: "```json"
"""
        + rule_ex.ADS
        + """
Q: This text is ads or not:
"""
        + txt
        + """
A:
"""
    )


def getJson(prompt, temp=1):
    st.write("temp: " + str(temp))
    try:
        res = model.generate_content(
            prompt,
            generation_config=genai.types.GenerationConfig(temperature=temp),
        )
        st.write("\n==========================\n")
        st.write(res.text)
        st.write("\n")
        json.loads(res.text)
        return res
    except:
        return getJson(prompt)


def summ(txt):
    topics = getJson(prompt_topic(txt), 0.5)
    tpc = json.loads(topics.text)
    res_stock = getJson(prompt_company(txt))
    res_ads = getJson(prompt_ads(txt))
    ads = json.loads(res_ads.text)
    # seg and sum
    tcks = json.loads(res_stock.text)
    # ifo = 0
    tt = 0
    po = 0
    for i in tpc["key_points"]:
        if i["label"] == "Positive":
            tt += 1
            po += 1
        if i["label"] == "Negative":
            tt += 1
        # if i["label"] == "Info":
        #     ifo += 1
    tpc.update(tcks)
    tpc.update(ads)
    if tt == 0:
        seg = 5
    else:
        seg = po / tt * 10
    tpc.update({"segment": seg})
    return tpc


from flask import Flask, request, jsonify
import json

app = Flask(__name__)


@app.route("/summ", methods=["POST"])
def summary():
    data = request.get_json()["text"]
    res = summ(data.replace('"', "'"))
    return jsonify(res), 200


if __name__ == "__main__":
    app.run(debug=True)
