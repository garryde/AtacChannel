# Atac Channel
This project is aiming to crawl the Twitter account [@InfoAtac](https://twitter.com/InfoAtac) which is the official account of the Rome public transport company and send it by telegram channel with different languages.

## Prepare
1. Apply a [Twitter Bearer Token](https://developer.twitter.com/en/docs/authentication/oauth-2-0/bearer-tokens) to grab tweet from Twitter.

2. Creat a [Telegram Channel](https://telegram.org/tour/channels#:~:text=Channels%20are%20a%20tool%20for,have%20the%20right%20to%20post.) and set its Telegram Channel ID 

3. Create a [Telegram Bot](https://core.telegram.org/bots)  and get its token

4. Sign up a [Deepl free developer account](https://www.deepl.com/en/pro#developer) and create a [Authentication Key](https://www.deepl.com/docs-api/accessing-the-api/)

## Using

1. Run `AtacBot.py` to generate the configuration file `config.ini`
2. Configure `config.ini`
3. Rerun `AtacBot.py`



## config.ini

|         Name         |     Type     |                                             Description                                              |
| :------------------: |:------------:|:----------------------------------------------------------------------------------------------------:|
| twitter_bearer_token |    String    | [Twitter Bearer Token](https://developer.twitter.com/en/docs/authentication/oauth-2-0/bearer-tokens) |
|      bot_token       |    String    |                         [Telegram Bot Token](https://core.telegram.org/bots)                         |
|       chat_id        |    String    |                                         Telegram Channel ID                                          |
|    deepl_auth_key    |    String    |               [Deepl API Auth Key](https://www.deepl.com/docs-api/accessing-the-api/)                |
|    target_lang    |    String    |       [Target translate language](https://www.deepl.com/zh/docs-api/translating-text/request/)       |
|   heartbeat_monitor   |    String    |                         Heartbeat URL. Leave empty to disable this function.                         |
|   tweets_sent_list   | String Array |                           Store the last five tweets sent(no need to fill)                           |
|  tweets_white_list   | String Array |                     Only send tweets that contain keywords (not case sensitive)                      |
|  tweets_black_list   | String Array |                     Only send tweets that without keywords (not case sensitive)                      |
|     str_del_list     | String Array |                      Delete the keyword specified in the Tweet(case sensitive)                       |
|     no_translate_list     | String Array |                                      Vocabulary not translated                                       |

