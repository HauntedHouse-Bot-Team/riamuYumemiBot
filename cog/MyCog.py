from discord.ext import commands
from src.MyModules import MyModules as myMod

class MyBot(commands.Cog):

    @commands.command()
    async def hello(self, ctx):
        await ctx.send(f'こんにちはクズだよ！！')

    @commands.command(name='致した')
    async def masturbation(self, ctx, arg):
        mod = myMod()
        usr = ctx.author.name
        guild = ctx.guild.name
        mod.seve_masturbation_log(usr, arg, guild)
        await ctx.send(f'{ctx.author.name}が{arg}でシコったのを確認したぞ！location: {guild}')

def setup(bot):
    bot.add_cog(MyBot(bot))
