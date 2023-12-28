import discord
from discord.ext import commands

from dotenv import load_dotenv
import os

from .socket import send_message



load_dotenv( )
intents = discord.Intents.default()
intents.members = True; intents.message_content = True

client = commands.Bot( command_prefix = commands.when_mentioned_or( "ao!" ), intents=intents )
channel = None



@client.hybrid_group( fallback = "canal" )
@commands.has_permissions( manage_messages = True )
async def ao( ctx ):
    global channel
    channel = ctx.channel.id


@client.listen( "on_message" )
async def msg_ao( message ):
    if message.channel.id == channel:
        send_message( message.content, message.author.display_name, message.author.id )



client.run( os.getenv( 'TOKEN' ) )
