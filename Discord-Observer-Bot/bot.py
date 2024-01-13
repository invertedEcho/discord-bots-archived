import discord
from discord.ext import commands, tasks
import config
import os
import datetime
import logging
from dotenv import load_dotenv
from keep_alive import keep_alive
load_dotenv()
keep_alive()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix="_", intents=intents)

# Convert days to hours cause we can only use hours.
# hours = int(config.DAYS) * 24

level = logging.WARNING
fmt = '[%(levelname)s] %(asctime)s - %(message)s'
logging.basicConfig(level=level, format=fmt)


@tasks.loop(hours=24)
async def inform(ctx):
    print("Yes.")
    members = await ctx.guild.fetch_members().flatten()
    for member in members:
        roles_of_member = member.roles
        for role in roles_of_member:
            if str(role) in config.ROLES_TO_LOOK_FOR:
                first_time = datetime.datetime.now()
                joined_time = member.joined_at
                diff = first_time - joined_time
                channel: discord.TextChannel = client.get_channel(
                    id=config.CHANNEL_ID)
                if diff.days <= 30:
                    await channel.send(f"INFO: {member.name} has now been on the server for {str(diff.days)} days")
                if diff.days >= config.DAYS:
                    if diff.days <= 30:
                        await channel.send(f"@here IMPORTANT: {member.name} has now been on the server for {str(diff.days)} days.")


@client.command()
async def start(ctx):
    await ctx.send("Task starting...")
    inform.start(ctx)


@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, number):
    await ctx.message.delete()
    channel = ctx.message.channel
    messages = await channel.history(limit=int(number)).flatten()
    await channel.delete_messages(messages)


@client.event
async def on_ready():
    print("Bot is ready.")

client.run(TOKEN)
