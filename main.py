import subprocess as sp
commands=[
	"node senko.js",
	"python yadb.py"
]
procs=[sp.Popen(command, shell=True) for command in commands]
for proc in procs:
	proc.wait()
