import numpy as np
import cv2 as cv
from PIL import ImageGrab
import os
import discord
from ScreenCap import get_ss_obj
from key import party_token



#sftp://


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"{client.user} Logged in now!")


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('!capture'):
        
        ss = get_ss_obj()
        await message.channel.send(file=ss)

# my_secret = os.environ['TOKEN']
bot_token = party_token
client.run(bot_token)



    
