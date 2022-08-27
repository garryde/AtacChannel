import telegram
import logging


class Telegram:
    def __init__(self, bot_token):
        self.bot_token = bot_token
        self.bot = telegram.Bot(bot_token)

    def send_message(self, chat_id, message):
        try:
            self.bot.send_message(chat_id, message, parse_mode=telegram.ParseMode.HTML)
        except Exception as e:
            logging.warning("Send message wrong; " + str(e))

    def send_muted_message(self, chat_id, message):
        try:
            self.bot.send_message(chat_id, message, parse_mode=telegram.ParseMode.HTML, disable_notification=True)
        except Exception as e:
            logging.warning("Send muted message wrong; " + str(e))
