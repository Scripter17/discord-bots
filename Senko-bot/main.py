#https://discordapp.com/oauth2/authorize?client_id=578753573140299787&scope=bot
"""
o=[]
l=document.querySelectorAll("h3 + table");
for (x=0; x<l.length; x++){
	p=[]
	//l[0].children[0].children[1].children[3].children[0].innerHTML
	for (y=1; y<l[x].children[0].children.length; y++){
		p.push(l[x].children[0].children[y].children[3].children[0].innerHTML)
	}
	o.push(p.join(","))
}
console.log(o.join("\n"))
"""
import discord, os, sys, asyncio
sys.path.append("..")
import globalTools

client=discord.Client()

delChannel=[]
notSoBot=None
thanatos=None # He agreed to be @ed every time the exploit is used
theRealSenko=None
certifiedSenko=None
jolyneIrl=None
colorTime=60
pokemonTags=open("pokemon.txt", "r").read().replace("\n", ",").replace(" ", "_").lower().split(",")

@client.event
async def on_message(message):
	global colorTime
	global thanatos, notSoBot, delChannel
	if message.author==client.user:
		return
	if message.content==".r34 samus_aran test":
		await client.send_message(message.channel, ".undo")
	if message.content.lower().split(" ")[0] in [".e621", ".r34", ".paheal", ".xbooru", ".yandera", ".pornhub"]:
		if "+" in message.content or "%" in message.content:
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
		elif True in [x in pokemonTags for x in message.content.lower().split(" ")]:
			delChannel.append(message.channel)
			reply="Pokémon tags are banned"
			await client.send_message(message.channel, reply)
			await client.delete_message(message)
	elif message.channel in delChannel and message.author==notSoBot:
		#print("aaa",delChannel)
		await client.delete_message(message)
		while message.channel in delChannel: # Just to be safe
			delChannel.pop(delChannel.index(message.channel))
	if message.author==theRealSenko:
		if message.content.lower().startswith("$verify"):
			for mem in message.mentions:
				await client.add_roles(mem, certifiedSenko)
		elif message.content.lower().startswith("$revoke"):
			for mem in message.mentions:
				await client.remove_roles(mem, certifiedSenko)
		elif message.content.lower().startswith("$timer "):
			colorTime=int(message.content.split(" ")[1])
async def rainbowRole():
	color=0
	colors=[discord.Colour.red(), discord.Colour.orange(), discord.Colour.gold(), discord.Colour.green(), discord.Colour.blue(), discord.Colour.purple()]
	while True:
		await client.edit_role(server=jolyneIrl, role=certifiedSenko, colour=colors[color])
		color=(color+1)%len(colors)
		await asyncio.sleep(colorTime)

@client.event
async def on_ready():
	global thanatos, notSoBot, theRealSenko, jolyneIrl, certifiedSenko
	thanatos=await client.get_user_info("185220964810883072")
	notSoBot=await client.get_user_info("439205512425504771")
	theRealSenko=await client.get_user_info("335554170222542851")
	jolyneIrl=client.get_server(id="560507261341007902")
	certifiedSenko=discord.utils.get(jolyneIrl.roles, id="587354703764127783")
	print(certifiedSenko)
	# Do the certifiedSenko thing
	globalTools.log('NotSoBot-r34-hotfix bot is ready (%s | %s)'%(client.user.id, client.user.name))
	await rainbowRole()

client.run(os.environ["nsb34"])