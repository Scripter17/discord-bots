# https://www.devdungeon.com/content/make-discord-bot-python
# https://discordapp.com/oauth2/authorize?client_id=508384658166382593&scope=bot
import discord, cowsaygen, sys, re, os, time, random
from currency_converter import CurrencyConverter
sys.path.append("..")
import globalTools

cConv=CurrencyConverter()
client=discord.Client()
class __:
	def init():
		__.myServer=client.get_server(id=str(os.environ["myServer"]))
		__.roles.levels={
			1: "Diagnosed (level 1)",
			4: "Terminal (level 4)",
			5: "Already dead (level 5)",
			10: "「CANCER ACT 10」 (level 10)"
		}
		for k in __.roles.levels:
			for x in __.myServer.roles:
				if x.name==__.roles.levels[k]:
					__.roles.levels[k]=x
	prefix="$"
	class cooldowns:
		jacksonGIF=0
		fuckoff=0
	class roles:
		initBullshit=-1 # Pretend it's unsigned

class functions:
	async def runIfJackson(message):
		authorId, authorName, content=message.author.id, message.author.name, message.content.lower()
		global cooldown # Global warming fixed!
		                # That's not even remotely funny, past me
		now=time.time()
		if "https://tenor.com/view/" in content: # Make Jackson able to use tenor, but not spam with it.
			globalTools.log("(cancer) Jackson used GIF")
			if now-__.cooldowns.jacksonGIF<20:
				await client.delete_message(message)
				if now-__.cooldowns.fuckoff>=20:
					await client.send_message(message.channel, "Cooldown remaining: %d seconds."%(20-int(now-__.cooldowns.jacksonGIF)))
				globalTools.log("(cancer) It's not very effective")
				__.cooldowns.fuckoff=now
			else:
				__.cooldowns.jacksonGIF=now
	
	async def ooof(message):
		authorId, authorName, content=message.author.id, message.author.name, message.content.lower()
		await client.send_message(message.channel, "IT'S \"OOF\" YOU FUCKING MORON")
		globalTools.log("(cancer) %s (%s) is a moron"%(authorId, authorName))
	
	async def conv(message):
		authorId, authorName, content=message.author.id, message.author.name, message.content.upper() # Currency names have to be in uppercase
		args=content[len(__.prefix)+5:].split(" ")
		try:
			args[0]=float(args[0])
		except:
			await client.send_message(message.channel, "You gotta make the first argument just a number, don't put $, €, or whatever before/after it")
			return None
		await client.send_message(message.channel, "%0.02f %s = %0.02f %s"%(args[0], args[1], cConv.convert(args[0], args[1], args[2]), args[2]))
	
	async def cowsay(message):
		authorId, authorName, content=message.author.id, message.author.name, message.content.lower()
		say=content[len(__.prefix)+7:]
		say=" ".join(say.split("​"))
		say="`​``".join(say.split("```"))
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
		match=re.match("GG <@!?\d+>, your cancer progressed to stage (\d+)!", content)
		if match!=None:
			match=int(match[1])
			if match in __.roles.levels.keys():
				await client.add_roles(message.mentions[0], __.roles.levels[match])
	
	async def wtf(message):
		await client.send_file(message.channel, "wtf/%d.jpg"%random.randint(1,18))
	
	async def oneSecond(message):
		time.sleep(1)
		await client.send_file(message.channel, r"1sec.jpg")
funcMap={
	"conv": functions.conv,
	"cowsay": functions.cowsay,
	"wtf": functions.wtf
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
		
		# globalTools.log(authorId+" "+os.environ["James"])
		if authorId in ["159985870458322944", os.environ["James"]]: await functions.doRoles(message)
		if authorId==os.environ["Jackson"]: await functions.runIfJackson(message)
		if re.match("\\b(o{2,}g|o{3,}f)\\b", content): await functions.ooof(message)
		if message.mention_everyone: await functions.atEveryone(message)
		await functions.robotRacism(message)
		if re.match(r"^((yeah|o?k|oh?),? )?(one?|1) ?sec(ond)?[.!]?$", content, flags=re.I): await functions.oneSecond(message)
	except Exception as e:
		globalTools.log(e)
		await globalTools.msgMe(client, "Shit's fucked, check logs.")

@client.event
async def on_ready():
	__.init()
	globalTools.log('Cancerbot is ready! (%s | %s)'%(client.user.id, client.user.name))
	globalTools.log("aaa", out=sys.stderr.write)

client.run(os.environ["cbottoken"])
