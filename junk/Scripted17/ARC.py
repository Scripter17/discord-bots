import praw # Reddit API
import pdb
import re # RegEx
import os
import urllib.request
def urlIsAlive(url): #https://gist.github.com/dehowell/884204
	request = urllib.request.Request(url)
	request.get_method = lambda: 'HEAD'
	try:
		urllib.request.urlopen(request)
		return True
	except urllib.request.HTTPError:
		return False

# Get comments already replied to
if not os.path.isfile("PostList.txt"):
	pr=[]
	pw=open("PostList.txt", "w")
else:
	pr=open("PostList.txt", "r").read().split("\n")
pat=re.compile(r"({\[.+?\]})") # RegEx to detect pages. {[Stuff]}

user=praw.Reddit('bot1').redditor("Scripter17") # Me
comments=user.stream.comments() # My comments
for comment in comments:
	if comment.id in pr: # If the comment is already replied to, skip it
		continue
	print(comment.id)
	open("PostList.txt", "a").write("\n"+comment.id)
	pr.append(comment.id)
	l=[]
	for u in re.findall(pat, comment.body):
		print(u) # Print matches
		if urlIsAlive("http://www.scp-wiki.net/"+u[2:-2]): # Check if page exists
			l.append("["+u[2:-2]+"](http://www.scp-wiki.net/"+u[2:-2]+")") # Format links. The rating is done in a way such that Marvin isn't triggered
	if len(l)>0: # If at least one valid page is found, link it/them
		try:
			comment.reply("\n\n".join(l)+"\n\n***\n\n^(This was done automatically by Scripter17's 2^nd bot | Replying to "+"".join(["&#x"+hex(ord(x))[2:]+";" for x in comment.id])+")") # Reply
			print("Replied")
			open("PostList.txt", "a").write("\nAbove Had Reply")
		except Exception as e:
			print(e)
			open("PostList.txt", "a").write("\nAbove Errored: "+str(e))
	print("-------")
