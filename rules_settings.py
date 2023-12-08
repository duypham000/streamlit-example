"""
{'model': 'xlarge', 'prompt': "
The following is a list of documents. Please extract the top keywords, separated by a comma, that describe the topic of the texts.

Document:
- Traditional diets in most cultures were primarily plant-based with a little meat on top, but with the rise of industrial style meat production and factory farming, meat has become a staple food.

Keywords: Traditional diets, Plant-based, Meat, Industrial style meat production, Factory farming, Staple food, Cultural dietary practices

Document:
- The website mentions that it only takes a couple of days to deliver but I still have not received mine.

Keywords: Website, Delivery, Mention, Timeframe, Not received, Waiting, Order fulfillment

Document:
-  {keyword}

Keywords:", 'prompt_vars': {}, 'preset': None, 'num_generations': 1, 'max_tokens': 50, 'temperature': None, 'k': None, 'p': None, 'frequency_penalty': None, 'presence_penalty': None, 'end_sequences': None, 'stop_sequences': ['
'], 'return_likelihoods': None, 'truncate': None, 'logit_bias': {}, 'stream': False}
"""

SUMM_RULE = """
    Your response must always be in English except company's name and stock's name.


    your keypoints must not exceed 255 words or 4 sentences each
    your keypoints must be bullet-like summaries

    each your your tickers must be the stock symbol of the company. Do not mistake the ticker for the currency symbol or commodity symbol
    your tickers must be the word that describes the content from text

    Do not return any notes or explanations at the end of your response.
"""

SUM_RULE_TITLE = [
    """
    your title must not exceed 255 words
    your title must offer a one-short-sentence summary capturing the essence.

"""
]


SUMEX_02 = """
    TEXT: SINGAPORE (Reuters) - Oil prices extended gains on Friday, rising about 1% \on fears that the Israel-Gaza conflict may spread in the Middle East and disrupt supplies from one of the world's top-producing regions.

    Brent crude futures climbed 77 cents, or 0.8%, to $93.15 a barrel by 0042 GMT. U.S. West Texas Intermediate crude was at $90.36 a barrel, up 99 cents, or 1.1%. The front-month November contract expires on Friday.

    The more active December WTI contract was at $89.13 a barrel, up 76 cents.

    Both contracts are on track to post a second weekly gain as an explosion at a Gaza hospital this week and the anticipated ground invasion by Israeli troops heightened fears of the conflict spreading in the Middle East.

    "It's quite scary in fact, looks like things could spiral out of control," IG analyst Tony Sycamore said. "The bigger concern remains that the escalation of tension that we're likely to see with regard to the IDF (Israel Defence Forces) entering Gaza this weekend means the risk to crude oil are towards higher prices."

    Israeli Defence Minister Yoav Gallant told troops gathered at the Gaza border on Thursday that they would soon see the Palestinian enclave "from inside", suggesting an expected ground invasion could be nearing.

    U.S. intercepted missiles fired from Yemen toward Israel, Pentagon said.

    WTI prices could rise towards a high last seen in late September at $95.03 a barrel if it breaks resistance at $91.50, Sycamore said.

    Oil price are also supported by forecasts of widening deficit in the fourth quarter after top producers Saudi Arabia and Russia extended supply cuts to the end of the year and amid low inventories especially in the United States.

    Washington is seeking to buy 6 million barrels of crude for delivery to the Strategic Petroleum Reserve in December and January, as it continues its plan to replenish the emergency stockpile, the U.S. Department of Energy said on Thursday.

    Separately, a temporary lifting of U.S. oil sanctions on OPEC member Venezuela is unlikely to require any policy changes by the OPEC+ producer group for the time being as a recovery in production is likely to be gradual, OPEC+ sources told Reuters.

    Venezuelan state-run oil company PDVSA has begun contacting customers with crude supply contracts, two people familiar to the matter said on Thursday, moving to resume cash sales to global refiners.

    JSON: {
        \"title\": \"\",
        \"tickers\": [\"OIL\"],
        \"keypoints\": [
            \"SINGAPORE (Reuters) - Oil prices rising about 1% \on Friday on fears that the Israel-Gaza conflict\",
            \"TBrent crude futures climbed 77 cents, or 0.8%, to $93.15 a barrel\",
            \"U.S. West Texas Intermediate crude was at $90.36 a barrel, up 99 cents, or 1.1%\",
            \"December WTI contract was at $89.13 a barrel, up 76 cents\",
            \"WTI prices could rise towards a high last seen in late September at $95.03 a barrel if it breaks resistance at $91.50\",
            \"Oil price are also supported by forecasts of widening deficit in the fourth quarter\",
        ],
    }
"""


