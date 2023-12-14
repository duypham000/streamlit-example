import google.generativeai as genai
import json

import examples
import rule_ex

# Or use `os.getenv('GOOGLE_API_KEY')` to fetch an environment variable.
GOOGLE_API_KEY = "AIzaSyCEupKbI7TZJRW_zhOOSmwUT6H2g-n4mWM"
# GOOGLE_API_KEY=userdata.get('GOOGLE_API_KEY')

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel("gemini-pro")
TEST_TEXT = examples.TEST_12

# topic && title
prompt_topic = (
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
    + TEST_TEXT
    + """
JSON:
    """
)
topics = model.generate_content(prompt_topic)

# label
# ticker

prompt_company = (
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
    + TEST_TEXT
    + """
A:"""
)

res_stock = model.generate_content(prompt_company)
# res_stock = model.generate_content(prompt_stock(res_company.text))

# tickers = '"tickers": ["' + '","'.join(res_stock.text.split(", ")) + '"]'
# result = topics.text[:-1] + "," + tickers + "}"
with open("log.txt", "a", encoding="utf-8") as f:
    # f.write(res_company.text)
    # f.write("\n")
    f.write(res_stock.text)
    f.write("\n")
    f.write(topics.text)
    f.write("\n")
    f.write("\n")
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
    f.write(str(tpc))
