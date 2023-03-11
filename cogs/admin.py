from discord.ext import commands


class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        """
        Error handler when the user does not pass along a search term with the command

        :param ctx: the message sent by the user
        :param error: error name
        :return: message to inform user to enter a search term
        """
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please enter the search term!')


async def setup(bot):
    await bot.add_cog(Admin(bot))
