<p align="center">
  <img src="https://raw.githubusercontent.com/ghsable/aimay/master/.readme/may.png" width="150" height="150" align="center" alt="may">
  <h2 align="center">LINE Bot AI <a href="https://ghsable.github.io/aimay/">May</a></h2>
  <p align="center">🤖 -> 🐈 <- 🧠</p>
</p>
  <p align="center">
    <a href="https://github.com/ghsable/aimay/actions">
      <img alt="CI Passing" src="https://github.com/ghsable/aimay/workflows/CI/badge.svg">
    </a>
    <a href="https://codecov.io/gh/ghsable/aimay">
      <img alt="Codecov" src="https://codecov.io/gh/ghsable/aimay/branch/master/graph/badge.svg">
    </a>
    <a href="https://github.com/ghsable/aimay/issues">
      <img alt="GitHub Issues" src="https://img.shields.io/github/issues/ghsable/aimay?color=0088ff">
    </a>
    <a href="https://github.com/ghsable/aimay/pulls">
      <img alt="GitHub Pull requests" src="https://img.shields.io/github/issues-pr/ghsable/aimay?color=0088ff">
    </a>
  </p>
  <p align="center">
    <a href="https://app.fossa.com/projects/git%2Bgithub.com%2Fghsable%2Faimay?ref=badge_large">
      <img alt="FOSSA Status" src="https://app.fossa.com/api/projects/git%2Bgithub.com%2Fghsable%2Faimay.svg?type=large">
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
| おうむがえし！ | おうむがえし！ニャン |
| ちゅーるを買ったよ | ちゅーるを食べたいニャン |
| りんりん(相棒)の調子はどう？ | りんりんは寝ているニャン |
| いい音楽ないかな | これを聴いているニャン<br>[あいみょん,裸の心](https://www.youtube.com/watch?v=yOAwvRmVIyo) |
| 映画を観たいな | これを観ているニャン<br>[イミテーション・ゲーム](https://filmarks.com/movies/57847) |
| 面白いドラマあるかな | ここを見ているニャン<br>[Filmarks](https://filmarks.com/list-drama/trend)<br>[TMDb](https://www.themoviedb.org/tv?language=ja) |
| ゲームをやろうかな | ここを見ているニャン<br>[Metacritic](https://www.metacritic.com/game) |
| 天気どうなるかな | ここを見ているニャン<br>[Google天気](https://www.google.co.jp/search?q=天気) |
| おやすみー | [sticker](https://developers.line.biz/media/messaging-api/sticker_list.pdf) |

## Development
### Requirement
* [LINE](https://line.me/ja/)
* [Python](https://www.python.org/) [3.8.5](https://github.com/ghsable/aimay/blob/master/runtime.txt) + [navdeep-G/samplemod](https://github.com/navdeep-G/samplemod) + [modules](#modules)
* [GitHub](#github) + [actions](#actions) + [badges](#badges)
* [Heroku](https://jp.heroku.com/)
* cat<< [Requirement](#requirement) >(⋈MAY◍＞◡＜◍)。✧♡RIN♡

#### modules

| Homepage                                                         | PyPI                                                   | GitHub                                                                      | [Version](https://github.com/ghsable/aimay/blob/master/requirements.txt) | Environment variable(Heroku)                         |
| :---                                                             | :---                                                   | :---                                                                        | :---                                                                     | :---                                                 |
| [nose](https://nose.readthedocs.io/en/latest/)                   | [nose](https://pypi.org/project/nose/)                 | [nose-devs/nose](https://github.com/nose-devs/nose)                         | `1.3.7`                                                                  | `-`                                                  |
| [Sphinx](https://www.sphinx-doc.org/en/master/)                  | [Sphinx](https://pypi.org/project/Sphinx/)             | [sphinx-doc/sphinx](https://github.com/sphinx-doc/sphinx)                   | `3.2.1`                                                                  | `-`                                                  |
| [Codecov](https://codecov.io/)                                   | [codecov](https://pypi.org/project/codecov/)           | [codecov/codecov-python](https://github.com/codecov/codecov-python)         | `2.1.9`                                                                  | `-`                                                  |
| [LINE Developers](https://developers.line.biz/ja/)               | [line-bot-sdk](https://pypi.org/project/line-bot-sdk/) | [line/line-bot-sdk-python](https://github.com/line/line-bot-sdk-python)     | `1.16.0`                                                                 | `LINE_CHANNEL_ACCESS_TOKEN`<br>`LINE_CHANNEL_SECRET` |
| [Flask](https://flask.palletsprojects.com/en/1.1.x/)             | [Flask](https://pypi.org/project/Flask/)               | [pallets/flask](https://github.com/pallets/flask)                           | `1.1.2`                                                                  | `-`                                                  |
| [A3RT/TalkAPI](https://a3rt.recruit-tech.co.jp/product/talkAPI/) | [pya3rt](https://pypi.org/project/pya3rt/)             | [nocotan/pya3rt](https://github.com/nocotan/pya3rt)                         | `1.1`                                                                    | `A3RT_TALKAPI_APIKEY`                                |
| [TMDb](https://www.themoviedb.org/?language=ja)                  | ~~[tmdbv3api](https://pypi.org/project/tmdbv3api/)~~   | ~~[AnthonyBloomer/tmdbv3api](https://github.com/AnthonyBloomer/tmdbv3api)~~ | ~`1.6.2`~                                                                | ~~`TMDB_API_KEY`~~                                   |
| [YouTube](https://www.youtube.com/?gl=JP)                        | -                                                      | -                                                                           | `-`                                                                      | `-`                                                  |
| [Filmarks](https://filmarks.com/)                                | -                                                      | -                                                                           | `-`                                                                      | `-`                                                  |
| [Metacritic](https://www.metacritic.com/game)                    | -                                                      | -                                                                           | `-`                                                                      | `-`                                                  |
| [Google](https://www.google.com/)                                | -                                                      | -                                                                           | `-`                                                                      | `-`                                                  |

#### GitHub

| Homepage                                  | This Repository                           |
| :---                                      | :---                                      |
| [GitHub](https://github.com/)             | [aimay](https://github.com/ghsable/aimay) |
| [GitHub Pages](https://pages.github.com/) | [aimay](https://ghsable.github.io/aimay/) |

#### actions

| Marketplace/Actions                                                               | [Version](https://github.com/ghsable/aimay/blob/master/.github/workflows/main.yml)  | Environment variable(GitHub)                            |
| :---                                                                              | :---                                                                                | :---                                                    |
| [Checkout](https://github.com/marketplace/actions/checkout)                       | `2.x.x`                                                                             | `-`                                                     |
| -                                                                                 | `-`                                                                                 | `A3RT_TALKAPI_APIKEY`                                   |
| [Codecov](https://github.com/marketplace/actions/codecov)                         | `1.x.x`                                                                             | `CODECOV_TOKEN`                                         |
| [GitHub Pages action](https://github.com/marketplace/actions/github-pages-action) | `3.x.x`                                                                             | `GITHUB_TOKEN`                                          |
| [Deploy to Heroku](https://github.com/marketplace/actions/deploy-to-heroku)       | `3.4.6`                                                                             | `HEROKU_API_KEY`<br>`HEROKU_APP_NAME`<br>`HEROKU_EMAIL` |

#### badges

| Homepage                          | Application                                                   | This Repository                                                                            |
| :---                              | :---                                                          | :---                                                                                       |
| [Codecov](https://codecov.io/)    | [marketplace/codecov](https://github.com/marketplace/codecov) | [aimay](https://codecov.io/gh/ghsable/aimay)                                               |
| [Shields.io](https://shields.io/) | -                                                             | -                                                                                          |
| [FOSSA](https://fossa.com/)       | [fossabot](https://github.com/fossabot)                       | [aimay](https://app.fossa.com/projects/git%2Bgithub.com%2Fghsable%2Faimay?ref=badge_large) |

[BACK TO TOP](#readme)
