import threading, os
commands=[
	"cd reroBot && reroBot.py",
	"cd cancerBot && cancerBot.py",
	"cd ynBot && ynBot.py",
	"cd DIOBot && DIOBot.py",
	"cd memeBot && memeBot.py"
]
[threading.Thread(target=os.system, args=[cmd]).start() for cmd in commands]