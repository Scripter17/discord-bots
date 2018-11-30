def cowsaygen(txt):
	cow=r"""
 \   ^__^
  \  (oo)\_______
     (__)\       )\/\
         ||----w |
         ||     ||
	"""
	ret=""
	msg=txt.split("\\n")
	maxlen=max([len(x) for x in msg])
	cow=cow.replace("\n","\n"+" "*min(maxlen//2+1, 8))[1:]
	ret+=" "+"_"*(maxlen+2)+"\n"
	for i,x in enumerate(msg):
		pre="<"
		pos=">"
		if len(msg)!=1:
			if i==0:
				pre="/"
				pos="\\"
			elif i==len(msg)-1:
				pre="\\"
				pos="/"
			else:
				pre="|"
				pos="|"
		ret+=pre+" "+x+" "*(maxlen-len(x)+1)+pos+"\n"
	ret+=" "+"-"*(maxlen+2)+"\n"
	ret+=cow
	return ret