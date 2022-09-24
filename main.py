import discord
from discord.ext import commands
import music
from keep_alive import keep_alive
import os

cogs = [music]

client = commands.Bot(command_prefix='!', intents=discord.Intents.all())

for i in range(len(cogs)):
    cogs[i].setup(client)

keep_alive()
try:
    client.run(
        "OTkwNDM2ODA0NTMwNDEzNTk4.G50qYM.su59g2y641czS2hOA7pLgEOKoLL8Du1E3x5oW4"
    )
except:
    os.system("kill 1")
