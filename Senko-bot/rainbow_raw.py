import discord, asyncio
client=discord.Client()

jolyneIrl=None
gimpMaster=None

async def rainbowRole():
	# Get the server
	jolyneIrl=client.get_server(id="560507261341007902")
	# Get the role
	gimpMaster=discord.utils.get(jolyneIrl.roles, id="587354703764127783")
	color=0 # Color number, 0-5
	colors=[discord.Colour.red(), discord.Colour.orange(), discord.Colour.gold(), discord.Colour.green(), discord.Colour.blue(), discord.Colour.purple()]
	while True:
		await client.edit_role(server=jolyneIrl, role=gimpMaster, colour=colors[color])
		color=(color+1)%len(colors) # Add one and loop around
		await asyncio.sleep(60) # Reduce workload by stopping for 60 seconds
		# IIRC Heroku hated while true loops, so this might crash in a bit

@client.event
async def on_ready():
	await rainbowRole()

client.run("BOT ID HERE")
