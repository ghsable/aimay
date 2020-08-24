# TEST
This is LINE Bot.

## Try it out!
Use this Line QR code to add the Bot:  
**OR CODE**

## Usage
* This Bot only supports Japanese.

Example:

| Push Message | Reply Message |
| :--- | :--- |
| おはよう | おやようございますニャン |
| ねむい | 私もねむいですニャン |
| 🦜おうむがえし！ | 🦜おうむがえし！ |
| ちゅーる買ったよ | ちゅーるたべたいニャン |
| りんりん(相棒)の調子はどう？ | りんりんは寝ているニャン |
| いい音楽ないかな | これを聴いているニャン<br>タイトル,[URL](https://www.youtube.com/?gl=JP) |
| 映画見たい | これを観ているニャン<br>[タイトル\nあらすじ](https://www.themoviedb.org/?language=ja) |
| 天気どうなるかな | ここを見ているニャン<br>[URL](https://www.google.co.jp/search?q=天気) |
| おやすみー | [sticker](https://developers.line.biz/media/messaging-api/sticker_list.pdf) |

## Development
* [LINE](https://line.me/ja/) + [Python](https://www.python.org/) [3.8.5](https://github.com/ghsable/test/blob/master/runtime.txt) + [modules](#modules) + [GitHub](https://github.com/) + [Heroku](https://jp.heroku.com/) = (⋈MAY◍＞◡＜◍)。✧♡

### modules

| Homepage                                                         | [PyPI](https://pypi.org/)                              | [GitHub](https://github.com/)                                           | [Version](https://github.com/ghsable/test/blob/master/requirements.txt) | Environment variable                                 |
| :---                                                             | :---                                                   | :---                                                                    | :---                                                                    | :---                                                 |
| [LINE Developers](https://developers.line.biz/ja/)               | [line-bot-sdk](https://pypi.org/project/line-bot-sdk/) | [line/line-bot-sdk-python](https://github.com/line/line-bot-sdk-python) | `1.16.0`                                                                | `LINE_CHANNEL_ACCESS_TOKEN`<br>`LINE_CHANNEL_SECRET` |
| [Flask](https://flask.palletsprojects.com/en/1.1.x/)             | [Flask](https://pypi.org/project/Flask/)               | [pallets/flask](https://github.com/pallets/flask)                       | `1.1.2`                                                                 | `-`                                                  |
| [TMDb](https://www.themoviedb.org/?language=ja)                  | [tmdbv3api](https://pypi.org/project/tmdbv3api/)       | [AnthonyBloomer/tmdbv3api](https://github.com/AnthonyBloomer/tmdbv3api) | `1.6.2`                                                                 | `TMDB_API_KEY`                                       |
| [A3RT/TalkAPI](https://a3rt.recruit-tech.co.jp/product/talkAPI/) | [pya3rt](https://pypi.org/project/pya3rt/)             | [nocotan/pya3rt](https://github.com/nocotan/pya3rt)                     | `1.1`                                                                   | `A3RT_TALKAPI_APIKEY`                                |
