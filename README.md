<p align="center">
  <a href="https://www.youtube.com/channel/UCZ6aj_JfxKjkaV8BLGw3WBw/about">
    <img src="https://raw.githubusercontent.com/ghsable/aimay/main/.readme/images/may_readme.png" width="150" height="150" align="center" alt="may">
  </a>
  <h2 align="center">LINE Bot AI <a href="https://ghsable.github.io/aimay/">May</a></h2>
  <p align="center">🤖 -> 🐈 <- 🧠</p>
</p>
  <p align="center">
    <a href="https://github.com/ghsable/aimay/actions">
      <img alt="CI Passing" src="https://github.com/ghsable/aimay/workflows/CI/badge.svg">
    </a>
    <a href="https://codecov.io/gh/ghsable/aimay">
      <img alt="Codecov" src="https://codecov.io/gh/ghsable/aimay/branch/main/graph/badge.svg">
    </a>
    <a href="https://app.codacy.com/manual/ghsable/aimay?utm_source=github.com&utm_medium=referral&utm_content=ghsable/aimay&utm_campaign=Badge_Grade_Settings">
      <img alt="Codacy Badge" src="https://api.codacy.com/project/badge/Grade/ee9e836cc9bb41ba8b8624cc5784513a">
    </a>
    <a href="https://www.codefactor.io/repository/github/ghsable/aimay">
      <img alt="CodeFactor" src="https://www.codefactor.io/repository/github/ghsable/aimay/badge">
    </a>
    <a href="https://codeclimate.com/github/ghsable/aimay/maintainability">
      <img alt="CodeClimate maintainability" src="https://api.codeclimate.com/v1/badges/e3f4d2f4c051c357b55a/maintainability">
    </a>
    <a href="https://github.com/ghsable/aimay/issues">
      <img alt="GitHub Issues" src="https://img.shields.io/github/issues/ghsable/aimay?color=0088ff">
    </a>
    <a href="https://github.com/ghsable/aimay/pulls">
      <img alt="GitHub Pull requests" src="https://img.shields.io/github/issues-pr/ghsable/aimay?color=0088ff">
    </a>
    <a href="https://gitter.im/ghsable/aimay?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge">
      <img alt="Gitter" src="https://badges.gitter.im/ghsable/aimay.svg">
    </a>
  </p>
  <p align="center">
    <a href="https://app.fossa.com/projects/git%2Bgithub.com%2Fghsable%2Faimay?ref=badge_large">
      <img alt="FOSSA Status" src="https://app.fossa.com/api/projects/git%2Bgithub.com%2Fghsable%2Faimay.svg?type=large">
    </a>
  </p>

# Table of Contents

