
# IMPORT DISCORD.PY. ALLOWS ACCESS TO DISCORD'S API.
import math
import random

import discord
# from discord.ext import commands

# IMPORT THE OS MODULE.
import os

# IMPORT LOAD_DOTENV FUNCTION FROM DOTENV MODULE.
from dotenv import load_dotenv

# LOADS THE .ENV FILE THAT RESIDES ON THE SAME LEVEL AS THE SCRIPT.
load_dotenv()

# client = commands.Bot(command_prefix="!")


# GRAB THE API TOKEN FROM THE .ENV FILE.
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# GETS THE CLIENT OBJECT FROM DISCORD.PY. CLIENT IS SYNONYMOUS WITH BOT.
bot = discord.Client()

# print("\n\n\n\nThis is my discord token : " + DISCORD_TOKEN + "\n\n\n\n\n")

prefix = "!"
# EVENT LISTENER FOR WHEN THE BOT HAS SWITCHED FROM OFFLINE TO ONLINE.
@bot.event
async def on_ready():
    # CREATES A COUNTER TO KEEP TRACK OF HOW MANY GUILDS / SERVERS THE BOT IS CONNECTED TO.
    guild_count = 0

    # LOOPS THROUGH ALL THE GUILD / SERVERS THAT THE BOT IS ASSOCIATED WITH.
    for guild in bot.guilds:
        # PRINT THE SERVER'S ID AND NAME.
        print(f"- {guild.id} (name: {guild.name})")

        # INCREMENTS THE GUILD COUNTER.
        guild_count = guild_count + 1

    # PRINTS HOW MANY GUILDS / SERVERS THE BOT IS IN.
    print("SampleDiscordBot is in " + str(guild_count) + " guilds.")

# global userclear

# EVENT LISTENER FOR WHEN A NEW MESSAGE IS SENT TO A CHANNEL.
@bot.event
async def on_message(message):
    # CHECKS IF THE MESSAGE THAT WAS SENT IS EQUAL TO "HELLO".
    if message.author == bot.user:
        return
    if message.content == prefix + "mafs":
        x = math.e + random.randint(0,1000)
        await message.channel.send(x)
    if "amlo" in message.content:
        await message.delete()
        await message.channel.send("No se puede decir el nombre del presi eh por favor {} ".format(message.author.name))
    if message.content == prefix + ('whoami'):
        await message.channel.send('You are {}'.format(message.author.name))
    if message.content == prefix + ('help'):
        await message.channel.send("**HELP**\n\n"
                                   "**!whoami** - bot replies with your username\n\n"
                                   "**!mafs** - bot sends a random number between 0-1000; will upgrade later to be used for"
                                   "calculations using the *Wolfram-Alpha* API. This includes derivatives, integrations,"
                                   "linear"
                                   "system solutions, etc.\n\n"
                                   "Anytime you mention the name of the mexican president the message will be "
                                   "deleted and you will be called out by the bot.\n\n"
                                   "Anytime the word/phrase **\'siu\'** is detected in a sentence, the bot will send a gif"
                                   "of the author of said phrase\n\n"
                                   "**!clear <number>** - will clear the last <number> amount of messages sent by whomever"
                                   "uses the command. Example of usage: \'**!clear 40**\' clears the last 40 messages. "
                                   "If no number is included in command, the default amount of messages will be "
                                   "deleted which is 30.")
    if message.content.startswith('siu'):
        await message.channel.send("https://giphy.com/gifs/zcVOyJBHYZvX2")
    if message.content.startswith(prefix+'clear'):
        amclear = int(splitclear(message.content))
        # print("hello " + userclear)
        # userclear = message.author.name
        await clear(message.channel, amclear)


def splitclear(mssg):
    usclear = mssg.split("!clear ", 1)
    if len(usclear) > 1:
        return usclear[1]
    return 30


# @client.command(name='clear', help='this command will clear msgs')
async def clear(ctx, amount):
    userclear = (await ctx.history(limit=1).flatten())[0].author.name
    count = 0
    await ctx.send("Deleting {} messages sent by {}".format(amount, userclear))
    async for mssg in ctx.history(limit=None):

        if mssg.author.name == userclear and amount >= count:
            count+=1
            await mssg.delete()


# client.run(DISCORD_TOKEN)

# EXECUTES THE BOT WITH THE SPECIFIED TOKEN. TOKEN HAS BEEN REMOVED AND USED JUST AS AN EXAMPLE.
bot.run(DISCORD_TOKEN)
