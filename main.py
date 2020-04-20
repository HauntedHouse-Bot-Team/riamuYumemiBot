import os
import configparser

from discord.ext import commands

INITIAL_EXTENSIONS = [
    'cog.MyCog',
]

class MyBot(commands.Bot):
    def __init__(self, command_prefix):
        super().__init__(command_prefix)
        for cog in INITIAL_EXTENSIONS:
            try:
                self.load_extension(cog)
            except Exception:
                traceback.print_exc()

    async def on_ready(self):
        print('---start---')

def main():
    base = os.path.dirname(os.path.abspath(__file__))
    conf_path = os.path.normpath(os.path.join(base))
    conf = configparser.ConfigParser()
    conf.read(conf_path+'/config/config.ini', encoding='utf-8')

    bot = MyBot(command_prefix='$')
    bot.run(conf['DEFAULT']['BOT_TOKEN'])

if __name__ == '__main__':
    main()