* [LINE Bot AI May](#readme)
* [Table of Contents](#table-of-contents)
* [Try it out!](#try-it-out)
* [Usage](#usage)
* [Development](#development)
  * [Overview](#overview)
  * [Requirement](#requirement)
    * [modules](#modules)
    * [GitHub](#github)
    * [actions](#actions)
    * [badges](#badges)
    * [others](#others)
  * [app.run](#apprun)
  * [Versioning](#versioning)

# Try it out!

Use this Line QR code to add the Bot:  
[![](https://raw.githubusercontent.com/ghsable/aimay/main/.readme/images/QRCODE_S.png)](https://lin.ee/L7JQsBk)

# Usage

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

# Development

## Overview

[![overview](https://raw.githubusercontent.com/ghsable/aimay/main/.readme/drawio/overview.svg)](https://www.w3.org/Graphics/SVG/)

## Requirement

* [LINE](https://line.me/ja/)
* [Python](https://www.python.org/) [3.9.0](https://github.com/ghsable/aimay/blob/main/runtime.txt) + [navdeep-G/samplemod](https://github.com/navdeep-G/samplemod) + [modules](#modules)
* [GitHub](#github) + [actions](#actions) + [badges](#badges) + [others](#others)
* [Heroku](https://jp.heroku.com/)
* cat<< [Requirement](#requirement) >(⋈MAY◍＞◡＜◍)。✧♡RIN♡

### modules

| Homepage                                                         | PyPI                                                   | GitHub                                                                    | [Version](https://github.com/ghsable/aimay/blob/main/requirements.txt) | Environment variable(Heroku)                         |
| :---                                                             | :---                                                   | :---                                                                      | :---                                                                   | :---                                                 |
| ~[uWSGI](https://uwsgi-docs.readthedocs.io/en/latest/)~          | ~[uWSGI](https://pypi.org/project/uWSGI/)~             | ~[unbit/uwsgi](https://github.com/unbit/uwsgi)~                           | ~`2.0.19.1`~                                                           | ~`-`~                                                |
| [Gunicorn](https://gunicorn.org/)                                | [gunicorn](https://pypi.org/project/gunicorn/)         | [benoitc/gunicorn](https://github.com/benoitc/gunicorn)                   | `20.0.4`                                                               | `-`                                                  |
| [nose](https://nose.readthedocs.io/en/latest/)                   | [nose](https://pypi.org/project/nose/)                 | [nose-devs/nose](https://github.com/nose-devs/nose)                       | `1.3.7`                                                                | `-`                                                  |
| [Sphinx](https://www.sphinx-doc.org/en/main/)                    | [Sphinx](https://pypi.org/project/Sphinx/)             | [sphinx-doc/sphinx](https://github.com/sphinx-doc/sphinx)                 | `3.5.0`                                                                | `-`                                                  |
| [Codecov](https://codecov.io/)                                   | [codecov](https://pypi.org/project/codecov/)           | [codecov/codecov-python](https://github.com/codecov/codecov-python)       | `2.1.11`                                                               | `-`                                                  |
| [LINE Developers](https://developers.line.biz/ja/)               | [line-bot-sdk](https://pypi.org/project/line-bot-sdk/) | [line/line-bot-sdk-python](https://github.com/line/line-bot-sdk-python)   | `1.18.0`                                                               | `LINE_CHANNEL_ACCESS_TOKEN`<br>`LINE_CHANNEL_SECRET` |
| [Flask](https://flask.palletsprojects.com/en/1.1.x/)             | [Flask](https://pypi.org/project/Flask/)               | [pallets/flask](https://github.com/pallets/flask)                         | `1.1.2`                                                                | `-`                                                  |
| [A3RT/TalkAPI](https://a3rt.recruit-tech.co.jp/product/talkAPI/) | [pya3rt](https://pypi.org/project/pya3rt/)             | [nocotan/pya3rt](https://github.com/nocotan/pya3rt)                       | `1.1`                                                                  | `A3RT_TALKAPI_APIKEY`                                |
| [TMDb](https://www.themoviedb.org/?language=ja)                  | ~[tmdbv3api](https://pypi.org/project/tmdbv3api/)~     | ~[AnthonyBloomer/tmdbv3api](https://github.com/AnthonyBloomer/tmdbv3api)~ | ~`1.6.2`~                                                              | ~`TMDB_API_KEY`~                                     |
| [YouTube](https://www.youtube.com/?gl=JP)                        | -                                                      | -                                                                         | `-`                                                                    | `-`                                                  |
| [Filmarks](https://filmarks.com/)                                | -                                                      | -                                                                         | `-`                                                                    | `-`                                                  |
| [Metacritic](https://www.metacritic.com/game)                    | -                                                      | -                                                                         | `-`                                                                    | `-`                                                  |
| [Google](https://www.google.com/)                                | -                                                      | -                                                                         | `-`                                                                    | `-`                                                  |

### GitHub

| Homepage                                                           | This Repository                                                                                         |
| :---                                                               | :---                                                                                                    |
| [GitHub](https://github.com/)                                      | [Code](https://github.com/ghsable/aimay)                                                                |
| [GitHub Issues](https://guides.github.com/features/issues/)        | [Issues](https://github.com/ghsable/aimay/issues)<br>[ISSUE_TEMPLATE](https://github.com/ghsable/aimay/tree/main/.github/ISSUE_TEMPLATE)<br>[CONTRIBUTING.md](https://github.com/ghsable/aimay/blob/main/.github/CONTRIBUTING.md)<br>[SUPPORT.md](https://github.com/ghsable/aimay/blob/main/.github/SUPPORT.md) |
| [GitHub Pull requests](https://github.com/features/code-review/)   | [Pull requests](https://github.com/ghsable/aimay/pulls)<br>[CODEOWNERS](https://github.com/ghsable/aimay/blob/main/.github/CODEOWNERS)<br>[pull_request_template.md](https://github.com/ghsable/aimay/blob/main/.github/pull_request_template.md) |
| [GitHub Actions](https://github.com/features/actions/)             | [Actions](https://github.com/ghsable/aimay/actions)<br>[workflows](https://github.com/ghsable/aimay/tree/main/.github/workflows) |
| [GitHub Projects](https://github.com/features/project-management/) | [Projects](https://github.com/ghsable/aimay/projects)                                                   |
| [GitHub Wiki](https://guides.github.com/features/wikis/)           | [Wiki](https://github.com/ghsable/aimay/wiki)                                                           |
| [GitHub Security](https://github.com/features/security)            | [Security](https://github.com/ghsable/aimay/security)<br>[CODE_OF_CONDUCT.md](https://github.com/ghsable/aimay/blob/main/.github/CODE_OF_CONDUCT.md)<br>[SECURITY.md](https://github.com/ghsable/aimay/blob/main/.github/SECURITY.md)             |
| [GitHub Insights](https://github.com/features/insights)            | [Insights](https://github.com/ghsable/aimay/pulse)                                                      |
| [GitHub Pages](https://pages.github.com/)                          | [aimay](https://ghsable.github.io/aimay/)                                                               |
| [GitHub Sponsors](https://github.com/sponsors)                     | [FUNDING.yml](https://github.com/ghsable/aimay/blob/main/.github/FUNDING.yml)                           |
| [GitHub CodeQL](https://securitylab.github.com/tools/codeql)       | [codeql-analysis.yml](https://github.com/ghsable/aimay/blob/main/.github/workflows/codeql-analysis.yml) |

### actions

| Marketplace/Actions                                                                         | [Version](https://github.com/ghsable/aimay/blob/main/.github/workflows/main.yml) | Environment variable(GitHub)                            |
| :---                                                                                        | :---                                                                             | :---                                                    |
| [Checkout](https://github.com/marketplace/actions/checkout)                                 | `2.x.x`                                                                          | `-`                                                     |
| -                                                                                           | `-`                                                                              | `A3RT_TALKAPI_APIKEY`                                   |
| [Codecov](https://github.com/marketplace/actions/codecov)                                   | `1.x.x`                                                                          | `CODECOV_TOKEN`                                         |
| [Codacy Coverage Reporter](https://github.com/marketplace/actions/codacy-coverage-reporter) | `0.2.0`                                                                          | `CODACY_PROJECT_TOKEN`                                  |
| [GitHub Pages action](https://github.com/marketplace/actions/github-pages-action)           | `3.x.x`                                                                          | `GITHUB_TOKEN`                                          |
| [Deploy to Heroku](https://github.com/marketplace/actions/deploy-to-heroku)                 | `3.6.8`                                                                          | `HEROKU_API_KEY`<br>`HEROKU_APP_NAME`<br>`HEROKU_EMAIL` |

### badges

| Homepage                                | Application                                                   | This Repository                                                                                                                                            |
| :---                                    | :---                                                          | :---                                                                                                                                                       |
| [Codecov](https://codecov.io/)          | [marketplace/codecov](https://github.com/marketplace/codecov) | [aimay](https://codecov.io/gh/ghsable/aimay)                                                                                                               |
| [Codacy](https://www.codacy.com/)       | -                                                             | [aimay](https://app.codacy.com/manual/ghsable/aimay?utm_source=github.com&utm_medium=referral&utm_content=ghsable/aimay&utm_campaign=Badge_Grade_Settings) |
| [CodeFactor](https://www.codefactor.io) | -                                                             | [aimay](https://www.codefactor.io/repository/github/ghsable/aimay)                                                                                         |
| [Code Climate](https://codeclimate.com) | -                                                             | [aimay](https://codeclimate.com/github/ghsable/aimay/maintainability)                                                                                      |
| [Gitter](https://gitter.im/)            | -                                                             | [aimay](https://gitter.im/ghsable/aimay)                                                                                                                   |
| [Shields.io](https://shields.io/)       | -                                                             | -                                                                                                                                                          |
| [FOSSA](https://fossa.com/)             | [fossabot](https://github.com/fossabot)                       | [aimay](https://app.fossa.com/projects/git%2Bgithub.com%2Fghsable%2Faimay?ref=badge_large)                                                                 |

### others

| Homepage                                                            | GitHub                                                                                                                   | This Repository                                                                                                                      |
| :---                                                                | :---                                                                                                                     | :---                                                                                                                                 |
| [Docker](https://www.docker.com/)                                   | [docker/docker-ce](https://github.com/docker/docker-ce)                                                                  | [Dockerfile](https://github.com/ghsable/aimay/blob/main/Dockerfile)                                                                  |
| [Theia](https://theia-ide.org/) on [Gitpod](https://www.gitpod.io/) | [eclipse-theia/theia](https://github.com/eclipse-theia/theia)<br>[gitpod-io/gitpod](https://github.com/gitpod-io/gitpod) | [.theia](https://github.com/ghsable/aimay/blob/main/.theia)<br>[.gitpod.yml](https://github.com/ghsable/aimay/blob/main/.gitpod.yml) |
| [GitHub Learning Lab](https://lab.github.com/)                      | [github/learning-lab-components](https://github.com/github/learning-lab-components)                                      | [ghsable/github-slideshow](https://github.com/ghsable/github-slideshow)                                                              |
| [ZenHub](https://www.zenhub.com/)                                   | [ZenHub](https://github.com/ZenHubIO)                                                                                    | -                                                                                                                                    |
| [Zube](https://zube.io/)                                            | [zube](https://github.com/zubeio)                                                                                        | -                                                                                                                                    |
| [Dependabot](https://dependabot.com/)                               | [Dependabot Preview](https://github.com/marketplace/dependabot-preview)                                                  | [dependabot.yml](https://github.com/ghsable/aimay/blob/main/.github/dependabot.yml)                                                  |
| [Stale](https://probot.github.io/apps/stale/)                       | [probot/stale](https://github.com/probot/stale)                                                                          | [stale.yml](https://github.com/ghsable/aimay/blob/main/.github/stale.yml)                                                            |
| [gitignore.io](https://www.toptal.com/developers/gitignore)         | [toptal/gitignore.io](https://github.com/toptal/gitignore.io)                                                            | [.gitignore](https://github.com/ghsable/aimay/blob/main/.gitignore)                                                                  |
| [draw.io](https://app.diagrams.net)                                 | [jgraph/drawio](https://github.com/jgraph/drawio)                                                                        | [drawio](https://github.com/ghsable/aimay/tree/main/.readme/drawio)                                                                  |

## app.run

| Case  | WSGI                                                  | [commands](https://github.com/ghsable/aimay/blob/main/Procfile)                                                   | HOST:PORT         |
| :---  | :---                                                  | :---                                                                                                              | :---              |
| 1     | [Flask](https://flask.palletsprojects.com/en/1.1.x/)  | `python -m aimay`                                                                                                 | `0.0.0.0:${PORT}` |
| 2     | [uWSGI](https://uwsgi-docs.readthedocs.io/en/latest/) | `uwsgi --workers=$(($(grep -c processor /proc/cpuinfo)*2+1)) --http=0.0.0.0:${PORT} --mount /=aimay.__main__:app` | `0.0.0.0:${PORT}` |
| **3** | [Gunicorn](https://gunicorn.org/)                     | `gunicorn --workers $(($(grep -c processor /proc/cpuinfo)*2+1)) aimay.__main__:app`                               | `0.0.0.0:${PORT}` |

## Versioning

* [Semantic Versioning](https://semver.org/)
  * [Tags](https://github.com/ghsable/aimay/tags)
  * [Releases](https://github.com/ghsable/aimay/releases)
  * [Packages](https://github.com/ghsable/aimay/packages)

---

[BACK TO TOP](#readme)
