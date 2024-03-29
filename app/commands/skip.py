from discord.ext import commands
from discord.ext.commands import Bot

from app.core.player import mp, play_song


class Skip(commands.Cog):
    def __init__(self, client: Bot):
        self.client = client

    @commands.command(help="Skips the currently playing song.")
    async def skip(self, ctx: commands.Context) -> commands.Context:
        queue = mp.return_queue(ctx.guild.id)
        voice_client = ctx.guild.voice_client
        if voice_client:
            if voice_client.is_playing() and not queue:
                voice_client.stop()
                await ctx.channel.send("Stopped playing the current song.")
            elif queue:
                voice_client.stop()
                next_song = queue[0]
                play_song(guild_id=ctx.guild.id, voice=voice_client)
                await ctx.channel.send(f"Now playing {next_song.name}")
            else:
                await ctx.channel.send("There is nothing to skip!")
        else:
            await ctx.channel.send("I am not connected to any voice channels.")


async def setup(client: Bot) -> None:
    await client.add_cog(Skip(client))
