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
import discord, os, sys, asyncio#, jolyne_irl
sys.path.append("..")
import globalTools

ready=False
client=discord.Client()
URLChars="+%&#"
colorTime=60

notSoBot=None
theRealSenko=None

senkoRoles={}

def getRoles():
	global senkoRoles
	for server in clinet.servers:
		for role in server.roles:
			if role.name.lower()=="certified senko":
				senkRoles[server.id]=role.id
	print(senkoRoles)

@client.event
async def on_message(message):
	if message.author==client.user or not ready:
		return
	cserver=servers.list[[x.server for x in servers.list].index(message.server)]
	# Senko commands
	if message.author==people.theRealSenko:
		if message.content.lower().startswith("$verify"):
			# Give a user the Certified Senko role for the server
			# Rules: Have a Senko-san pfp, or at least the ears
			for mem in message.mentions:
				await client.add_roles(mem, senkoRoles[server.id])
		elif message.content.lower().startswith("$revoke"):
			# Revoke Certified Senko
			for mem in message.mentions:
				await client.remove_roles(mem, senkoRoles[server.id])
		elif message.content.lower()=="$list":
			# List all Senkos
			reply="```"
			for mem in cserver.server.members:
				for role in mem.roles:
					if role==senkoRoles[server.id]:
						reply+="\n"+mem.name+"#"+mem.discriminator+" | <@!"+mem.id+">"
			reply+="```"
			await client.send_message(message.channel, reply)

async def rainbowRole():
	color=0
	colors=[discord.Colour.red(), discord.Colour.orange(), discord.Colour.gold(), discord.Colour.green(), discord.Colour.blue(), discord.Colour.purple()]
	while True:
		for server in client.servers:
			await client.edit_role(server=server, role=senkRoles[server.id], colour=colors[color])
		color=(color+1)%len(colors)
		await asyncio.sleep(colorTime)

@client.event
async def on_ready():
	global ready, notSoBot, theRealSenko
	#people.designatedAtMod=await client.get_user_info("185220964810883072") # Thanatos
	people.notSoBot=await client.get_user_info("439205512425504771")
	people.theRealSenko=await client.get_user_info("335554170222542851") # Me
	
	globalTools.log('Senko-bot bot is ready (%s | %s)'%(client.user.id, client.user.name))
	ready=True
	# Do the certifiedSenko thing
	#await rainbowRole()
	while True:
		try:
			await rainbowRole()
		except Exception as e:
			print(e)

client.run(os.environ["senkobottoken"])
