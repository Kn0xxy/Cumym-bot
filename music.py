import discord
from discord.ext import commands
import youtube_dl


class music(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def disconnect(self, ctx):
        await ctx.voice_client.disconnect()

    @commands.command()
    async def play(self, ctx, url):
        if ctx.author.voice is None:
            await ctx.send("You're not in a voice channel dumbass")
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await voice_channel.connect()
        else:
            await ctx.voice_client.move_to(voice_channel)

        FFMPEG_OPTIONS = {'before_options': '-reconnect 1', 'options': '-vn'}
        YDL_OPTIONS = {'format': "bestaudio"}
        vc = ctx.voice_client

        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info['formats'][0]['url']
            source = await discord.FFmpegOpusAudio.from_probe(
                url2, **FFMPEG_OPTIONS)
            vc.play(source)

    @commands.command()
    async def pause(self, ctx):
        await ctx.send("DONT PAUSE <:Angry:537178740912816137>")
        await ctx.voice_client.pause()

    @commands.command()
    async def stop(self, ctx):
        await ctx.send("this shit fucking sucks lmao")
        await ctx.voice_client.stop()

    @commands.command()
    async def resume(self, ctx):
        await ctx.send("<:linussextips:969924876024569886>")
        await ctx.voice_client.resume()


def setup(client):
    client.add_cog(music(client))
