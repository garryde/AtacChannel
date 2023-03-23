import asyncio
import time
import traceback

import requests.exceptions
import util
import tweepy
import logging

# Configuration
config_list = ["twitter_bearer_token", "bot_token", "chat_id","deeplx_url", "deepl_auth_key", "openai_auth_key", "target_lang",
               "heartbeat_monitor",
               "tweets_sent_list", "tweets_white_list", "tweets_black_list", "str_del_list", "no_translate_list"]
con = util.Config(config_strs=config_list)
twitter_bearer_token = con.read_str("twitter_bearer_token")
bot_token = con.read_str("bot_token")
chat_id = con.read_str("chat_id")
deeplx_url = con.read_str("deeplx_url")
deepl_auth_key = con.read_str("deepl_auth_key")
openai_auth_key = con.read_str("openai_auth_key")
target_lang = con.read_str("target_lang")
heartbeat_monitor = con.read_str("heartbeat_monitor")
tweets_sent_list = con.read_list("tweets_sent_list")
tweets_white_list = con.read_list("tweets_white_list")
tweets_black_list = con.read_list("tweets_black_list")
str_del_list = con.read_list("str_del_list")
no_translate_list = con.read_list("no_translate_list")

# objet init
tg = util.Telegram(bot_token)
dl = util.DeeplTool(deepl_auth_key, target_lang)
dlx = util.DeeplXTool(deeplx_url, target_lang)
oa = util.OpenAiTool(openai_auth_key)
tw = util.Tweet(tweets_sent_list, tweets_white_list, tweets_black_list, no_translate_list)
twee_client = tweepy.Client(bearer_token=twitter_bearer_token)

# logger init
log_format = '%(asctime)s; %(levelname)s; %(message)s'
logging.basicConfig(filename='logbook.log', encoding='utf-8', level=logging.INFO, format=log_format)
logging.getLogger('deepl').setLevel(logging.ERROR)

logging.info('System start successfully!')

# start loop
while True:
    # send heartbeat
    if heartbeat_monitor != "empty":
        if heartbeat_monitor.startswith("http://") or heartbeat_monitor.startswith("https://"):
            try:
                requests.get(heartbeat_monitor)
            except Exception as e:
                logging.warning("Heartbeat error.")
        else:
            raise Exception("Heartbeat monitor url has to start with http:// or https://")

    # request recent 5 twetweetsets
    try:
        try:
            result = twee_client.get_users_tweets(id='370690455', exclude=['replies', 'retweets'], max_results=5)
        except Exception as e:
            logging.warning("Get user tweets wrong; " + str(e))
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
            # Delete twitter url(For all languages)
            tweet_text = util.Url.del_twitter_url(tweet_text)
            # Tweet preprocessing
            tweet_text = tweet_text.replace("METRO ", "Metro ").replace("#Metro", "Metro")
            tweet_text = tweet_text.replace("ℹ", "").replace("ℹ️", "").replace("👉", "")
            # Delete URl(For translated version only)
            tweet_text_no_url = util.Url.del_url(tweet_text)
            if tweet_text_no_url == "": continue
            # protect no-translate words
            tweet_text_no_translate = tw.tweet_convert_before_trans(tweet_text_no_url)
            # DeepL Translate
            if deeplx_url != "":
                tweet_zh_deepl = dlx.translate(tweet_text_no_translate)
            elif deepl_auth_key != "":
                tweet_zh_deepl = dl.translate(tweet_text_no_translate)
            else:
                tweet_zh_deepl = None
            # restore no-translate words
            if tweet_zh_deepl is not None:
                tweet_zh_deepl = tw.tweet_convert_after_trans(tweet_zh_deepl)
            # OpenAI Translate
            tweet_zh_oa = oa.translate(tweet_text_no_url)

            # Send message
            message = tweet_time + "\n🇮🇹\n" + tweet_text
            if tweet_zh_deepl is None and tweet_zh_oa is None:
                raise Exception("No translation service available.")
            if tweet_zh_deepl is not None:
                message += "\n" + dl.flag + " DeepL" + "\n" + tweet_zh_deepl
            if tweet_zh_oa is not None:
                message += "\n" + "🤖️" + " ChatGPT" + "\n" + tweet_zh_oa

            tg.send_message(chat_id, message)
            tw.tweet_add_sent(tweet_id)
            con.write_config("tweets_sent_list", str(tweets_sent_list))
    except Exception as e:
        logging.error(traceback.print_exc())
        logging.error("Unknown Error; " + str(e))
        break
    finally:
        time.sleep(60)
