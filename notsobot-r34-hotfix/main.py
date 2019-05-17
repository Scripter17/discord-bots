#https://discordapp.com/oauth2/authorize?client_id=578753573140299787&scope=bot
import discord, os, sys
sys.path.append("..")
import globalTools

client=discord.Client()

delChannel=None
notSoBot=None
thanatos=None

@client.event
async def on_message(message):
	global thanatos, notSoBot, delChannel
	if message.author==client.user:
		return
	if message.content.lower().startswith(".r34") and ("+" in message.content or "%" in message.content):
		delChannel=message.channel
		print(delChannel)
		await client.delete_message(message)
		reply="""No. Just because the bot lets you bypass the block list, doesn't mean I will.
		%s, %s appears to have bypassed the banned tag filter (or at least attempted to) with the following command
		`%s`""".replace("\t", "")%(thanatos.mention, message.author.mention, message.content.replace("@", "@ "))
		if "`" in message.content:
			reply+="\nThe cheeky bugger seems to be trying to break me, too."
		await client.send_message(message.channel, reply)
	elif delChannel!=None and message.channel==delChannel and message.author==notSoBot:
		print("aaa",delChannel)
		await client.delete_message(message)
		delChannel=None  

@client.event
async def on_ready():
	global thanatos, notSoBot
	thanatos=await client.get_user_info("185220964810883072")
	notSoBot=await client.get_user_info("439205512425504771")
	globalTools.log('NotSoBot-r34-hotfix bot is ready (%s | %s)'%(client.user.id, client.user.name))

client.run(os.environ["nsb34"])
