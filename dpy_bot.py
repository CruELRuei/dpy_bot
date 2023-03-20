import discord
from discord.ext import commands
import json
import random

with open('setting.json','r',encoding='utF8') as jfile:
    jdata = json.load(jfile)

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix= '!',intents=discord.Intents.all())

@client.event
async def on_ready():
    print('目前登入身份：',client.user)
    game = discord.Game('普羅多喵喵')
    await client.change_presence(status=discord.Status.online, activity=game)
    print("Bot is online")

@client.command()
async def on_voice_state_update(ctx):
   await ctx.send(F"{ctx.author}你好,你現在在{ctx.guild.name}的{ctx.channel.mention}")

@client.command()
async def here(ctx):
    await ctx.send(F"{ctx.author}你好,你現在在{ctx.guild.name}的{ctx.channel.mention}")

@client.command()
async def web(ctx):
    random_pic = random.choice(jdata['url_pic'])
    await ctx.send(random_pic)


client.run(jdata['TOKEN'])