import discord
from discord.ext import tasks
import asyncio
import os

# token = ""
client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if f"<@!{client.user.id}>" in msg:
    await message.reply(f"Gladly! {msg[msg.index('<@!'):msg.index('>')+1]}, why don't ya get customize yourself at <#900989098054004736> by getting some roles and then you can have fun and interact with the people this server! Just keep in mind the rules to keep the experience fun for all :D")

client.run(os.environ['TOKEN'])
