import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext, manage_commands,SlashCommand
import Config


intents = discord.Intents.all()
client = commands.Bot(command_prefix='/', intents=intents)
slash = SlashCommand(client, sync_commands=True)
client_token = Config.TOKEN

@client.event
async def on_ready():
    print(f"Logged in as {client.user} (ID: {client.user.id})")
    await client.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name="INSERT STATUS"))

class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(
        name="avatar",
        description="Displays the avatar of the specified user or the message author if no user is provided."
    )
    async def avatar(self, ctx: SlashContext, user: discord.User = None):
        if user is None:
            user = ctx.author
        
        avatar_url = user.avatar_url
        embed = discord.Embed(title=f"{user.name}'s avatar", color=discord.Color.random())
        embed.set_image(url=avatar_url)
        await ctx.send(embed=embed)

client.add_cog(MyCog(client))
client.run(client_token)