SUMEX_TITLE = """
    TEXT: SINGAPORE (Reuters) - Oil prices extended gains on Friday, rising about 1% \on fears that the Israel-Gaza conflict may spread in the Middle East and disrupt supplies from one of the world's top-producing regions.

    Brent crude futures climbed 77 cents, or 0.8%, to $93.15 a barrel by 0042 GMT. U.S. West Texas Intermediate crude was at $90.36 a barrel, up 99 cents, or 1.1%. The front-month November contract expires on Friday.

    The more active December WTI contract was at $89.13 a barrel, up 76 cents.

    Both contracts are on track to post a second weekly gain as an explosion at a Gaza hospital this week and the anticipated ground invasion by Israeli troops heightened fears of the conflict spreading in the Middle East.

    "It's quite scary in fact, looks like things could spiral out of control," IG analyst Tony Sycamore said. "The bigger concern remains that the escalation of tension that we're likely to see with regard to the IDF (Israel Defence Forces) entering Gaza this weekend means the risk to crude oil are towards higher prices."

    Israeli Defence Minister Yoav Gallant told troops gathered at the Gaza border on Thursday that they would soon see the Palestinian enclave "from inside", suggesting an expected ground invasion could be nearing.

    U.S. intercepted missiles fired from Yemen toward Israel, Pentagon said.

    WTI prices could rise towards a high last seen in late September at $95.03 a barrel if it breaks resistance at $91.50, Sycamore said.

    Oil price are also supported by forecasts of widening deficit in the fourth quarter after top producers Saudi Arabia and Russia extended supply cuts to the end of the year and amid low inventories especially in the United States.

    Washington is seeking to buy 6 million barrels of crude for delivery to the Strategic Petroleum Reserve in December and January, as it continues its plan to replenish the emergency stockpile, the U.S. Department of Energy said on Thursday.

    Separately, a temporary lifting of U.S. oil sanctions on OPEC member Venezuela is unlikely to require any policy changes by the OPEC+ producer group for the time being as a recovery in production is likely to be gradual, OPEC+ sources told Reuters.

    Venezuelan state-run oil company PDVSA has begun contacting customers with crude supply contracts, two people familiar to the matter said on Thursday, moving to resume cash sales to global refiners.

    TITLE: Oil climbs on Mideast contagion fears from Israel-Gaza conflict
"""


example_prompt = """
<s>[INST]
I have the following document:
- The website mentions that it only takes a couple of days to deliver but I still have not received mine.

Please give me the keywords that are present in this document and separate them with commas.
Make sure you to only return the keywords and say nothing else. For example, don't say:
"Here are the keywords present in the document"
[/INST] meat, beef, eat, eating, emissions, steak, food, health, processed, chicken</s>"""


