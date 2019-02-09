import subprocess as sp
commands=[
	"cd reroBot && python reroBot.py",
	"cd cancerBot && python cancerBot.py",
	"cd ynBot && python ynBot.py",
	"cd DIOBot && python DIOBot.py"
	#"cd memeBot && python memeBot.py"
]
proc=[sp.Popen(cmd, shell=True) for cmd in commands]
for p in proc: p.wait()