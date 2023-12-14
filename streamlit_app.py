import google.generativeai as genai
import examples
import rules_settings
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
Dont mark response by anything. For example: "```json"
"""
        + rule_ex.LABEL
        + """
Q: Give me title and key points this text, each key points, give a label negative, positive or info:
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
A: {
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
A:"""
    )


def summ(txt):
    topics = model.generate_content(prompt_topic(txt))
    st.write(topics.text)
    st.write("\n")
    res_stock = model.generate_content(prompt_company(txt))
    st.write(res_stock.text)
    st.write("\n")
    # seg and sum
    tpc = json.loads(topics.text)
    tcks = json.loads(res_stock.text)
    tt = 0
    po = 0
    for i in tpc["key_points"]:
        if i["label"] == "Positive":
            tt += 1
            po += 1
        if i["label"] == "Negative":
            tt += 1
    tpc.update(tcks)
    tpc.update({"segment": po / tt * 10})
    return tpc


# with open("log.txt", "a", encoding="utf-8") as f:
#     # f.write(res_company.text)
#     # f.write("\n")
#     f.write(res_stock.text)
#     f.write("\n")
#     f.write(topics.text)
#     f.write("\n")
#     f.write("\n")
#     f.write(str(tpc))


txt = st.text_area("Text to analyze", examples.TEST_11)
if st.button("Restart", type="primary"):
    st.rerun()
if st.button("Submit", type="primary"):
    # URL = url
    st.write("Waitting")
    if len(txt) > 0:
        res = summ(txt)
        st.write("\n")
        st.write("Result:")
        st.write("\n")
        st.json(res)
