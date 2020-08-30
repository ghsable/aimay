<p align="center">
  <img src="https://raw.githubusercontent.com/ghsable/test/master/README/may.png" width="150" height="150" align="center" alt="may">
  <h2 align="center">LINE Bot AI May</h2>
  <p align="center">🤖 -> 🐈 <- 🧠</p>
</p>
  <p align="center">
    <a href="https://github.com/ghsable/test/actions">
      <img alt="Deploy Passing" src="https://github.com/ghsable/test/workflows/Deploy/badge.svg">
    </a>
  </p>

## Try it out!
Use this Line QR code to add the Bot:  
**OR CODE**

## Usage
* This Bot only supports 🗾[Japanese](https://en.wikipedia.org/wiki/Japanese_language)

Example:

| Push Message | Reply Message |
| :--- | :--- |
| おはよう | おはようございますニャン |
| ねむい | 私もねむいですニャン |
| 🦜おうむがえし！ | 🦜おうむがえし！ニャン |
| ちゅーるを買ったよ | ちゅーるを食べたいニャン |
| りんりん(相棒)の調子はどう？ | りんりんは寝ているニャン |
| いい音楽ないかな | これを聴いているニャン<br>[あいみょん,裸の心](https://www.youtube.com/watch?v=yOAwvRmVIyo) |
| 映画を観たいな | これを観ているニャン<br>[イミテーション・ゲーム](https://filmarks.com/movies/57847) |
| 面白いドラマあるかな | ここを見ているニャン<br>[Filmarks](https://filmarks.com/list-drama/trend)<br>[TMDb](https://www.themoviedb.org/tv?language=ja) |
| ゲームをやろうかな | ここを見ているニャン<br>[Metacritic](https://www.metacritic.com/game) |
| 天気どうなるかな | ここを見ているニャン<br>[Google天気](https://www.google.co.jp/search?q=天気) |
| おやすみー | [sticker](https://developers.line.biz/media/messaging-api/sticker_list.pdf) |

## Development
* [LINE](https://line.me/ja/) x ([Python](https://www.python.org/) [3.8.5](https://github.com/ghsable/test/blob/master/runtime.txt) + [modules](#modules)) x ([GitHub](https://github.com/) + [Actions](#actions)) x [Heroku](https://jp.heroku.com/) = (⋈MAY◍＞◡＜◍)。✧♡RIN♡

### modules

| Homepage                                                         | PyPI                                                   | GitHub                                                                      | [Version](https://github.com/ghsable/test/blob/master/requirements.txt) | Environment variable(Heroku)                         |
| :---                                                             | :---                                                   | :---                                                                        | :---                                                                    | :---                                                 |
| [LINE Developers](https://developers.line.biz/ja/)               | [line-bot-sdk](https://pypi.org/project/line-bot-sdk/) | [line/line-bot-sdk-python](https://github.com/line/line-bot-sdk-python)     | `1.16.0`                                                                | `LINE_CHANNEL_ACCESS_TOKEN`<br>`LINE_CHANNEL_SECRET` |
| [Flask](https://flask.palletsprojects.com/en/1.1.x/)             | [Flask](https://pypi.org/project/Flask/)               | [pallets/flask](https://github.com/pallets/flask)                           | `1.1.2`                                                                 | `-`                                                  |
| [YouTube](https://www.youtube.com/?gl=JP)                        | -                                                      | -                                                                           | `-`                                                                     | `-`                                                  |
| [TMDb](https://www.themoviedb.org/?language=ja)                  | ~~[tmdbv3api](https://pypi.org/project/tmdbv3api/)~~   | ~~[AnthonyBloomer/tmdbv3api](https://github.com/AnthonyBloomer/tmdbv3api)~~ | ~`1.6.2`~                                                               | ~~`TMDB_API_KEY`~~                                   |
| [Filmarks](https://filmarks.com/)                                | -                                                      | -                                                                           | `-`                                                                     | `-`                                                  |
| [Metacritic](https://www.metacritic.com/game)                    | -                                                      | -                                                                           | `-`                                                                     | `-`                                                  |
| [Google](https://www.google.com/)                                | -                                                      | -                                                                           | `-`                                                                     | `-`                                                  |
| [A3RT/TalkAPI](https://a3rt.recruit-tech.co.jp/product/talkAPI/) | [pya3rt](https://pypi.org/project/pya3rt/)             | [nocotan/pya3rt](https://github.com/nocotan/pya3rt)                         | `1.1`                                                                   | `A3RT_TALKAPI_APIKEY`                                |

### Actions
| Marketplace/Actions                                                         | Version  | Environment variable(GitHub)                            |
| :---                                                                        | :---     | :---                                                    |
| [Checkout](https://github.com/marketplace/actions/checkout)                 | `2.x.x`  | `-`                                                     |
| [Deploy to Heroku](https://github.com/marketplace/actions/deploy-to-heroku) | `3.4.6`  | `HEROKU_API_KEY`<br>`HEROKU_APP_NAME`<br>`HEROKU_EMAIL` |
