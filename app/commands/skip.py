from app.main import client
from app.api.player import play_song


@client.command(name="skip")
async def skip(ctx):
    queue = client.get_queue(ctx.guild.id)
    voice_client = ctx.guild.voice_client
    if voice_client.is_playing() and not len(queue):
        voice_client.stop()
        await ctx.channel.send("Stopped playing the current song.")
    elif queue:
        voice_client.stop()
        next_song = queue[0]
        play_song(guild_id=ctx.guild.id, voice=voice_client, song_url=next_song.url)
        await ctx.channel.send("Now playing {}".format(next_song.name))
    else:
        await ctx.channel.send("There is nothing to skip!")


async def setup(bot):
    bot.add_command(skip)
