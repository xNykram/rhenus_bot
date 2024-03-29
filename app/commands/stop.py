from discord.ext import commands
from discord.ext.commands import Bot


class Stop(commands.Cog):
    def __init__(self, client: Bot):
        self.client = client

    @commands.command(help="Stops playing the current song and clears the queue.")
    async def stop(self, ctx):
        voice_client = ctx.guild.voice_client
        if voice_client.is_playing():
            voice_client.stop()
            await ctx.channel.send("Stopped playing the current song.")
        else:
            await ctx.channel.send("There are no more songs in the queue.")


async def setup(client: Bot) -> None:
    await client.add_cog(Stop(client))
