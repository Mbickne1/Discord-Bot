#Imports
import os
import discord
from dotenv import load_dotenv
#Load Enviornment Variables
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
#Create Intents
#May need to change to less/more intents letter on need
intents = discord.Intents.default()
intents.members = True