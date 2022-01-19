Slack Sounds
--

Python Slack Bot to play unique sounds for each channel.

# Setup

## Install required packages

Python 3 is required.  It is also recommended to consider using a virtualenv.

```
pip install -r requirements.txt
```

## Register your bot with Slack

1. https://api.slack.com/apps
1. Click **Create New App**
1. Give you app a name, ie: 'slack-sounds'
1. Click **Create** and copy the app level token, later used as **SLACK_APP_TOKEN**
1. Navigate to the **OAuth & Permissions** tab under **Features** on the left panel.
1. Scroll down to **Bot Token Scopes** and add
   * channels:history
   * channels:read
   * groups:history
   * groups:read
1. Navigate to the **Socket Mode** tab under **Settings** in the left panel.
1. Enable the Socket Mode
1. Navigate to **Event Subscriptions** under **Features** in the left panel. 
1. Enable Events.
1. Scroll down to **Subscribe to Bot Events** and add
   * channel_history_changed
   * message.groups
1. Navigate to **Install App** under Settings, click **Install to Workspace**
1. Copy the **Bot User OAuth Token** later used as **SLACK_BOT_TOKEN**

## Setup the environment variables

Create a .env file in the root folder of this project with the following content:
```
SLACK_USER_ID={your slack user id}
SLACK_APP_TOKEN=xapp-{from above step}
SLACK_BOT_TOKEN=xorb-{from above step}
SLACK_SOUNDS_PATH={path to where you are going to store wav files}
SLACK_SOUND_PLAYER={command line friendly sound player}
```

Here's an example for use in linux:
```
SLACK_USER_ID=UXXXXXX
SLACK_APP_TOKEN=xapp-XXXXXX
SLACK_BOT_TOKEN=xorb-XXXXXX
SLACK_SOUNDS_PATH=/home/tim/dev/slack-sounds/sounds
SLACK_SOUND_PLAYER="cvlc --play-and-exit"
```

# Configuring sounds

The `SLACK_SOUNDS_PATH` should have .wav files named per channel.  If you want the channel `#notifications` to add a `notifications.wav` file to your `SLACK_SOUNDS_PATH`.  

If you want to play a sound only if you are mentioned (@here and @channel also), then put your sound in `SLACK_SOUNDS_PATH/mentions/notifications.wav`.

Channels that do not have a mention wav file nor a channel wav file, will not play a sound.

NOTE: You should probably turn off notification sounds on Slack.


# Run the application

```
python app.py
```

# Add your app to channels
You need to invite your app to each channel you want to play a sound for.

1. At the top of the channel, click the drop down on the channel name.
1. Navigate to the **Integrations** tab
1. In the **Apps** section click **Add App**
1. Find your app and add it

# Reference Material
* https://www.twilio.com/blog/how-to-build-a-slackbot-in-socket-mode-with-python

# License
MIT License