RULE_KEYWORDS_OLD = """
    <s>[INST] <<SYS>>
        You are a financial expert.
        From a text, you can extract stock tickers includes this text.
        Your response must be noun
        You are to the point and only give the answer in isolation without any chat-based fluff.
    <</SYS>>
"""
EXAMPLE_KEYWORDS_OLD = """
    The following is a text. Please extract stocks from this:
    - The Vietnamese Stock Exchange (VNX) saw a decline of nearly 40% \from its previous high price of 75,600 dong to 45,950 dong per share; the Vietnam Real Estate Company (VRE) experienced a 12% \decline from 31,300 dong to 27,450 dong per share.
    VNX has been in a downturn for nearly two weeks now in the range of 43.x - 46.x (with prices falling rapidly) and VRE is currently one of the leading companies involved in the recovery process, having increased by 7.6% \over the past six trading sessions.
    Stock VIC (Vingroup) has experienced a significant drop within the last two weeks, with strong selling pressure and significant discounts. 
    According to last week's trading data, VN-Index fell 26 points from the previous day's index of 1.154. The share market dropped by approximately 9.36% within two weeks, reaching a low of 120 points. The decline in stock prices over the past two weeks has been significant and continuous, indicating that investors are becoming increasingly cautious.
    After falling to 1.150 points, VN-Index began to recover and the buying pressure increased with strong discounts within the range of 43.x - 46.x (the lowest point in the past six years) with a discount of up to 20 billion dongs per share. 
    Meanwhile, VRE stock has been the leading stock in the process of recovering, with an increase of 7.6% \over the past six days, returning to its current level.
    According to Mr. Nhan, although he is not an investor in the Vingroup stock group, the active movements of this stock group are still worth paying attention to.
    With the decline in stock prices, the viability of the stock market and the banking sector will depend on various factors such as the performance of individual stocks and industries. Although the decline in stock prices has slowed down, it is unlikely to stop completely. 
    In Q4/2023, VIC stock is expected to recover to a range of 53.0 - 55.0 points with the support of other related stocks such as VHM and VRE. However, with this forecast, there are also opportunities for the VN-Index to return to its normal level before the end of the quarter.
    [/INST] VNX, VRE, VIC, VN-Index, VHM [INST]
    The following is a text. Please extract stocks from this:
    - The residential real estate and industrial park real estate sectors showed significant divergence. Among the gainers, IDC rocketed by 5.2 percent, ITA climbed by 3.1 percent, PDR soared by 4.73 percent, VIC grew by 2.1 percent, BCM gained by 2.5 percent, KBC edged up by 1.09 percent, VCG increased by 2.56 percent, HDG added up by 2.93 percent, and CTD surged by 4.96 percent. Additionally, several penny stocks, including QCG, ITC, PTL, TLD, and VRC, reached the trading limit. On the other hand, several other stocks experienced notable declines, such as DIG dropping by 3.11 percent, DXG losing by 1.38 percent, DXS sliding by 1.31 percent, CII weakening by 1.7 percent, and LGC chopping by 2.07 percent.
    [/INST] IDC, ITA, PDR, VIC, BCM, KBC, VCG, HDG, CTD, QCG, ITC, PTL, TLD, VRC, DIG, DXG, DXS, CII, LGC [INST]
    The following is a text. Please extract stocks from this:
"""

