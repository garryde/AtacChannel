import deepl


class Deepl:
    def __init__(self, auth_key):
        self.auth_key = auth_key
        self.translator = deepl.Translator(auth_key)

    def translate_to_zh(self, message):
        return str(self.translator.translate_text(message, target_lang="ZH"))

    def translate_to_en(self, message):
        return str(self.translator.translate_text(message, target_lang="EN-GB"))
