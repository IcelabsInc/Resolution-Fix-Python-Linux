import subprocess
import os
import re


resolutionGetCommmand = subprocess.run(["cvt", "1280", "1024"], capture_output = True).stdout.decode()

resGetCommand = str(resolutionGetCommmand).split("\"")

resolution = ""

resolutionFullData = "\""
resolutionFullData += resGetCommand[1]
resolutionFullData += "\""

resolution = resolutionFullData

resolutionFullData += str(resGetCommand[2]).split("\n")[0]

newModeCommand = "xrandr --newmode "
newModeCommand += resolutionFullData

displayNameOutput = subprocess.run(["xrandr"], capture_output = True).stdout.decode()

datas1 = str(displayNameOutput).split("\n")

displayName = ""

for lines in datas1:
    if re.findall(" connected", lines).__len__() > 0:
        d = lines.split(" ")
        displayName = d[0]
        break

os.system(newModeCommand)
os.system("xrandr --addmode " + displayName + " " + resolution)
os.system("xrandr -s " + resolution)