TEST_ALL = """
    <s><<SYS>>
        You are a financial expert.
        You can tell what happend about stocks from text.
        Your response must be from text provided, dont search from internet.
        You are to the point and only give the answer in isolation without any chat-based fluff.

        Your result must folow this rule
        Nouns: you must find out all nouns from text
        Stocks: from nouns found, you must find stocks mentioned
        Topic: you must sumary about stocks from text
        Verbs: you must find all verbs from sumary
        Point: from this verbs, you must evaluate verb nuances by point, if positive give positive numbers, if negative give negative numbers
        Total: from all result, summarize by json type

        Only using information from text
        Make sure you to only return the result and say nothing else.
    <</SYS>>
"""
TEST_ALL = """
[INST]Please summary what happend from this text:
    -The Vietnamese Stock Exchange (VNX) saw a decline of nearly 40% from its previous high price of 75,600 dong to 45,950 dong per share; the Vietnam Real Estate Company (VRE) experienced a 12% \decline from 31,300 dong to 27,450 dong per share.According to last week's trading data, VN-Index fell 26 points from the previous day's index of 1.154. The share market dropped by approximately 9.36% within two weeks, reaching a low of 120 points. The decline in stock prices over the past two weeks has been significant and continuous, indicating that investors are becoming increasingly cautious.After falling to 1.150 points, VN-Index began to recover and the buying pressure increased with strong discounts within the range of 43.x - 46.x (the lowest point in the past six years) with a discount of up to 20 billion dongs per share. 
[/INST]Nouns: The Vietnamese Stock Exchange, The Vietnam Real Estate Company, VN-Index, The share market, VN-Index
    Stocks: VNX, VRE, VN-Index
    Topic:
        - VNX decline of nearly 40% f rom its previous high price of 75,600 dong to 45,950 dong per share.
        - VRE experienced a 12% decline from 31,300 dong to 27,450 dong per share.
        - VN-Index fell 26 points from the previous day's index of 1.154, after falling to 1.150 points, buying pressure increased the range of 43.x - 46.x with a discount of up to 20 billion dongs per share.
    Verb:
        - VNX: decline
        - VRE: decline
        - VN-Index: fell, falling, increased
    Point:
        - VNX: -2
        - VRE: -2
        - VN-Index: -2, -3, 4
    Total:{
        "Stocks": ["VNX", "VRE", "VN-Index"],
        "Topic": [
            "VNX decline of nearly 40% from its previous high price of 75,600 dong to 45,950 dong per share",
            "VRE experienced a 12% \decline from 31,300 dong to 27,450 dong per share",
            "VN-Index fell 26 points from the previous day's index of 1.154, after falling to 1.150 points, buying pressure increased the range of 43.x - 46.x with a discount of up to 20 billion dongs per share"
        ],
        "Point": [
            "VNX 3",
            "VRE 3",
            "VN-Index 4",
        ]
    }
[INST]Please summary what happend from this text:
    -Vingroup grew by 2.1 percent, BCM gained by 2.5 percent, KBC edged up by 1.09 percent. Additionally, several penny stocks, including QCG, TLD, and VRC, reached the trading limit. Meanwhile, VRE stock has been the leading stock in the process of recovering, with an increase of 7.6% \over the past six days, returning to its current level.
[/INST]Nouns: Vingroup, BCM, KBC, QCG, TLD, VRC, VRE
    Stocks: VIC ,BCM, KBC, QCG, TLD, VRC, VRE
    Topic:
        - VIC grew by 2.1 percent.
        - BCM gained by 2.5 percent.
        - KBC edged up by 1.09 percent.
        - QCG, TLD, and VRC reached the trading limit
        - VRE increase of 7.6% \over the past six days
    Verb effected:
        - VIC: grew
        - BCM: gained
        - KBC: edged up
        - QCG: reached
        - TLD: reached
        - VRC: reached
        - VRE: increase
    Point:
        - VIC: 2
        - BCM: 2
        - KBC: 2
        - QCG: 1
        - TLD: 1
        - VRC: 1
        - VRE: 2
    Total:{
        "Stocks": ["VIC" , "BCM", "KBC", "QCG", "TLD", "VRC", "VRE"],
        "Topic": [
            "VIC grew by 2.1 percent",
            "BCM gained by 2.5 percent",
            "KBC edged up by 1.09 percent",
            "QCG, TLD, and VRC reached the trading limit",
            "VRE increase of 7.6% \over the past six days",
        ],
        "Point": [
            "VIC 7",
            "BCM 7",
            "KBC 7",
            "QCG 6",
            "TLD 6",
            "VRC 6",
            "VRE 7",
        ],
    }
"""

RULE_KEYWORDS = """
        You are a financial expert.
        From a text, you can extract stock tickers includes this text.
        Your response must be noun
        You are to the point and only give the answer in isolation without any chat-based fluff.
"""
EXAMPLE_KEYWORDS = """
[INST]Please extract key points from this text:
    -The Vietnamese Stock Exchange (VNX) saw a decline of nearly 40% \from its previous high price of 75,600 dong to 45,950 dong per share; the Vietnam Real Estate Company (VRE) experienced a 12% \decline from 31,300 dong to 27,450 dong per share.According to last week's trading data, VN-Index fell 26 points from the previous day's index of 1.154. The share market dropped by approximately 9.36% within two weeks, reaching a low of 120 points. The decline in stock prices over the past two weeks has been significant and continuous, indicating that investors are becoming increasingly cautious.After falling to 1.150 points, VN-Index began to recover and the buying pressure increased with strong discounts within the range of 43.x - 46.x (the lowest point in the past six years) with a discount of up to 20 billion dongs per share. 
[/INST]- The Vietnamese Stock Exchange (VNX) decline of nearly 40% \from its previous high price of 75,600 dong to 45,950 dong per share
- the Vietnam Real Estate Company (VRE) experienced a 12% \decline from 31,300 dong to 27,450 dong per share
- VN-Index fell 26 points from the previous day's index of 1.154, after falling to 1.150 points, buying pressure increased the range of 43.x - 46.x with a discount of up to 20 billion dongs per share

[INST]Please extract key points from this text:
    - Vingroup grew by 2.1 percent, BCM gained by 2.5 percent, KBC edged up by 1.09 percent. Additionally, several penny stocks, including QCG, TLD, and VRC, reached the trading limit. Meanwhile, VRE stock has been the leading stock in the process of recovering, with an increase of 7.6% \over the past six days, returning to its current level.
[/INST]- Vingroup grew by 2.1 percent
- BCM gained by 2.5 percent
- KBC edged up by 1.09 percent
- QCG, TLD, and VRC reached the trading limit
- VRE increase of 7.6% \over the past six days
"""

