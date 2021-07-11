import subprocess

def execShell(shellname):
    bashCommand = "/home/pi/habcatpi/CLI/shells/"+shellname+".sh"
    process = subprocess.Popen(['/bin/bash', bashCommand], shell=False, stdout=subprocess.PIPE)
    output, error = process.communicate()
    print(output.decode("utf-8"))