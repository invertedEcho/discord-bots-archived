import discord
import os
from discord.ext import commands
from keep_alive import keep_alive

keep_alive()
TOKEN = os.environ['TOKEN']
client = commands.Bot(command_prefix=".")
hardcode_msg_id = 890657937482190929
emoji_warframe = "<:warframe:774682268551348267>"
emoji_swbf2 = "<:swbf2:866085948190359592>"
emoji_overwatch = "<:overwatch:866085052408791060>"
emoji_minecraft = "<:minecraft:866085540948082699>"
emoji_eso = "<:eso:866085778030723092>"
emoji_ps2 = "<:planetside2:866085609189146695>"
role_swbf2 = "════════SWBF2═══════"
swbf2_subrole = "Trooper"
role_eso = "═════Elder Scrolls Online═════"
eso_subrole = "Son/Daughter of the Avari"
role_warframe = "════════Warframe════════"
role_planetside = "════════Planetside 2════════"
role_overwatch = "════════Overwatch════════"
role_minecraft = "════════Minecraft════════"


@client.event
async def on_ready():
    print("Bot is ready!")


@client.event
async def on_raw_reaction_add(payload):
    member = payload.member
    guild = client.get_guild(598894487694999552)
    role_swbf2 = guild.get_role(612971880470544433)
    swbf2_subrole = guild.get_role(598900107844386819)
    role_eso = guild.get_role(803200652796887050)
    eso_subrole = guild.get_role(866082526261936138)
    role_warframe = guild.get_role(612979731310051358)
    warframe_subrole = guild.get_role(866091738065010688)
    role_ps2 = guild.get_role(866076382160748585)
    ps2_subrole = guild.get_role(866100572175466526)
    role_overwatch = guild.get_role(866076203566759977)
    role_minecraft = guild.get_role(619882693596807178)
    if member.bot:
        return
    elif hardcode_msg_id == payload.message_id and str(payload.emoji) == emoji_swbf2:
        await member.add_roles(role_swbf2)
        await member.add_roles(swbf2_subrole)
    elif hardcode_msg_id == payload.message_id and str(payload.emoji) == emoji_eso:
        await member.add_roles(role_eso)
        await member.add_roles(eso_subrole)
    elif hardcode_msg_id == payload.message_id and str(payload.emoji) == emoji_warframe:
        await member.add_roles(role_warframe)
        await member.add_roles(warframe_subrole)
    elif hardcode_msg_id == payload.message_id and str(payload.emoji) == emoji_ps2:
        await member.add_roles(role_ps2)
        await member.add_roles(ps2_subrole)
    elif hardcode_msg_id == payload.message_id and str(payload.emoji) == emoji_overwatch:
        await member.add_roles(role_overwatch)
    elif hardcode_msg_id == payload.message_id and str(payload.emoji) == emoji_minecraft:
        await member.add_roles(role_minecraft)


@client.command()
async def send_message(ctx):
    global msg
    message = discord.Embed(title="Role Assigning:", color=0xFF5733)
    message.add_field(name="Please react with the emotes accordingly.",
                      value="Hint: You can hover over the icons to see names of the icons.")
    msg = await ctx.send(embed=message)
    await msg.add_reaction(emoji_swbf2)
    await msg.add_reaction(emoji_eso)
    await msg.add_reaction(emoji_warframe)
    await msg.add_reaction(emoji_ps2)
    await msg.add_reaction(emoji_overwatch)
    await msg.add_reaction(emoji_minecraft)

client.run(TOKEN)
