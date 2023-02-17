import discord

class RPGClient(discord.Client):
    async def on_ready(self: discord.Client):
        guilds = [guild.name async for guild in self.fetch_guilds()]
        print(f"Finished logon, serving {guilds}")
    
    # async def on_message(self: discord.client, message: discord.Message):
    #     if message.author