# https://www.devdungeon.com/content/make-discord-bot-python
# https://discordapp.com/oauth2/authorize?client_id=569276005093736506&scope=bot
import discord, os, globalTools
from datetime import datetime, timedelta
client=discord.Client()
def isSecondWeek():
	epoch=datetime(1970,1,1,0,0,0)
	today=datetime.today()
	epochMonday=epoch-timedelta(epoch.weekday())
	todayMonday=today-timedelta(today.weekday())
	return (todayMonday-epochMonday).days//7%2==0
def getLoc():
	t=(isSecondWeek()+1)*1000+datetime.datetime.today().weekday()*100+datetime.datetime.today().hour
	r=0
	for x in locs:
		if t>=x[0]:
			r=x[1]
	return r

locs=
# WDHH
[[1000, "Home"]]+
[[1008+d*100,"School"] for d in range(5)]+
[[1016+d*100,"Home"] for d in range(5)]+
[[2008+d*100,"School"] for d in range(5)]+
[[2016+d*100,"Home"] for d in range(5)]+
[[2418, "Dad's"]]+
[[2514, "Camp"]]+
[[2619, "Home"]]

@client.event
async def on_message(message):
	if message.content.lower()=="*locate":
		w=datetime.today().weekday()
		h=datetime.today().hour
		if w<5 and 8<=h<=16:
			await client.send_message(message.channel, "James should be at school")
		elif isSecondWeek():
			await client.send_message(message.channel, "James should be at his dad's place")
		else:
			await client.send_message(message.channel, "James should be at home")

@client.event
async def on_ready():
	print(isSecondWeek())
	globalTools.log('WhereTheFuckIsThatBitchJames-bot is ready! (%s | %s)'%(client.user.id, client.user.name))
client.run(os.environ["lbottoken"])
