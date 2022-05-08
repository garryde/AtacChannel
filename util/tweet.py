from datetime import datetime
import random

class Tweet:
    def __init__(self, tweets_sent_list=[], tweets_white_list=[], tweets_blocked_list=[], no_translate_list=[]):
        self.tweets_sent_list = tweets_sent_list
        self.tweets_white_list = tweets_white_list
        self.tweets_blocked_list = tweets_blocked_list
        self.no_translate_list = no_translate_list
        self.no_translate_dic = {}
        for i in no_translate_list:
            self.no_translate_dic[i] = str(random.randint(100000, 999999))
        self.no_translate_dic_rev = dict(zip(self.no_translate_dic.values(), self.no_translate_dic.keys()))

    def tweet_add_sent(self, tweet_id: int):
        if len(self.tweets_sent_list) >= 10:
            self.tweets_sent_list.pop(0)
        self.tweets_sent_list.append(str(tweet_id))

    def tweet_check_sent(self, tweet_id: int):
        if str(tweet_id) in self.tweets_sent_list:
            return True
        else:
            return False

    def tweet_check_blacklist(self, tweet_text: str):
        """
        Check whether tweet include blocked key word.
        :param tweet_text:
        :return: Return True if it is blocked.
        """
        for block_tweet in self.tweets_blocked_list:
            if block_tweet.lower() in tweet_text.lower():
                return True
        return False

    def tweet_check_whitelist(self, tweet_text: str):
        """
        Check whether tweet include whitelist key word.
        :param tweet_text:
        :return: Return True if it is in white list.
        """
        for allowed_tweet in self.tweets_white_list:
            if allowed_tweet.lower() in tweet_text.lower():
                return True
        return False

    def tweet_convert_before_trans(self, tweet_text: str):
        for no_translate in self.no_translate_dic.items():
            tweet_text.replace(no_translate[0], no_translate[1])
        return tweet_text

    def tweet_convert_after_trans(self, tweet_text: str):
        for no_translate in self.no_translate_dic_rev.items():
            tweet_text.replace(no_translate[0], no_translate[1])
        return tweet_text

    @staticmethod
    def tweetid_to_dt(tweet_id: int):
        shifted = tweet_id >> 22
        timestamp = shifted + 1288834974657
        time_created = datetime.fromtimestamp(timestamp / 1000).strftime('%Y-%m-%d %H:%M:%S')
        return time_created
