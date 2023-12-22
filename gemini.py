import google.generativeai as genai
import json
import time

GOOGLE_API_KEY = "AIzaSyCEupKbI7TZJRW_zhOOSmwUT6H2g-n4mWM"
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-pro")

current_time = 0
call_count = 0
call_limit = 60


# def test_count():
#     global current_time
#     global call_count
#     global call_limit
#     sec_now = int(time.time())
#     sec_remain = sec_now % 60
#     space = sec_now - current_time
#     print("call %s", call_count)
#     if space > 60:
#         current_time = sec_now - sec_remain
#         if call_count > call_limit:
#             call_count -= call_limit
#         else:
#             call_count = 0
#     else:
#         if call_count > call_limit - 1:
#             print("waitting %s", 60 - sec_remain)
#             time.sleep(60 - sec_remain + 10)
#             return test_count()
#     call_count += 1
#     print("run %s", call_count)
#     return "done"


def getJson(prompt, temp=1):
    global current_time
    global call_count
    global call_limit
    sec_now = int(time.time())
    sec_remain = sec_now % 60
    space = sec_now - current_time
    if space > 60:
        current_time = sec_now - sec_remain
        if call_count > call_limit:
            call_count -= call_limit
        else:
            call_count = 0
    else:
        if call_count > call_limit - 1:
            time.sleep(60 - sec_remain + 10)
            return getJson(prompt, temp)
    call_count += 1
    try:
        call_count += 1
        res = model.generate_content(
            prompt,
            generation_config=genai.types.GenerationConfig(temperature=temp),
        )
        json.loads(res.text)
        return res
    except:
        print("error")
        return getJson(prompt, temp)
