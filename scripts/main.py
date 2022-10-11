from torch import autocast
from diffusers import StableDiffusionPipeline
import torch
import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from dotenv import load_dotenv
load_dotenv()


app = App(token=os.getenv("SLACK_BOT_TOKEN"))

MODEL_ID = "CompVis/stable-diffusion-v1-4"
WAIFU_MODEL_ID = "hakurei/waifu-diffusion"
DEVICE = "cuda"
YOUR_TOKEN = os.getenv("YOUR_TOKEN")
GENERATED_FILEPATH = "./results/generated.png"
INIT_FILEPATH = "./results/init.png"
WIDTH = 512
HEIGHT = 512
COMMAND = os.getenv("COMMAND")

using_user = None
pipe = None


@app.command(COMMAND)
def generate_image(ack, client, say, body):
    global using_user
    global pipe
    
    ack()
    prompt = body["text"]
    if prompt.startswith("help"):
        say(f"You can generate an image with this command, `{COMMAND} [prompt]` .\n" +
            "It takes about 1 minute to genrate an image. " +
            "While anyone else is generating an image, you can't generate it.\n" +
            "If you want to look for prompts, you can find them in https://lexica.art/ .")
        return
    
    try:
        if using_user is not None:
            say(f"Please try again after <@{using_user}> finishes genrating.")

        else:
            if pipe is None:
                say(f"Loading the text-to-image model now...")
                print('Model(T2I) loading start.')
                pipe = StableDiffusionPipeline.from_pretrained(
                    MODEL_ID, revision="fp16", torch_dtype=torch.float16, use_auth_token=YOUR_TOKEN)
                pipe.to(DEVICE)
                print('Model(T2I) loading finished.')

            using_user = body["user_name"]
            say(f"Generating an image using the prompt `{prompt}` posted by <@{using_user}>. Please wait about a minute.")

            with autocast(DEVICE):
                print(f'Generating start. ')
                image = pipe(prompt, guidance_scale=7.5,
                             height=HEIGHT,
                             width=WIDTH,
                             num_inference_steps=100)["sample"][0]

                os.makedirs('./results', exist_ok=True)
                image.save(GENERATED_FILEPATH)
                print(f'Generating finished.')

            client.files_upload_v2(
                channel=body['channel_id'],
                file=GENERATED_FILEPATH,
                title=prompt
            )

            say(f"Generated an image using the prompt `{prompt}` posted by <@{using_user}>.")
            using_user = None
    except Exception as e:
        using_user = None
        print(e)
        say(f"An error occured. Please try again. Error: {e}")


@app.event("message")
def handle_message_events(body, logger):
    logger.info(body)


# アプリを起動します
if __name__ == "__main__":
    SocketModeHandler(app, os.getenv('SLACK_APP_TOKEN')).start()
