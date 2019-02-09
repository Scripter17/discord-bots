# https://www.devdungeon.com/content/make-discord-bot-python
# https://discordapp.com/oauth2/authorize?client_id=508384658166382593&scope=bot
import discord, cowsaygen, sys, re, os, time
from currency_converter import CurrencyConverter
sys.path.append("..")
import globalTools

cConv=CurrencyConverter()
client=discord.Client()
class __:
	class cooldowns:
		jacksonGBT=0
		fuckoff=0
	prefix="$"
	class roles:
		initBullshit=-1 # Pretend it's unsigned
class functions:
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
		match=re.match("GG .+?, your cancer progressed to stage (\d+)!", content)
		if match!=None:
			match=int(match[1])
			if match in __.roles.levels.keys():
				client.add_roles(message.author, __.roles.levels[match])

funcMap={
	"conv": functions.conv,
	"cowsay": functions.cowsay
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
		
		if authorId=="159985870458322944": await functions.doRoles(message)
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
	# I shit you not, "__" (the parent class) is undefined here.
	# So yes, putting that here too is kind of required.
	# I don't understand either.
	__.roles.levels={
		1: list(filter(lambda x:x!=None, [(x if x.name=="Diagnosed (level 1)" else None) for x in __.roles.myServer.roles]))[0],
		4: list(filter(lambda x:x!=None, [(x if x.name=="Terminal (level 4)" else None) for x in __.roles.myServer.roles]))[0]
	}

client.run(os.environ["cbottoken"])
