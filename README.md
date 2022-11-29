# Stable Diffusion Slack Bot

This is a slack bot to generate an image with Stable Diffusion using Japanese prompts and post it.
This app is proved to be operated under AWS EC2 instance g4dn.xlarge.

## How to install and run

Before you go, you need to prepare the environment to run [the certified version of Stable Diffusion v1-4](https://huggingface.co/CompVis/stable-diffusion-v1-4).

Run the following commands.

```
conda env create -f environment.yaml
conda activate sdbot
```

Then, set the HuggingFace token, Slack App Token, Slack Bot Token, and Slack Slash Command in the `.env` file.

```
YOUR_TOKEN=hf_xxxxxxxxxxxxxx
SLACK_BOT_TOKEN=xoxb-999999999999999999999999
SLACK_APP_TOKEN=xapp-999999999999999999999999
COMMAND=/sdbot
```

After you make the `.env` file, you can run it using the following command.

```
python3 scripts/main.py
```

## How to use

You can generate an image using the slash command you set in the `.env` file before and any prompt like this.

```
/sdbot a jumping cat in a garden
```

You can display help messages using the following slash command.

```
/sdbot help
```

## Configurations of the slack app

You can create your app acccording to [this document](https://slack.dev/bolt-python/ja-jp/tutorial/getting-started).
You need to set these configurations in the app.

### Socket Mode
- turn `Enable Socket Mode` on
- input `Token Name`
- copy `Token` and paste it to the `SLACK_APP_TOKEN` in the `.env` file.

### Slash Commands
- hit the `Create New Command` button
- input these settings
  - Command: the slash command you set in the `.env` file
  - Short Description: `Generate an image`
  - Usage Hint: `[prompt]`

### OAuth & Permissions - Bot Token Scopes
- grant these OAuth Scopes
  - chat:write
  - files:write
  - files:read

### OAuth & Permissions - OAuth Tokens for Your Workspace
- hit the `Install to Workspace` button
- copy `Bot User OAuth Token` and paste it to the `SLACK_BOT_TOKEN` in the `.env` file.

## Acknowledgments

This repository is forked from [sifue/stable-diffusion-bot](https://github.com/sifue/stable-diffusion-bot).
This version is modified to support slash commands and remove some features from the original repository.
