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
class people:
	theRealSenko=None
	notSoBot=None
	designatedAtMod=None # He agreed to be @ed every time the exploit is used
class servers:
	class jolyneIrl:
		server=None
		certifiedSenko=None
	class mine:
		server=None
		certifiedSenko=None
servers.list=[servers.jolyneIrl, servers.mine]

delChannel=set()
colorTime=60
pokemonTags=open("pokemon.txt", "r").read().replace("\n", ",").replace(" ", "_").lower().split(",")

@client.event
async def on_message(message):
	if message.author==client.user:
		return
	cserver=servers.list[[x.server for x in servers.list].index(message.server)]
	if message.content.lower().split(" ")[0] in [".e621", ".r34", ".paheal", ".xbooru", ".yandera", ".pornhub"]:
		if "+" in message.content or "%" in message.content:
			delChannel.add(message.channel)
			await client.delete_message(message)
			reply="Commands with `+` and/or `%` are not allowed. 'Why' is not important."
			reply+="\n"+people.designatedAtMod.mention+", "+message.author.mention+" used the command"
			reply+="\n```"+message.content.replace("`", "`\u200b")+"```" # "\u200b" = Zero-width space
			await client.send_message(message.channel, reply)
		elif message.channel==servers.jolyneIrl.server and pokemonTags&set(message.content.lower.split(" "))!={}:
			delChannel.add(message.channel)
			reply="Pokémon tags are banned, sorry."
			reply+="\nBTW I might've deleted the wrong message, if so, sorry."
			await client.send_message(message.channel, reply)
			await client.delete_message(message)
	elif message.channel in delChannel and message.author==people.notSoBot and not message.content.lower().startswith(":no_entry: **cooldown**"):
		await client.delete_message(message)
		delChannel.remove(message.channel)
	if message.author==people.theRealSenko:
		if message.content.lower().startswith("$verify"):
			for mem in message.mentions:
				await client.add_roles(mem, cserver.certifiedSenko)
		elif message.content.lower().startswith("$revoke"):
			for mem in message.mentions:
				await client.remove_roles(mem, cserver.certifiedSenko)
		elif message.content.lower()=="$list" and message.server in [x.server for x in servers.list]:
			reply="```"
			for mem in cserver.server.members:
				for role in mem.roles:
					if role==cserver.certifiedSenko:
						reply+="\n"+mem.name+"#"+mem.discriminator+" | <@!"+mem.id+">"
			reply+="```"
			await client.send_message(message.channel, reply)

async def rainbowRole():
	color=0
	colors=[discord.Colour.red(), discord.Colour.orange(), discord.Colour.gold(), discord.Colour.green(), discord.Colour.blue(), discord.Colour.purple()]
	while True:
		for s in servers.list:
			await client.edit_role(server=s.server, role=s.certifiedSenko, colour=colors[color])
		color=(color+1)%len(colors)
		await asyncio.sleep(colorTime)

@client.event
async def on_ready():
	people.designatedAtMod=await client.get_user_info("185220964810883072") # Thanatos
	people.notSoBot=await client.get_user_info("439205512425504771")
	people.theRealSenko=await client.get_user_info("335554170222542851")
	# The public Jolyne_irl server
	servers.jolyneIrl.server=client.get_server(id="560507261341007902")
	servers.jolyneIrl.certifiedSenko=discord.utils.get(servers.jolyneIrl.server.roles, id="587354703764127783")
	# My server
	servers.mine.server=client.get_server(id="462645694084284417")
	servers.mine.certifiedSenko=discord.utils.get(servers.mine.server.roles, id="596917358732378112")
	# Do the certifiedSenko thing
	globalTools.log('Senko-bot bot is ready (%s | %s)'%(client.user.id, client.user.name))
	await rainbowRole()

client.run(os.environ["nsb34"])
