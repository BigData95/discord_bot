import discord
from dotenv import load_dotenv
import os
from discord.ext import commands
load_dotenv()


class MyClient(discord.Client):
    description = '''Simple bot '''
    intents = discord.Intents.default()
    intents.members = True
    bot = commands.Bot(command_prefix='$',
                       description=description, intents=intents)

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))


    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        # await message.channel.send("Funciona")

    @bot.command()
    async def test(ctx, arg1, arg2):
        await ctx.send('You passed {} and {}'.format(arg1, arg2))

    @bot.command()
    async def add(ctx, a: int, b: int):
        await ctx.send(a + b)



client = MyClient()
client.run(os.getenv('TOKEN'))
