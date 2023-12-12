from openai import OpenAI

# Point to the local server
client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")

completion = client.chat.completions.create(
    model="local-model",  # this field is currently unused
    messages=[
        {
            "role": "system",
            "content": """
You are a professional interpreter from translate stock news from Vietnamese to English.
Your response must always be in English.
You only give the translation without any chat-based fluff.
Only give the translation on your response, dont give me like "In this case" or something like that
""",
        },
        {
            "role": "user",
            "content": """
translate this text to English:
Một ngày sau khi công bố Chứng khoán LPBank cùng hai nhà đầu tư mua cổ phiếu, Hoàng Anh Gia Lai hủy thông tin với lý do "báo cáo sai sót".
""",
        },
    ],
    temperature=0.7,
)

print(completion.choices[0].message)
