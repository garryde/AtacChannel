import json
import logging
import requests
from enum import Enum


# https://github.com/OwO-Network/DeepLX

class DeeplXTool:
    def __init__(self, url, target_lang="ZH"):
        self.url = url
        self.target_lang = target_lang
        self.flag = Flags[target_lang.replace("-", "_")].value

    def translate(self, message):
        try:
            data = json.dumps({"text": message, "target_lang": self.target_lang})
            response = requests.post(url=self.url, data=data)
            return json.loads(response.text)["data"]
        except Exception as e:
            logging.warning("DeepLX Translate message wrong; " + str(e))


class Flags(Enum):
    BG = "🇧🇬"
    CS = "🇨🇿"
    DA = "🇩🇰"
    DE = "🇩🇪"
    EL = "🇬🇷"
    EN_GB = "🇬🇧"
    EN_US = "🇺🇸"
    ES = "🇪🇸"
    ET = "🇪🇪"
    FI = "🇫🇮"
    FR = "🇫🇷"
    HU = "🇭🇺"
    IT = "🇮🇹"
    JA = "🇯🇵"
    LT = "🇱🇹"
    LV = "🇱🇻"
    NL = "🇳🇱"
    PL = "🇵🇱"
    PT_PT = "🇵🇹"
    PT_BR = "🇧🇷"
    RO = "🇷🇴"
    RU = "🇷🇺"
    SK = "🇸🇰"
    SL = "🇸🇮"
    SV = "🇸🇪"
    ZH = "🇨🇳"