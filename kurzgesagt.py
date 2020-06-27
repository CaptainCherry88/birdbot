import time
import os
import logging
import discord
from discord.ext import commands
logging.basicConfig(level=logging.INFO)

print("Delaying bot for server creation")
time.sleep(5)
class Bot(commands.AutoShardedBot):
    """Main Bot"""

    def __init__(self):
        bot = commands.Bot(command_prefix='k!',owner_ids={389718094270038018,183092910495891467,424843380342784011})
        super().__init__(command_prefix="k!",case_insensitive=True)
        self.starttime = time.time()
        self.logger = logging.getLogger('worker')
        cogs = []
        fails = {}
        for i in cogs:
            try:
                super().load_extension(i)
                logger.info(f'Loading {i}')
            except Exception as e:
                logger.exception('Exception at {i}')
                fails[i] = e

        async def on_ready(self):
            logger.info('Logged in as')
            logger.info(f"\tUser: {bot.user.name}")
            logger.info(f"\tID  : {bot.user.id}")
            logger.info('------')
            #bot status
            activity = discord.Activity(type=discord.ActivityType.listening, name="to Steve's voice" )
            await bot.change_presence(activity = activity)


with open('token.txt') as tokenfile:
    token = tokenfile.read()
Bot().run(token)
