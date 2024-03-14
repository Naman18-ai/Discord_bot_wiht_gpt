import discord
import os
#app id:1217738952853946408
#publc key:aced67ad996c10f85070766cedf035f12bd52198d748503cc6130427742a3ab9
from openai import OpenAI
openai_client = OpenAI(api_key="your_api key")

class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.chat_history = []
        
    async def on_ready(self):
        print(f'A wild {self.user} has appeared!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        
        if self.user!= message.author:
          self.chat_history.append(message.content)
          if self.user in message.mentions:
            channel =message.channel
            user_message=message.clean_content
            response = openai_client.chat.completions.create(
              model="gpt-3.5-turbo",
              messages=[
                {
                  "role": "user",
                  "content":"\n".join(self.chat_history) 
                    # user_message
                }
              ],
              temperature=1,
              max_tokens=256,
              top_p=1,
              frequency_penalty=0,
              presence_penalty=0
            )
            message_to_send = response.choices[0].message.content
            await channel.send(message_to_send)

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)        
client.run("your_client_secret")     