# https://www.devdungeon.com/content/make-discord-bot-python
# https://discordapp.com/oauth2/authorize?client_id=508384658166382593&scope=bot
import discord, cowsaygen, sys, re, os, time
from currency_converter import CurrencyConverter
sys.path.append("..")
import globalTools

cConv=CurrencyConverter()
client=discord.Client()
class __:
	prefix="$"
	class cooldowns:
		jacksonGBT=0
		fuckoff=0
	class roles:
		initBullshit=-1 # Pretend it's unsigned
class functions:
	def help(message):
		await client.send_message(message.channel, """Cancerbot by James C. Wise - Help
Commands:
	{0}help: Display this message
	{0}conv [amount] [starting currency] [ending currency]: Convert from one currency to another. Example: `{0}conv 2 CAD GBP`
	{0}cowsay [text]: The classic Linux command but on discord! The [text] can have newlines, either by pressing SHIFT+ENTER or by typing `\\n`.
	(Note: Lines that are too long will make it look ugly, I'm working on fixing it but be patient)
Auto... things:
	Run if Jackson:
		Jackson (aka Llamacorn) is a... well he's a character.
		As such, there are a few things this bot is designed to prevent him, and him specifically, from doing.
			Gif spam: Jackson can only send tenor.com gifs once every 20 seconds
			`:WOKE:` and `:iamaloser:`: Those are two emojis on my server, and Jackson is banned from using them
	ooof:
		If you say "ooof" (more than 2 `o`s) or "oog", the bot will call you a moron.
	`@everyone`:
		If you do `@everyone`, the bot will call you a marrowey clog, because you are one.
	Robot racism:
		If you type, for example, "beep boop bop", the bot will say that's racist towards robots.
		I don't remember why I added it, but I did.
Notice:
	Please note that this bot was soley intended to work on my server and *my server only*, any other servers might cause this bot to have problems and/or crash.""".format(__.prefix))
	async def runIfJackson(message):
		authorId, authorName, content=message.author.id, message.author.name, message.content.lower()
		global cooldown # Global warming fixed!
		if "https://tenor.com/view/" in content: # Make Jackson able to use tenor, but not spam with it.
			#print("Jackson: "+"\n\t".join(MESSAGE.split("\n"))
			globalTools.log("(cancer) Jackson used GIF")
			if time.time()-__.cooldowns.jacksonGBT<20:
				await client.delete_message(message)
				if time.time()-__.cooldowns.fuckoff>=20:
					await client.send_message(message.channel, "Cooldown remaining: "+str(20-int(time.time()-__.cooldowns.jacksonGBT))+" seconds.")
				globalTools.log("(cancer) It's not very effective")
				__.cooldowns.fuckoff=time.time()
			else:
				__.cooldowns.jacksonGBT=time.time()
		if ":woke:" in content or ":iamaloser:" in content:
			await client.delete_message(message)
			if time.time()-__.cooldowns.fuckoff>=20:
				await client.send_message(message.channel, "Fuck off with that shit")
			globalTools.log("(cancer) Jackson can fuck off with that shit")
			__.cooldowns.fuckoff=time.time()
	
	async def ooof(message):
		authorId, authorName, content=message.author.id, message.author.name, message.content.lower()
		await client.send_message(message.channel, "IT'S \"OOF\" YOU FUCKING MORON")
		globalTools.log("(cancer) %s (%s) is a moron"%(authorId, authorName))
	
	async def conv(message):
		authorId, authorName, content=message.author.id, message.author.name, message.content.upper() # Currency names have to be in uppercase
		args=content[len(__.prefix)+5:].split(" ")
		print(args)
		try:
			args[0]=float(args[0])
		except:
			await client.send_message(message.channel, "You gotta make the first argument just a number, don't put $, €, or whatever before/after it")
			return None
		await client.send_message(message.channel, "%0.02f %s = %0.02f %s"%(args[0], args[1], cConv.convert(args[0], args[1], args[2]), args[2]))
	
	async def cowsay(message):
		authorId, authorName, content=message.author.id, message.author.name, message.content.lower()
		say=message.content[len(__.prefix)+7:]
		if say[0]=="\n": say=say[1:]
		say=say.replace("\n","\\n")
		await client.send_message(message.channel, "```"+cowsaygen.cowsaygen(say)+"```")
		globalTools.log("(cancer) %s (%s) cowsayed %s"%(authorId, authorName, say))
	
	async def atEveryone(message):
		authorId, authorName, content=message.author.id, message.author.name, message.content.lower()
		await client.send_message(message.channel, "Stop it with `@everyone`, you marrowey clog.")
		globalTools.log("(cancer) %s (%s) pinged everyone"%(authorId, authorName))
	
	async def robotRacism(message):
		authorId, authorName, content=message.author.id, message.author.name, message.content.lower()
		robotRacism=re.match("((beep|boop|bop|bz+t) ?)+", content)
		if robotRacism!=None:
			await client.send_message(message.channel, ">"+robotRacism[0]+"\nTHAT'S RACIST TOWARDS ROBOTS")
			globalTools.log("(cancer) %s (%s) is racist towards robots"%(authorId, authorName))
	
	async def doRoles(message):
		content, server=message.content, message.server
		if server!=__.myServer:
			return
		#print(content)
		match=re.match("GG <@\d+>, your cancer progressed to stage (\d+)!", content)
		if match!=None:
			match=int(match[1])
			#print(match, __.roles.levels[match] if match in __.roles.levels.keys() else __.roles.levels)
			if match in __.roles.levels.keys():
				await client.add_roles(message.mentions[0], __.roles.levels[match])

funcMap={
	"conv": functions.conv,
	"cowsay": functions.cowsay,
	"help": functions.help
}

@client.event
async def on_message(message):
	try:
		if message.author==client.user:
			return
		if message.author!=os.environ["James"] and os.environ["test"]=="true": return
		authorId, authorName, content=message.author.id, message.author.name, message.content.lower()
		
		funcName=globalTools.getFunc(__.prefix, content)
		if funcName in funcMap.keys(): await funcMap[funcName](message)
		
		if authorId=="159985870458322944": await functions.doRoles(message) # MEE6 bot stuff
		if authorId==os.environ["Jackson"]: await functions.runIfJackson(message)
		if re.match("\\b(o{2,}g|o{3,}f)\\b", content): await functions.ooof(message)
		if message.mention_everyone: await functions.atEveryone(message)
		await functions.robotRacism(message)
	except:
		globalTools.msgMe(client, "Shit's fucked, check logs.")
@client.event
async def on_ready():
	print('Cancerbot is ready! (%s | %s)'%(client.user.id, client.user.name))
	# I need to put this here because `await client.wait_until_ready()` won't work in the class definiton.
	# also `await class x:` doesn't work so I can't make it work.
	# aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
	__.roles.myServer=client.get_server(id=str(os.environ["myServer"]))
	__.myServer=client.get_server(id=str(os.environ["myServer"]))
	__.roles.levels={
		1: list(filter(lambda x:x!=None, [(x if x.name=="Diagnosed (level 1)" else None) for x in __.roles.myServer.roles]))[0],
		4: list(filter(lambda x:x!=None, [(x if x.name=="Terminal (level 4)" else None) for x in __.roles.myServer.roles]))[0]
	}

client.run(os.environ["cbottoken"])
