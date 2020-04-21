import configparser
import os


import discord
from discord.ext import commands
from src.MyModules import MyModules as myMod

class MyBot(commands.Cog):

    def __init__(self, bot):
        base = os.path.dirname(os.path.abspath(__file__))
        conf_path = os.path.normpath(os.path.join(base, '../config'))
        conf = configparser.ConfigParser()
        conf.read(conf_path+'/config.ini', encoding='utf-8')
        self.bot = bot
        self.bot_id = int(conf['DEFAULT']['BOT_ID'])
        self.icon_url = 'https://cdn.discordapp.com/avatars/{id}/{avatar}.png'

    @commands.command()
    async def hello(self, ctx):
        bot = self.bot.get_user(self.bot_id)
        icon = self.icon_url.format(
            id = str(self.bot_id),
            avatar = bot.avatar,
        )
        embed = discord.Embed(title='こんにちはクズだよ！！', color=0xff66cf)
        embed.set_author(name='夢見りあむ', icon_url=icon)
        await ctx.send(embed=embed)

    @commands.command(name='致した')
    async def masturbation(self, ctx, arg):
        mod = myMod()

        bot = self.bot.get_user(self.bot_id)
        usr_name = ctx.author.name
        guild_name = ctx.guild.name

        bot_icon = self.icon_url.format(
            id = str(self.bot_id),
            avatar = bot.avatar,
        )
        icon = self.icon_url.format(
            id = str(ctx.author.id),
            avatar = ctx.author.avatar,
        )

        embed_description = f"{usr_name}が'{arg}'でシコったのを確認したぞ！"
        embed = discord.Embed(title='致した', description=embed_description, color=0xff66cf)
        embed.set_author(name=usr_name, icon_url=icon)
        embed.set_thumbnail(url=bot_icon)
        embed.set_footer(text=f'location: {guild_name}')

        mod.seve_masturbation_log(usr_name, arg, guild_name)
        await ctx.send(embed=embed)

    @commands.command(name='サーバー別致し件数')
    async def masturbation_count_list_by_servers(self, ctx):
        mod = myMod()
        bot = self.bot.get_user(self.bot_id)
        icon = self.icon_url.format(
            id = str(self.bot_id),
            avatar = bot.avatar,
        )
        embed_description = '>>> '
        list_by_guild = mod.get_count_list_by_guild()
        for row in list_by_guild:
            embed_description += f"{row['guild']}: {row['count']}\n"

        embed = discord.Embed(title='オタク別致し件数', description=embed_description, color=0xff66cf)
        embed.set_author(name='夢見りあむ', icon_url=icon)
        await ctx.send(embed=embed)

    @commands.command(name='オタク別致し件数')
    async def masturbation_count_list_by_users(self, ctx):
        mod = myMod()
        bot = self.bot.get_user(self.bot_id)
        icon = self.icon_url.format(
            id = str(self.bot_id),
            avatar = bot.avatar,
        )
        embed_description = '>>> '
        list_by_guild = mod.get_count_list_by_user()
        for row in list_by_guild:
            embed_description += f"{row['user']}: {row['count']}\n"

        embed = discord.Embed(title='サーバー別致し件数', description=embed_description, color=0xff66cf)
        embed.set_author(name='夢見りあむ', icon_url=icon)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(MyBot(bot))
