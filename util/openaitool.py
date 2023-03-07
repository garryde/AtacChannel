import logging
import openai


# OpenAI class to handle API calls
class OpenAiTool:
    def __init__(self, api_key, target_lang="Chinese"):
        openai.api_key = api_key
        self.target_lang = target_lang

    def translate(self, message):
        try:
            return openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system",
                     "content": f"Please translate the following message from italian into {self.target_lang}:"},
                    {"role": "user", "content": message}
                ]
            ).choices[0].message.content
        except Exception as e:
            logging.warning("OpenAI Translate message wrong; " + str(e))
