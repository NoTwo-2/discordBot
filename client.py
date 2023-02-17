import discord
import constants



class RPGClient(discord.Client):
    


    def __init__(self, prefix: str, intents: discord.Intents):
        super().__init__(intents=intents)
        self.prefix: str = prefix


    # Custom Functions
    async def __resolve_command(message: discord.Message):
        command = message.content[1:]
        
        match command:
            case _:
                await message.channel.send("Unknown Command!")

    async def on_ready(self: discord.Client):
        guilds = [guild.name async for guild in self.fetch_guilds()]
        print(f"Finished logon, serving {guilds}")
    
    async def on_message(self: discord.Client, message: discord.Message):
        if message.author == self.user:
            return
        
        if message.content.startswith(constants.COMMAND_PREFIX):
            self.__resolve_command(message)