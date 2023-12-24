from discord.ext import commands

class MyBot(commands.Bot):
    def __init__(self, args):
        super().__init__(args)

    def custom(self):
        print("hello")