EXAMPLE_TOPIC = """
[INST]Please extract key points from this text:
-The Vietnamese Stock Exchange (VNX) saw a decline of nearly 40% \from its previous high price of 75,600 dong to 45,950 dong per share; the Vietnam Real Estate Company (VRE) experienced a 12% \decline from 31,300 dong to 27,450 dong per share.According to last week's trading data, VN-Index fell 26 points from the previous day's index of 1.154. The share market dropped by approximately 9.36% within two weeks, reaching a low of 120 points. The decline in stock prices over the past two weeks has been significant and continuous, indicating that investors are becoming increasingly cautious.After falling to 1.150 points, VN-Index began to recover and the buying pressure increased with strong discounts within the range of 43.x - 46.x (the lowest point in the past six years) with a discount of up to 20 billion dongs per share. 
[/INST]- The Vietnamese Stock Exchange (VNX) decline of nearly 40% \from its previous high price of 75,600 dong to 45,950 dong per share
- The Vietnam Real Estate Company (VRE) experienced a 12% \decline from 31,300 dong to 27,450 dong per share
- VN-Index fell 26 points from the previous day's index of 1.154, after falling to 1.150 points, buying pressure increased the range of 43.x - 46.x with a discount of up to 20 billion dongs per share
"""

RULE_TOPIC = """
You are a financial expert.
You can extract key points from from text.
You are to the point and only give the answer in isolation without any chat-based fluff.
Each key points must be one to two sentences.
Each key points marked with "-" characters, don't marked with numbers or anything else
Make sure you to only return the key points and say nothing else. For example, don't say:
"Key points extracted:"
"""
EXAMPLE_TOPIC_Old = """
    Please summary what happend about VNX, VRE, VIC, VN-Index, VHM from this text:
    - The Vietnamese Stock Exchange (VNX) saw a decline of nearly 40% \from its previous high price of 75,600 dong to 45,950 dong per share; the Vietnam Real Estate Company (VRE) experienced a 12% \decline from 31,300 dong to 27,450 dong per share.
    VNX has been in a downturn for nearly two weeks now in the range of 43.x - 46.x (with prices falling rapidly) and VRE is currently one of the leading companies involved in the recovery process, having increased by 7.6% \over the past six trading sessions.
    Stock VIC (Vingroup) has experienced a significant drop within the last two weeks, with strong selling pressure and significant discounts. 
    According to last week's trading data, VN-Index fell 26 points from the previous day's index of 1.154. The share market dropped by approximately 9.36% within two weeks, reaching a low of 120 points. The decline in stock prices over the past two weeks has been significant and continuous, indicating that investors are becoming increasingly cautious.
    After falling to 1.150 points, VN-Index began to recover and the buying pressure increased with strong discounts within the range of 43.x - 46.x (the lowest point in the past six years) with a discount of up to 20 billion dongs per share. 
    Meanwhile, VRE stock has been the leading stock in the process of recovering, with an increase of 7.6% \over the past six days, returning to its current level.
    According to Mr. Nhan, although he is not an investor in the Vingroup stock group, the active movements of this stock group are still worth paying attention to.
    With the decline in stock prices, the viability of the stock market and the banking sector will depend on various factors such as the performance of individual stocks and industries. Although the decline in stock prices has slowed down, it is unlikely to stop completely. 
    In Q4/2023, VIC stock is expected to recover to a range of 53.0 - 55.0 points with the support of other related stocks such as VHM and VRE. However, with this forecast, there are also opportunities for the VN-Index to return to its normal level before the end of the quarter.
    [/INST] {"VNX" : ["VNX decline of nearly 40% \from its previous high price of 75,600 dong to 45,950 dong per share", "in a downturn for nearly two weeks now in the range of 43.x - 46.x"],
        "VRE" : ["VRE experienced a 12% \decline from 31,300 dong to 27,450 dong per share", "having increased by 7.6% \over the past six trading sessions", "has been the leading stock in the process of recovering, with an increase of 7.6% \over the past six days, returning to its current level"], 
        "VIC" : ["VIC has experienced a significant drop within the last two weeks, with strong selling pressure and significant discounts", "expected to recover to a range of 53.0 - 55.0 points with the support of other related stocks such as VHM and VRE"], 
        "VN-Index" : ["VN-Index falling to 1.150 points" , "VN-Index began to recover and the buying pressure increased with strong discounts within the range of 43.x - 46.x (the lowest point in the past six years) with a discount of up to 20 billion dongs per share"], 
        "VHM" : []} [INST]
    Please summary what happend about IDC, ITA, PDR, VIC, BCM, KBC, VCG, HDG, CTD, QCG, ITC, PTL, TLD, VRC, DIG, DXG, DXS, CII, LGC from this text:
    - The residential real estate and industrial park real estate sectors showed significant divergence. 
    Among the gainers, IDC rocketed by 5.2 percent, ITA climbed by 3.1 percent, PDR soared by 4.73 percent, 
    VIC grew by 2.1 percent, BCM gained by 2.5 percent, KBC edged up by 1.09 percent, VCG increased by 2.56 percent, HDG added up by 2.93 percent, and CTD surged by 4.96 percent. 
    Additionally, several penny stocks, including QCG, ITC, PTL, TLD, and VRC, reached the trading limit. 
    On the other hand, several other stocks experienced notable declines, such as DIG dropping by 3.11 percent, DXG losing by 1.38 percent, DXS sliding by 1.31 percent, CII weakening by 1.7 percent, and LGC chopping by 2.07 percent.
    [/INST] {"IDC" : ["IDC rocketed by 5.2 percent"],
        "ITA" : ["ITA climbed by 3.1 percent"],
        "PDR" : ["PDR soared by 4.73 percent"],
        "VIC" : ["VIC grew by 2.1 percent"],
        "BCM" : ["BCM gained by 2.5 percent"],
        "KBC" : ["KBC edged up by 1.09 percent"],
        "VCG" : ["VCG increased by 2.56 percent"],
        "HDG" : ["HDG added up by 2.93 percent"],
        "CTD" : ["CTD surged by 4.96 percent"],
        "QCG" : ["several penny stocks, including QCG, ITC, PTL, TLD, and VRC, reached the trading limit"],
        "ITC" : ["several penny stocks, including QCG, ITC, PTL, TLD, and VRC, reached the trading limit"],
        "PTL" : ["several penny stocks, including QCG, ITC, PTL, TLD, and VRC, reached the trading limit"],
        "TLD" : ["several penny stocks, including QCG, ITC, PTL, TLD, and VRC, reached the trading limit"],
        "VRC" : ["several penny stocks, including QCG, ITC, PTL, TLD, and VRC, reached the trading limit"],
        "DIG" : ["DIG dropping by 3.11 percent"],
        "DXG" : ["DXG losing by 1.38 percent"],
        "DXS" : ["DXS sliding by 1.31 percent"],
        "CII" : ["CII weakening by 1.7 percent"],
        "LGC" : ["LGC chopping by 2.07 percent"]} [INST]
"""

