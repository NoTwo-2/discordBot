import discord
import client
import config

# allow specific intents
intents = discord.Intents.default()
intents.message_content = True

client = client.RPGClient(intents= intents)

client.run(config.token)