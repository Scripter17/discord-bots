import sys, os, asyncio, discord
from discord.ext import commands

intents=discord.Intents.default()
intents.reactions=True
intents.members=True
intents.guilds=True
bot=commands.Bot(command_prefix="~", intents=intents)

channels={}
watching=[] # React dicts of all recent reactions

def getServerGRLogChannel(server):
	if server.id in channels:
		return channels[server.id]
	for channel in server.channels:
		if channel.name=="ghost-reacts":
			channels[server.id]=channel
			return channel

def makeReactDict(reaction, user):
	return {
		"user"   :user,
		"message":reaction.message,
		"emoji"  :reaction.emoji
	}

@bot.event
async def on_ready():
	print("[Hacker voice] I'm in")

@bot.event
async def on_reaction_add(reaction, user):
	reactDict=makeReactDict(reaction, user)
	watching.append(reactDict)
	await asyncio.sleep(5)
	watching.remove(reactDict)

@bot.event
async def on_reaction_remove(reaction, user):
	reactDict=makeReactDict(reaction, user)
	if reactDict in watching:
		if isinstance(reaction.emoji, str):
			emojiID="N/A"
			url="N/A"
		else:
			emojiID=str(reaction.emoji.id)
			url=reaction.emoji.url
		await getServerGRLogChannel(reaction.message.guild).send(f"Ghost react from {user.mention}\nEmoji: {reaction.emoji}\nID: {emojiID}\nMessage: {reaction.message.jump_url}\nURL: {url}")

bot.run(os.environ["grdbot"])
