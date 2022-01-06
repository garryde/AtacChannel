from datetime import datetime
import util


class Tweet:
    def __init__(self, tweets_sent_list=[], tweets_blocked_list=[]):
        self.tweets_sent_list = tweets_sent_list
        self.tweets_blocked_list = tweets_blocked_list

    def tweet_add_sent(self, tweet_id: int):
        if len(self.tweets_sent_list) >= 10:
            self.tweets_sent_list.pop(0)
        self.tweets_sent_list.append(str(tweet_id))

    def tweet_check_sent(self, tweet_id: int):
        if str(tweet_id) in self.tweets_sent_list:
            return True
        else:
            return False

    def tweet_check_blocked(self, tweet_text: str):
        for block_tweet in self.tweets_blocked_list:
            if block_tweet in tweet_text:
                return True
        return False

    @staticmethod
    def tweetid_to_dt(tweet_id: int):
        shifted = tweet_id >> 22
        timestamp = shifted + 1288834974657
        time_created = datetime.fromtimestamp(timestamp / 1000).strftime('%Y-%m-%d %H:%M:%S')
        return time_created
