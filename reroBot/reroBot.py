# https://www.devdungeon.com/content/make-discord-bot-python
import discord, random, re, os, sys
sys.path.append("..")
import globalTools

client=discord.Client()
class __:
	whymsg=["I have absolutely no idea.", "Why not?", "¯\_(ツ)_/¯", "Because one of my friends told me to."]
	prefix="r/"

class functions:
	async def help(client, message):
		await client.send_message(message.channel, \
"""Literally just type 'RERO' (case insensitive) anywhere and I will reply to you.
If you don't get the meme, watch JoJo's Bizarre Adventure Part 3 episode 9.
Commands: `r/help`, `r/why`, `r/explain`, and `r/invite`.
Secret Commands: The fact that there are secret commands is the only hint you're getting.""")
	async def why(message):
		await client.send_message(message.channel, random.choice(__.whymsg))
	async def invite(message):
		await client.send_message(message.channel, "https://discordapp.com/oauth2/authorize?client_id=485540685965950978&scope=bot")
	async def explain(message):
		await client.send_file(message.channel, r"rero-bot-explain.jpg")
	async def egg(message):
		await client.send_file(message.channel, r"rero-bot-egg.jpg")
	async def scream(message):
		await client.send_file(message.channel, r"rero-bot-scream.jpg")
funcMap={
	"help":functions.help,
	"why":functions.why,
	"invite":functions.invite,
	"egg":functions.egg,
	"scream":functions.scream,
	"explain":functions.explain
}
@client.event
async def on_message(message):
	try:
		# we do not want the bot to reply to itself
		if message.author==client.user:
			return
		if message.author!=os.environ["James"] and os.environ["test"]=="true": return
		authorId, authorName, content=message.author.id, message.author.name, message.content.lower()
		
		funcName=globalTools.getFunc(__.prefix, content)
		if funcName in funcMap.keys():
			globalTools.log("(rero) %s (%s) %s"%(authorId, authorName, content))
			await funcMap[funcName](message)
		elif "rero" in content:
			globalTools.log("(rero) %s (%s) Rero'd"%(authorId, authorName))
			msg="RERO RERO RERO RERO RERO RERO RERO RERO"
			if "reor" in content:
				msg+="\n Also, it's \"RERO\", idiot"
				globalTools.log("(rero) %s (%s) Also Reor'd"%(authorId, authorName))
			await client.send_message(message.channel, msg)
		elif "reor" in content:
			globalTools.log("(rero) %s (%s) Reor'd"%(authorId, authorName))
			await client.send_message(message.channel, "It's \"RERO\", idiot.")
	except Exception as e:
		globalTools.log(e)
		globalTools.msgMe(client, "Shit's fucked, check logs.")

@client.event
async def on_ready():
	globalTools.log('Rero bot is ready! (%s | %s)'%(client.user.id, client.user.name))

client.run(os.environ["rbottoken"])
