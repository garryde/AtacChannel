import time

from requests import ReadTimeout

import util
import tweepy
import re

# Configuration
config_list = ["twitter_bearer_token", "bot_token", "chat_id", "deepl_auth_key", "tweets_sent_list", "tweets_white_list", "tweets_black_list", "str_del_list"]
con = util.Config(config_strs=config_list)
twitter_bearer_token = con.read_str("twitter_bearer_token")
bot_token = con.read_str("bot_token")
chat_id = con.read_str("chat_id")
deepl_auth_key = con.read_str("deepl_auth_key")
tweets_sent_list = con.read_list("tweets_sent_list")
tweets_white_list = con.read_list("tweets_white_list")
tweets_black_list = con.read_list("tweets_black_list")
str_del_list = con.read_list("str_del_list")

tg = util.Telegram(bot_token)
dl = util.Deepl(deepl_auth_key)
tw = util.Tweet(tweets_sent_list,tweets_white_list, tweets_black_list)
twee_client = tweepy.Client(bearer_token=twitter_bearer_token)

while True:
    # request recent 5 tweets
    try:
        result = twee_client.get_users_tweets(id='370690455', exclude=['replies', 'retweets'], max_results=5)
        for tweet in reversed(result.data):
            tweet_id = tweet.id
            tweet_text = tweet.text
            tweet_time = util.Tweet.tweetid_to_dt(tweet_id)
            # Check whether tweet in white list
            if len(tweets_white_list) > 0:
                if not tw.tweet_check_whitelist(tweet_text):
                    continue
            # Check whether sent and blocked
            if tw.tweet_check_sent(tweet_id): continue
            if tw.tweet_check_blacklist(tweet_text): continue
            # Delete useless string
            for str_del in str_del_list:
                tweet_text = tweet_text.replace(str_del, "")
            # Delete twitter url
            tweet_text = util.Url.del_twitter_url(tweet_text)
            # delete URl and Translate
            tweet_zh = dl.translate_to_zh(util.Url.del_url(tweet_text)).replace("#Metro", "Metro")

            message = tweet_time + "\n🇮🇹\n" + tweet_text + "\n🇨🇳\n" + tweet_zh
            tg.send_message(chat_id, message)
            tw.tweet_add_sent(tweet_id)
            con.write_config("tweets_sent_list", str(tweets_sent_list))
    except ReadTimeout:
        continue
    except ConnectionError:
        continue
    except Exception as e:
        print("********Unknown Exception********")
        print(e)
    finally:
        time.sleep(60)