TITLE_RULE = """
You are a financial expert.
You can sumary and give a title from a financial text.
"""
LABEL_RULE = """
You are a financial expert.
You can labels financials text provided is Negative or Positive.
You only give the labels without any chat-based fluff.
Only give the labels on your response, dont give me like "In this case" or something like that

[INST]Please label each item:
- ITA climbed by 3.1 percent
- DIG dropping by 3.11 percent
- VN-Index falling to 1.150 points
- VCG increased by 2.56 percent
[/INST]- Negative
- Positive
- Positive
- Negative
"""
TICKERS_RULE = """
    You are a financial expert.
    You can find all nouns and find which stocks mentioned.
"""

TICKERS_EXAMPLE = """
[INST]please find the VietNam companies fron this text:
"The Vietnamese Stock Exchange (VNX) saw a decline of nearly 40% \from its previous high price of 75,600 dong to 45,950 dong per share; 
the Vietnam Real Estate Company (VRE) experienced a 12% \decline from 31,300 dong to 27,450 dong per share."
The VN30-Index, tracking the 30 biggest stocks on HoSE, also lost 37.75 points, or 3.15 per cent, to 1,159.94 points. 
In the VN30 basket, 26 stocks went down with four hitting the maximum intraday loss of 7 per cent. In contrast, only three stocks edged higher today and one ended flat."
[/INST]The Vietnamese Stock Exchange (VNX), the Vietnam Real Estate Company (VRE), VN30
"""
