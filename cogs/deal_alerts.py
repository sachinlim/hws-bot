from discord.ext import commands
from discord.utils import get
import docs


class Deals(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        channel = self.bot.get_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)

        # if a message is a link, people can react to it and others can be alerted of it if it's a good deal
        if message.content.startswith(docs.deal_requirement1) or message.content.startswith(docs.deal_requirement2):
            if payload.channel_id == docs.deals_channel_id:
                if payload.emoji.name == "🔥":
                    reaction = get(message.reactions, emoji=payload.emoji.name)

                    if reaction and reaction.count == docs.deals_required_reaction_count:
                        await message.channel.send(f'Hot deal for <@&{docs.deals_role_id}> members!',
                                                   reference=message)


async def setup(bot):
    await bot.add_cog(Deals(bot))
