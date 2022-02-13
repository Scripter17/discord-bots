import subprocess as sp
commands=[
	"python senko.py",
	"python yadb.py"
]
procs=[sp.Popen(command, shell=True) for command in commands]
for proc in procs:
	proc.wait()
