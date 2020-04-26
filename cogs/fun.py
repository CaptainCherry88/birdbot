import discord
from discord.ext import commands

class Fun(commands.Cog, name='Fun'):
    def __init__(self, bot):
        self.bot = bot    
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('loaded fun')

    @commands.command()
    async def clap(self, ctx, *, clap):
        """Replaces spaces with :clap:"""
        claps = clap.replace(" ", " :clap: ")
        await get_channel(414452106129571842).send(claps)

def setup(bot):
    bot.add_cog(Fun(bot))