# Stable Diffusion Bot
日本語でプロンプトを与えるとStable Diffusionの画像を投稿してくれるSlack Bot

## 環境導入と実行
```
conda env create -f environment.yaml
conda activate sdbot
```
以上を行って `.env` ファイルにHuggingfaceのトークンと、SlackのAppトークンとBotトークンを設定。

```
YOUR_TOKEN=hf_xxxxxxxxxxxxxx
SLACK_BOT_TOKEN=xoxb-999999999999999999999999
SLACK_APP_TOKEN=xapp-999999999999999999999999
```

設定後、実行は以下のコマンドの通り。

```
python3 script/main.py
```
## Stable Diffusion Botの使い方

- 画像生成: !img [プロンプト]
- ヘルプ表示: !img-help

## Slackのアプリに必要な権限
アプリの作り方は[このドキュメント](https://slack.dev/bolt-python/ja-jp/tutorial/getting-started)に準拠。
必要権限は以下。

### OAuth & Permissions - Bot Token Scopes
- chat:write
- files:write

### Event Subscriptions
- message.channels
- message.groups
- message.im
- message.mpim 


## 参考ドキュメント
- [Stable Diffusion with 🧨 Diffusers](https://huggingface.co/blog/stable_diffusion)
- [image-2-image using diffusers](https://colab.research.google.com/github/patil-suraj/Notebooks/blob/master/image_2_image_using_diffusers.ipynb#scrollTo=V24njWQBC8eC)