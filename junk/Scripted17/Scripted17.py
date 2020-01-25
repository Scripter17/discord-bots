import praw, pdb, re, os, time, urllib.request, pyscp
botStart=time.time()

class funcs:
	class __:
		def urlIsAlive(url): #https://gist.github.com/dehowell/884204
			request = urllib.request.Request(url)
			request.get_method = lambda: 'HEAD'
			try:
				urllib.request.urlopen(request)
				return True
			except urllib.request.HTTPError:
				return False
	def onComment(comment):
		print(comment.body)
		links=[]
		for matches in re.findall(pat, comment.body):
			url="http://www.scp-wiki.net/"+matches[2:-2]
			if urlIsAlive(url): # Check if page exists
				article=funcs.__.scpwiki(matches[2:-2])
				print("aaaa")
				links.append("["+matches[2:-2]+" "+str(article.title)+"](http://www.scp-wiki.net/"+matches[2:-2]+")") # Format links. The rating is done in a way such that Marvin isn't triggered
		if len(links)>0: # If at least one valid page is found, link it/them
			CID="".join(["&#x"+hex(ord(x))[2:]+";" for x in comment.id])
			footer="\n\n***\n\n^(This was done automatically by Scripter17's bot | Replying to %s)"%CID
			comment.reply("\n\n".join(links)+footer) # Reply
funcs.__.scpwiki=pyscp.wikidot.Wiki("www.scp-wiki.net")
print("aaaa")
pat=re.compile(r"({\[.+?\]})") # RegEx to detect pages. {[Stuff]}
bot=praw.Reddit(user_agent='bot1', client_id=os.environ["scripted17ID"], client_secret=os.environ["scripted17SEC"])
user=bot.redditor("Scripter17") # Me
comments=user.stream.comments() # My comments
for comment in comments:
	if comment.created_utc<botStart:
		continue
	funcs.onComment(comment)
