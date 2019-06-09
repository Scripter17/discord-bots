#https://discordapp.com/oauth2/authorize?client_id=578753573140299787&scope=bot
import discord, os, sys, sched
sys.path.append("..")
import globalTools

client=discord.Client()

delChannel=[]
notSoBot=None
thanatos=None # He agreed to be @ed every time the exploit is used
gimpMaster=None
jolyneIrl=None

@client.event
async def on_message(message):
	global thanatos, notSoBot, delChannel
	if message.author==client.user:
		return
	if message.content.lower().startswith(".r34") and ("+" in message.content or "%" in message.content):
		# notSoBot's r34 command allows you to use `.r34 +[tag]` to avoid a ban on `[tag]`
		# This bot prevents you from using that
		delChannel.append(message.channel)
		#print(delChannel)
		await client.delete_message(message)
		reply="""No. Just because the bot lets you bypass the block list, doesn't mean I will.
		%s, %s appears to have bypassed the banned tag filter (or at least attempted to) with the following command
		`%s`""".replace("\t", "")%(thanatos.mention, message.author.mention, message.content.replace("@", "@ "))
		if "`" in message.content:
			reply+="\nThe cheeky bugger seems to be trying to break me, too."
		await client.send_message(message.channel, reply)
	elif message.channel in delChannel and message.author==notSoBot:
		#print("aaa",delChannel)
		await client.delete_message(message)
		while message.channel in delChannel: # Just to be safe
			delChannel.pop(delChannel.index(message.channel))


async def rainbowRole(sc):
	colors=[discord.Colour.red(), discord.Colour.orange(), discord.Colour.gold(), discord.Colour.green(), discord.Colour.blue(), discord.Colour.purple()]
	print(users, colors[c].to_tuple())
	await client.edit_role(server=joleneIrl, role=gimpMaster, colour=colors[c])
	c=(c+1)%len(colors)
	sc.enter(60, 1, rainbowRole, (sc,)) # Heroku does not like `while True`


@client.event
async def on_ready():
	global thanatos, notSoBot
	thanatos=await client.get_user_info("185220964810883072")
	notSoBot=await client.get_user_info("439205512425504771")
	jolyneIrl=client.get_server(id="560507261341007902")
	gimpMaster=discord.utils.get(jolyneIrl.roles, id="587355498358112266")
	# Do the gimpMaster thing
	s=sched.scheduler(time.time, time.sleep)
	s.enter(1, 1, rainbowRole, (s,))

	globalTools.log('NotSoBot-r34-hotfix bot is ready (%s | %s)'%(client.user.id, client.user.name))

client.run(os.environ["nsb34"])
