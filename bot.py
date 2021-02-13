import discord
from discord.ext import commands

client = commands.Bot(command_prefix="!")

@client.event
async def online():
    print("Bot is ready to use")

@client.command()
async def bothelp(ctx):
    await ctx.send("Hi. I'm Tea, the discord bot. I am still in develop so I don't have much command.")

@client.command()
async def invite(ctx):
    await ctx.send("https://discord.com/api/oauth2/authorize?client_id=807100950728278046&permissions=0&scope=bot")

@client.command(aliases=["k"])
@commands.has_permissions(kick_members = True)
async def kick(ctx, member : discord.Member, *, reason="No reason provided"):
    await ctx.send(member.mention + " has been kicked. Reason:"+reason)
    await member.kick(reason=reason)

@client.command(aliases=["b"])
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason="No reason provided"):
    await ctx.send(member.mention + " has been banned. Reason:"+reason)
    await member.ban(reason=reason)

client.run("ODA3MTAwOTUwNzI4Mjc4MDQ2.YBzFVQ.B33TU7_lLmGobwuGK_y4fSg5frA")
