import telegram

class Telegram:
    def __init__(self, bot_token):
        self.bot_token = bot_token
        self.bot = telegram.Bot(bot_token)

    def send_message(self,chat_id, message):
        self.bot.send_message(chat_id, message, parse_mode=telegram.ParseMode.HTML)

    def send_muted_message(self,chat_id, message):
        self.bot.send_message(chat_id, message, parse_mode=telegram.ParseMode.HTML, disable_notification=True)

