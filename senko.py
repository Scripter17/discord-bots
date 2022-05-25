import datetime, colorsys, os, sys, asyncio, time, discord, regex
from discord.ext import commands

bot=commands.Bot(command_prefix="$")

@bot.event
async def on_ready():
	print("[Hacker voice] I'm in")
	await doRoles()

currentRoleColor=None
async def doRoles():
	while True:
		if getColor()==currentRoleColor:
			await asyncio.sleep(60*30)
			continue
		for server in bot.guilds:
			role=discord.utils.get(server.roles, name="Senko Moment")
			if role is not None:
				try:
					await role.edit(color=getColor())
				except Exception as e:
					print(e)
		await asyncio.sleep(60*30)

def getColor():
	color=colorsys.hsv_to_rgb(getHue(), 1, 1)
	color=(round(color[0]*255), round(color[1]*255), round(color[2]*255))
	return discord.Color((color[0]<<16)+(color[1]<<8)+color[2])

def getHue():
	today=datetime.datetime.today()
	return today.timetuple().tm_yday/(365+isLeapYear(today.year))

def isLeapYear(y):
	return y%4==0 and y%100!=0 or y%400==0

@bot.event
async def on_message(message):
	if regex.search(r"(child attraction quirk){e<=5}", message.content):
		await message.delete()

bot.run(os.environ["senkobottoken"])
