import socket, os, sys, time
from subprocess import Popen, PIPE


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

new_content = ''
f = open("url.txt", "r")
os.system("mkdir info host_list")
lines = f.readlines()
f.close()
for l in lines:
    if l.startswith('http://'):
        x = l.replace("http://", "")
    elif l.startswith('https://'):
        x = l.replace("https://", "")
    else:
        x = l

    new_content += (x + '\n',x)[x[len(x) - 1] == '\n']

    hostname = x
    response = os.system("wget --no-check-certificate --timeout=5 --tries=1 " + hostname)
    if response == 0:
        pingstatus = "Network Active'\n'"
        print(bcolors.OKGREEN + pingstatus + bcolors.ENDC)
    else:
        pingstatus = "Cant get files but may be pinged'\n'"
        print(bcolors.WARNING + pingstatus + bcolors.ENDC)



f = open("host_list/simple_hosts.txt", "w")
f.write(new_content)
f.close()
os.system("rm index.html*")

try:
    with open("host_list/simple_hosts.txt") as file:
        lines = set(file.readlines())

    with open("host_list/simple_hosts.txt", 'w') as file:
        file.writelines(lines)

except IOError as e:
    print(e)

with open("host_list/simple_hosts.txt", "r") as lines:
    with open("info/basic_info.txt", "w") as w:
        for l in lines:
            out = Popen("host " + l, shell=True, stdout=PIPE, close_fds=True)
            w.write('\n' + out.stdout.read().decode("utf8"))
