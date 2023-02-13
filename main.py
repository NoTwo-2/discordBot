import discord
import config

# allow specific intents
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents= intents)

@client.event
async def on_ready():
    guilds = [guild.name async for guild in client.fetch_guilds()]
    print(f"Finished logon, serving {guilds}")


client.run(config.token)