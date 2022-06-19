import discord
import utils
from discord.ext import commands

def start():

    bot = commands.Bot(command_prefix='/', intents=utils.intents)

    @bot.event
    async def on_ready():
        print(f'{bot.user.name} has connected to Discord!')

    @bot.command(name="chat")
    async def chat_bot(ctx):
        
        @bot.event
        async def on_message(message):
            if message.author == bot.user.name:
                return

            if "Hello Bot" in message.content.lower():
                res = "Hello Human!"
                await message.channel.send(res)

    

    bot.run(utils.TOKEN)