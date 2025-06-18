import discord
import os 
from dotenv import load_dotenv
import pytubefix
from pytubefix import YouTube
from pytubefix import Search
from discord.ext import commands, tasks
import asyncio
import nacl
import re
import shutil
load_dotenv()
TOKEN = os.getenv("TOKEN")

intents = discord.Intents().all()
intents.message_content = True
intents.members =True
bot = commands.Bot(command_prefix = "!", intents = intents)

os.makedirs("downloads", exist_ok=True)
@bot.event
async def on_ready():
    try:
        print("Music Bot successfully connected!")
    except:
        print("[!] Couldn't connect, an Error occured")

# yt_dlp.utils.bug_reports_message = lambda: ''

ytdl_format_options = {
    "format": "bestaudio/best",
    "restrictfilenames": True,
    "noplaylist": True,
    "nocheckcertificate": True,
    "ignoreerrors": False,
    "logostderr": False,
    "quiet": True, 
    "no_warnings": True,
    "default_search": "auto",
    "source_address": "0.0.0.0",
    "outtmpl": "downloads/%(title).%(ext)s"
}

ffmpeg_options = {
    "before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5",
    "options": '-vn -filter:a "volume=0.15"'
}

# yt_dlp = pytubefix.YouTube(ytdl_format_options)

def give_link(name):
    search = Search(f"{name}")
    yt_id = search.results
    video_ids = [video.video_id for video in yt_id]

    video_id = video_ids[0] 
    base_url = f"https://www.youtube.com/watch?v={video_id}"
    return base_url

def delete_audio():
    path = "downloads"
    if os.path.exists(path):
        shutil.rmtree(path)
        print("Folder deleted")
    else:
        print("Folder not found.")

def remove_all_files(dir):
    for f in os.listdir(dir):
        os.remove(os.path.join(dir,f))




def is_valid_youtube_url(url):
    pattern = r"^(https?\:\/\/)?(www\.)?(youtube\.com\/watch\?v=|youtu\.be\/)[\w\-]{11}(&.*)?$"
    return re.match(pattern, url) is not None

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source,*, data, volume= 0.5):
        super().__init__(source,volume)
        self.data = data
        self.title = data.get("title")
        # self.url = ""
    
    @classmethod
    async def from_url(cls, url, *, loop= None, stream= False):
        loop = loop or asyncio.get_event_loop()

        def download_audio():
            yt = YouTube(url)
            audio_stream = yt.streams.filter(only_audio=True).first()
            out_file = audio_stream.download(output_path = "downloads")
            return out_file, {"title": yt.title}
        
        filename, data = await loop.run_in_executor(None, download_audio)
        return cls(discord.FFmpegPCMAudio(filename), data=data)
    
    # @bot.command(name = "play_song", help = "To play song")
    # async def play(ctx, url):
    #     if not ctx.message.author.name == "Md.Umair":
    #         await ctx.send("NOT AUTHORISED !")
    #         return 
    #     try:
    #         server = ctx.message.guild
    #         voice_channel = server.voice_client


@bot.command(name = "join", help = "Tells the bot to join the voice channel")
async def join(ctx):
    if not ctx.message.author.voice:
        await ctx.send("{} is not connected to a voice channel".format(ctx.message.author.name))
        return 
    else:
        channel = ctx.message.author.voice.channel
    await channel.connect()


# @bot.command(name = "play", help = "To play song")
# async def play(ctx, url):
#     # if not ctx.message.author.name == "Md.Umair":
#     #     await ctx.send("NOT AUTHORISED!")
#     #     return 

#     try:
#         server = ctx.message.guild
#         voice_channel = server.voice_client

#         async with ctx.typing():
#             filename = await YTDLSource.from_url(url, loop = bot.loop)
#             voice_channel.play(discord.FFmpegPCMAudio(executable="ffmpeg.exe", source = filename))
#         await ctx.send("**Now playing :** {}".format(filename))
#     except: 
#         await ctx.send("The bot is not connected to a voice channel.")

@bot.command(name="play", help="To play song")
async def play(ctx, name):
    url = give_link(name)
    if url is None:
        url = "https://www.youtube.com/watch?v=kPa7bsKwL-c"
    
    print(f"User input URL: {url}")

    if not is_valid_youtube_url(url):
        await ctx.send("❌ Please provide a valid YouTube video URL.")
        return 
    try:
        # Check if user is in a voice channel
        if ctx.author.voice is None:
            await ctx.send("❌ You must be in a voice channel to use this command.")
            return

        # Connect bot to voice channel if not already connected
        if ctx.voice_client is None:
            await ctx.author.voice.channel.connect()

        # Download and play audio
        async with ctx.typing():
            player = await YTDLSource.from_url(url, loop=bot.loop)
            # audio_source = discord.FFmpegPCMAudio(
            #     executable="ffmpeg.exe", 
            #     source=filename, 
            #     before_options = "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5",
            #     options = "-vn"
            # )
            ctx.voice_client.play(player, after = lambda e: print(f"Playback error: {e}") if e else None)
            print(f"Is playing: {ctx.voice_client.is_playing()}")


        await ctx.send(f"🎵 Now playing: **{player.title}**")

    except Exception as e:
        await ctx.send(f"❌ Error: {e}")


@bot.command(name = "pause", help = "This command pauses the song")
async def pause(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_playing():
        voice_client.pause()
    else:
        await ctx.send("The bot is not playing anything at the moment.")

@bot.command(name = "resume", help = "Resume the song")
async def resume(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_paused():
        voice_client.resume()
    else:
        await ctx.send("The bot was not playing anything before this. Use play command")


@bot.command(name = "leave", help = "To make the bot leave the voice channel")
async def leave(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_connected():
        await voice_client.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")
    remove_all_files("downloads")
@bot.command(name = "stop", help = "Stops the song")
async def stop(ctx):

    voice_client = ctx.message.guild.voice_client
    if voice_client.is_playing():
        voice_client.stop()
    else:
        await ctx.send("The bot is not playing anything at the moment.")
    


bot.run(TOKEN)

