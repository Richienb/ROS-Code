from sys import argv as args
ver = str(args[1])
if "pre" in starting:
    ver = ver.split("e")[0] + "e" + str(int(ver.split("e")[1]) + 1)
else:
    ver = ver + "pre1"
print(ver)
