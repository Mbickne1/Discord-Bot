import discord
import utils

def run():
    client = discord.Client(intents=utils.intents)

    @client.event
    async def on_ready():
        guild = discord.utils.get(client.guilds, name=utils.GUILD)
        print(f'{client.user} has connected to Discord in the following guild:\n'
            f'{guild.name}(id: {guild.id})')
    
    client.run(utils.TOKEN)

