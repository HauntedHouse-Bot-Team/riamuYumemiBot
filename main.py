import os
from dotenv import load_dotenv

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
    base_path = os.path.dirname(os.path.abspath(__file__))
    dotenv_path = os.path.join(base_path, '.env')
    load_dotenv(dotenv_path)

    bot = MyBot(command_prefix='$')
    bot.run(os.getenv('BOT_TOKEN'))

if __name__ == '__main__':
    main()
