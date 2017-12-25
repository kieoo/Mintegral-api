import subprocess

ps= subprocess.Popen("ps -ef | grep python", shell=True, stdout=subprocess.PIPE)
if '/data/Mintegral_API_Test/venv/bin/behave' in ps.stdout.read():
    print "test case is already running..."
else:
    cmd = '. venv/bin/activate && behave project/features --junit'
    subprocess.call(cmd, shell=True, executable='/bin/bash')