import nextcord
from nextcord import Intents
from nextcord.ext import commands
import requests, json

token = json.load(open("config.json"))

intents = Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='', intents=intents)

@bot.command(name="atumalaca")
async def SendMessage(ctx):
    await ctx.send('HAHAHAHAHAHA HAHAHAHA ATUMALACA HAHAHAHA ATUMALACA HAHAHAHA EQUINOLE TICULACA TIC TA TIC TIC TIC TA HAHAHAHAHAH', files=[nextcord.File('atumalaca.mp4')])

@bot.event
async def on_ready():
    print(f"logged in as: {bot.user.name}")

if __name__ == '__main__':
    bot.run(token)
