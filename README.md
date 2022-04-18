# Atac Bot
This project is aiming to crawl the Twitter account [@InfoAtac](https://twitter.com/InfoAtac) which is the official account of the Rome public transport company and send it by telegram channel with different languages.



## Using

1. Run `AtacBot.py` to generate the configuration file `config.ini`
2. Configure `config.ini`
3. Rerun `AtacBot.py`



## config.ini

|         Name         |     Type     |                         Description                          |
| :------------------: | :----------: | :----------------------------------------------------------: |
| twitter_bearer_token |    String    | [Twitter Bearer Token](https://developer.twitter.com/en/docs/authentication/oauth-2-0/bearer-tokens) |
|      bot_token       |    String    |     [Telegram Bot Token](https://core.telegram.org/bots)     |
|       chat_id        |    String    |                     Telegram Channel ID                      |
|    deepl_auth_key    |    String    | [Deepl API Auth Key](https://www.deepl.com/docs-api/accessing-the-api/) |
|   tweets_sent_list   | String Array |               Store the last five tweets sent                |
|  tweets_white_list   | String Array | Only send tweets that contain keywords (not case sensitive)  |
|  tweets_black_list   | String Array | Only send tweets that without keywords (not case sensitive)  |
|     str_del_list     | String Array |  Delete the keyword specified in the Tweet(case sensitive)   |

