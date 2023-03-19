import discord
from discord.ext import commands

intents=discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix= '!',intents=discord.Intents.all())

@client.event
async def on_ready():
    print('目前登入身份：',client.user)
    game = discord.Game('喔龍江森')
    await client.change_presence(status=discord.Status.online, activity=game)
    print("Bot is online")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('說'):
      tmp = message.content.split(" ",2)
      if len(tmp) == 1:
        await message.channel.send("你要我說什麼啦？")
      else:
        await message.channel.send(tmp[1])
    if message.content.startswith('更改狀態'):
        tmp = message.content.split(" ",2)
        if len(tmp) == 1:
            await message.channel.send("你要改成什麼啦？")
        else:
            game = discord.Game(tmp[1])
            await client.change_presence(status=discord.Status.online, activity=game)

    if message.content.startswith('跟我打聲招呼吧'):
        channel = message.channel
        await channel.send('那你先跟我說你好')
        def checkmessage(m):
            return m.content == '你好' and m.channel == channel
        msg = await client.wait_for('message', check=checkmessage)
        await channel.send('嗨, {.author}!'.format(msg))

@client.command()
async def here(ctx):
    await ctx.send(F"{ctx.author}你好,你現在在{ctx.guild.name}的{ctx.channel.mention}")



client.run('MTA4Njk5MDUwMzg1OTQ3NDQzMg.GAw4Uu._1kn9FBHxEcS5z9yRwpxsSNoujCMQKqZ-H4cnU')