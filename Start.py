import subprocess as sp
commands=["python ReroBot.py", "python CancerBot.py", "python YesNo.py", "python DIOBot.py"]
proc=[sp.Popen(cmd, shell=True) for cmd in commands]
for p in proc: p.wait()
