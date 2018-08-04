from sys import argv as args
import os
from sys import exit as exitexc
from hashing import gethash
import subprocess
def executepyfile(filename):
 for i in enumerate(open(str(filename)).read().splitlines()):
  try:
   exec(i[1])
  except Exception as exc:
   print("ERROR: An error of type {0} occured while running line {1} because {2}".format(type(exc).__name__,str(value[0]+1),str(exc.args[0])))
   exitexc(1)
try:
 args[1]
except IndexError:
 print("ERROR: No ROS Code file provided in execution arguments")
 exitexc(1)
if not os.path.isfile(args[1]):
 print("ERROR: "+args[1]+" is not found.")
 exitexc(1)
if os.path.isfile("__roscache__/cache-"+gethash(args[1].split("\\")[-1].split("/")[-1])):
 execlist=["python","./__roscache__/cache-"+gethash(args[1].split("\\")[-1].split("/")[-1])]
 for i in range(2,len(args)):
  execlist.append(args[i])
if os.path.isdir("/home/el"):
 pass
# Created by pyminifier (https://github.com/liftoff/pyminifier)
