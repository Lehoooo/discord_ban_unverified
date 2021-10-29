import discord
from discord import member
from discord.ext import commands

TOKEN = "PUT YOUR TOKEN HERE"

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(intents=intents, command_prefix='>')

@bot.event
async def on_ready():
    print("Logged in as: " + bot.user.name + "#" + bot.user.discriminator)
    print("Ready")

@bot.command()
async def ban_unverified(ctx):
    for member in ctx.guild.members:
        for role in member.roles:
            if role.name != "Verified":
                print(f"Banning {str(member.id) + str(member)}")
                try:
                    await member.ban()
                except Exception as e:
                    print("Error Banning")

bot.run(str(TOKEN))
