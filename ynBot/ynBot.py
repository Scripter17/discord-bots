# https://www.devdungeon.com/content/make-discord-bot-python
# https://discordapp.com/oauth2/authorize?client_id=497561729048510465&scope=bot
import discord, re, os, sys
sys.path.append("..")
import globalTools

class __:
	prefix="yn/"

class functions:
	async def help(message):
		await client.send_message(message.channel, "yn/yes => yesyesyes.jpg\nyn/no => nonono.jpg")
		globalTools.log("(yn) %s (%s) asked for help"%(AID, ANAME))
	async def yes(message):
		await client.send_file(message.channel, r"yn-bot-yesyesyes.jpg")
		globalTools.log("(yn) %s (%s) said yes"%(AID, ANAME))
	async def no(message):
		await client.send_file(message.channel, r"yn-bot-nonono.jpg")
		globalTools.log("(yn) %s (%s) said no"%(AID, ANAME))

funcMap={
	"help":functions.help,
	"yes":functions.yes,
	"no":functions.no
}

client=discord.Client()
@client.event
async def on_message(message):
	try:
		if message.author==client.user:
			return
		if message.author!=os.environ["James"] and os.environ["test"]=="true": return
		content=message.content.lower()
		
		funcName=globalTools.getFunc(__.prefix, content)
		if funcName in funcMap.keys(): await funcMap[funcName](message)
	except:
		globalTools.msgMe(client, "Shit's fucked, check logs.")

@client.event
async def on_ready():
	print('YesNo bot is ready! (%s | %s)'%(client.user.id, client.user.name))
client.run(os.environ["ynbottoken"])
