from dotenv import load_dotenv
from slack_bolt.adapter.socket_mode import SocketModeHandler
from slack_bolt import App
from slack_sdk import WebClient
import os

DEBUG=False

load_dotenv()
SLACK_BOT_TOKEN = os.environ['SLACK_BOT_TOKEN']
SLACK_APP_TOKEN = os.environ['SLACK_APP_TOKEN']
MY_USER_ID = os.environ['SLACK_USER_ID']
SOUNDS = os.environ['SLACK_SOUNDS_PATH']
PLAYER = os.environ['SLACK_SOUND_PLAYER']

app = App(token=SLACK_BOT_TOKEN)
channels_by_id = {}

def mentioned(text):
    #<!here>
    #<!channel>
    #<@{USERID}>
    if '<!here>' in text:
        return True
    if '<!channel>' in text:
        return True
    if ('<@' + MY_USER_ID + '>') in text:
        return True
    return False

@app.event("message")
def message(logger, event):
    #skip messages by us
    if 'user' in event and event['user'] == MY_USER_ID and not DEBUG:
        return

    #warn when we don't know about a channel
    if event['channel'] not in channels_by_id:
        print("no sound for", channels_by_id[event['channel']])
        return

    channel = channels_by_id[event['channel']]
    wav = channel+'.wav'
    path = os.path.join(SOUNDS, 'mentions', wav)
    path2 = os.path.join(SOUNDS, wav)

    if 'text' not in event:
        print("no text element in", channel)
        return

    # if we were mentioned and have a mention sound, play it
    if mentioned(event['text']) and os.path.exists(path):
        print("playing mention sound for", channel)
        os.system(PLAYER + " " + path + " 2> /dev/null")

    # if we have a sound for every message (not from us), play it
    elif os.path.exists(path2):
        print("playing channel sound for", channel)
        os.system(PLAYER + " " + path2 + " 2> /dev/null")

    elif DEBUG:
        print("no sound to play for", channel)


if __name__ == "__main__":
    if DEBUG:
        print("Running in DEBUG mode")

    #gather channels
    client = WebClient(token=SLACK_BOT_TOKEN)
    response = client.conversations_list(types="public_channel, private_channel")
    if response['ok'] != True:
        print("failed to get channels")
        exit(1)

    for ch in response['channels']:
        channels_by_id[ch['id']] = ch['name']

    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    handler.start()
