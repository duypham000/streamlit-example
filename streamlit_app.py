import openai
import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import re
from llm_base import whp, getTicker, checkTicker, getTitle, label

# from streamlit_ws_localstorage import injectWebsocketCode, getOrCreateUID

def getResult(prompt):
    try:
        # completion = generate(prompt)
        completion = openai.Completion.create(
            model="local-model",
            prompt=prompt,
            max_tokens=1000,
        )
        res = completion["choices"][0]["text"]

        st.write("\n\n=========prompt=========\n" + prompt)
        st.write(
            # +"\n\n=========json=========\n"
            # + completion.text
            "\n\n=========result=========\n"
        )
        st.write(res)
        if len(re.findall(r"\[[^\]]*\]", res)) > 0:
            res = re.split(r"\[[^\]]*\]", res)[0]
        if res.count("[/ANS]") == 0:
            res = res.split("[/ANS]")[0]
        return res
    except:
        st.write("\n\n=========json=========\n" + "ERROR server")
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


url = st.text_input("Url", "https://9z5q89i1s2u9lw-5000.proxy.runpod.net/v1")
txt = st.text_area("Text to analyze", """""")
if st.button("Submit", type="secondary"):
    URL = url
    st.write("Waitting")
    if txt != "":
        action(txt)
if st.button("Stop", type="primary"):
    # st.session_state.value = "Foo"
    st.rerun()