import re
import requests


class Url:

    @staticmethod
    def find_url(text: str):
        return re.search(r"http\S+", text)

    @staticmethod
    def del_url(text: str):
        return re.sub(r"http\S+", "", text)

    @staticmethod
    def get_real_url(url_str: str):
        try:
            return requests.head(url_str, stream=True).headers['Location']
        except KeyError:
            return url_str
    @staticmethod
    def is_twitter_url(url_str: str):
        return True if "twitter.com" in Url.get_real_url(url_str) else False

    @staticmethod
    def del_twitter_url(tweet_text: str):
        url = Url.find_url(tweet_text)
        # URL not detected
        if not bool(url):
            return tweet_text
        # URL from twitter
        elif Url.is_twitter_url(url.group()):
            return Url.del_url(tweet_text)
        # URL from others
        else:
            return tweet_text

