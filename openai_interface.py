import os
import time
from openai import OpenAI

client = OpenAI()


from pubsub import Pubsub

ps = Pubsub()

from openai import OpenAI
client = OpenAI()


instructions = """
"You are an intelligent, thoughtful assistant.

Normally, you are a conversationalist, providing kind, intelligent, brief answers at the utmost expert, at the advanced professor level.

You also have a few additional functions:

- REPEAT: If I ever ask you to 'playback' or 'repeat what I said', I want you to insert the text phrase '(play::repeat)' verbatim into our text, including parentheses and double colon",

- COLOR: If it seems like I want you to control the lights, then act like a color expert.
You are an expert at colors and color theory and lighting design.
You are controlling philips hue lamps. There are 6 lamps, with IDs [1, 2, 3, 6, 7, 8]. I will give you a phrase or a statement (for example: "a beach at sunset", "a campfire", "a neon dance party"); your goal is to translate that into a series of colors and brightnesses. Specifically, for each lamp, the result should look like:
[{
    "lampid": 1,
    "xy": [0.1, 0.5],
    "on": true,
    "bri": 200
},
...
]
Each light should be a different color. XY is a color in CIE color space. The first entry is the x coordinate and the second entry is the y coordinate. If you're acting like a color expoert, then in this case, follow these IMPORTANT instructions: respond with JSON only and NO OTHER TEXT OR EXPLANATION. The output should look like "{
    "mode": "hue::",
    "1": {"xy": [0.675, 0.322], "on": true, "bri": 200},
    "2": {"xy": [0.367, 0.358], "on": true, "bri": 200},
    "3": {"xy": [0.190, 0.099], "on": true, "bri": 200},
    "6": {"xy": [0.453, 0.454], "on": true, "bri": 200},
    "7": {"xy": [0.555, 0.297], "on": true, "bri": 200},
    "8": {"xy": [0.408, 0.517], "on": true, "bri": 200}
}", but with different "xy", "on", and "bri" values.'

"""



assistant = client.beta.assistants.create(
  name="Conversationalist",
  description="An intelligent, thoughtful conversationalist.",
  instructions=instructions,
  model="gpt-4-1106-preview",
  tools=[],
  file_ids=[]
)

thread = client.beta.threads.create()



def chat_to_assistant(msg):

    thread_message = client.beta.threads.messages.create(
      thread_id=thread.id,
      role="user",
      content=msg,
    )

    run = client.beta.threads.runs.create(
      thread_id=thread.id,
      assistant_id=assistant.id
    )

    while run.status != 'completed':
        run = client.beta.threads.runs.retrieve(
          thread_id=thread.id,
          run_id=run.id
        )
        print(run.status)
        time.sleep(1)

    thread_messages = client.beta.threads.messages.list(thread.id)

    most_recent_message = thread_messages.data[0]
    assert most_recent_message.content[0].type == "text"
    return most_recent_message.content[0].text.value

#chat_to_assistant("hello! can I ask you a question?")
#chat_to_assistant("how old are you?")
##################


from pathlib import Path

speech_file_path = Path(__file__).parent / "speech.mp3"
response = client.audio.speech.create(
  model="tts-1",
  voice="alloy",
  input="The quick brown fox jumped over the lazy dog."
)
response.stream_to_file(speech_file_path)



while True:
    message = ps.recv_string()
    print("received", message)
    
    if "transcribed::" in message:
        msg = message.split("transcribed::")[1]
        resp = chat_to_assistant(msg)
        ps.send_string("openai::" + resp)



