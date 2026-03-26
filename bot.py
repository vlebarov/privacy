from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ban')
    @commands.has_permissions(administrator=True)
    async def ban(self, ctx, member: commands.MemberConverter, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'{member.mention} has been banned for {reason}')

    @commands.command(name='mute')
    @commands.has_permissions(administrator=True)
    async def mute(self, ctx, member: commands.MemberConverter, *, reason=None):
        # Add mute logic here (e.g., using roles)
        await ctx.send(f'{member.mention} has been muted for {reason}')

def setup(bot):
    bot.add_cog(Moderation(bot))