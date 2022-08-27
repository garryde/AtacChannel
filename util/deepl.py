import deepl
import logging
from enum import Enum


class Deepl:
    def __init__(self, auth_key, target_lang="ZH"):
        self.auth_key = auth_key
        self.translator = deepl.Translator(auth_key)
        self.target_lang = target_lang
        self.flag = Flags[target_lang.replace("-", "_")].value

    def translate(self, message):
        try:
            return str(self.translator.translate_text(message, target_lang=self.target_lang))
        except Exception as e:
            logging.warning("Translate message wrong; " + str(e))


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
