# https://www.devdungeon.com/content/make-discord-bot-python
# https://discordapp.com/oauth2/authorize?client_id=539892745729212426&scope=bot
import discord, PIL, PIL.Image, PIL.ImageDraw, PIL.ImageFont, urllib.request, sys, drawWord, os
sys.path.append("..")
import globalTools

opener=urllib.request.build_opener()
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
urllib.request.install_opener(opener)

client=discord.Client()

class __:
	prefix="meme/"

@client.event
async def on_message(message):
	if message.author==client.user:
		return
	if message.author!=os.environ["James"] and os.environ["test"]=="true": return
	if message.author.id==os.environ["James"] and message.content.lower()==__.prefix+"debug":
		cmd=""
		while cmd!="exit":
			cmd=input(">>>")
			exec(cmd)
	if message.content.lower().startswith(__.prefix+"caption"):
		if len(message.attachments)==0 or message.attachments[0]["url"].split(".")[-1].lower() not in ["png", "jpg"]:
			await client.send_message(message.channel, "No image attached")
		else:
			args=message.content[len(__.prefix)+len("caption")+1:]
			print(args)
			ftype=message.attachments[0]["url"].split(".")[-1]
			urllib.request.urlretrieve(message.attachments[0]["url"], "meme/meme."+ftype)
			img=PIL.Image.open("meme/meme."+ftype)
			textHeight=drawWord.word_wrap_height(PIL.ImageDraw.Draw(img), args, img.size[0], PIL.ImageFont.truetype("arial.ttf", 16))
			print(textHeight)
			newImg=PIL.Image.new("RGB", (img.size[0], img.size[1]+textHeight), (255,255,255))
			newImg.paste(img, (0, textHeight))
			newDraw=PIL.ImageDraw.Draw(newImg)
			drawWord.draw_word_wrap(newDraw, args, max_width=newImg.size[0], fill=(0,0,0), font=PIL.ImageFont.truetype("arial.ttf", 16))
			newImg.save("meme/meme.png")
			await client.send_file(message.channel, 'meme/meme.png')
@client.event
async def on_ready():
	print('Memebot is ready! (%s | %s)'%(client.user.id, client.user.name))
client.run(os.environ["memebottoken"])
