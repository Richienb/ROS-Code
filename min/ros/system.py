import subprocess
import os
import sys
import logging
import pkg_resources
import clipboard
from.roserrors import*
def getplatform():
 return sys.platform
def shellcommand(command):
 subprocess.call(str(command))
def pipupdate():
 packages=[d for d in pkg_resources.working_set]
 subprocess.call('pip install --upgrade '+' '.join(packages))
def dirtool(operation,directory):
 operation=operation.lower()
 if operation=='exists':
  return bool(os.path.exists(directory))
 if operation=='create':
  if os.path.exists(directory):
   raise RuntimeError('An Error Has Occured: Directory Already Exists (0007)')
  else:
   os.makedirs(directory)
 elif operation=='delete':
  if os.path.exists(directory):
   os.rmdir(directory)
  else:
   raise RuntimeError('An Error Has Occured: Directory Doesn\'t Exist (0009)')
 else:
  raise RuntimeError('An Error Has Occured: Invalid Operation Entered (0008)')
def file(operation,path):
 operation=operation.lower()
 if operation=='exists':
  return bool(os.path.isfile(path))
 if operation=='read':
  if os.path.isfile(path):
   with open(path,'r')as f:
    return[line.strip()for line in f]
  raise RuntimeError('An Error Has Occured: File Not Found (0012)')
 elif operation=='delete':
  if os.path.isfile(path):
   os.remove(path)
  else:
   raise RuntimeError('An Error Has Occured: File Not Found (0012)')
 elif operation=='create':
  if not file('exists',path):
   open(path,'w').close()
  else:
   raise RuntimeError('An Error Has Occured: File Already Exists (0013)')
 elif operation=='clear':
  if os.path.isfile(path):
   open(path,'w').close()
  raise RuntimeError('An Error Has Occured: File Not Found (0012)')
 else:
  raise RuntimeError('An Error Has Occured: Invalid Operation Entered (0008)')
def exitexecution(arguments=0):
 sys.exit(arguments)
def charlimit():
 return sys.maxsize
def unilimit():
 return sys.maxunicode
def pyversion(part=None):
 if part is None:
  return sys.version_info
 return sys.version_info[part]
def pyexec():
 return sys.executable
def pycopyright():
 return sys.copyright
def loglevel(leveltype=None,isequal=False):
 leveltype=leveltype.lower()
 loglevels={"none":0,"debug":10,"info":20,"warning":30,"error":40,"critical":50}
 if leveltype is None and isequal is False:
  return logging.getEffectiveLevel()
 if leveltype is not None and isequal is True:
  if leveltype in loglevels.values():
   return leveltype==logging.getEffectiveLevel()
  elif leveltype in loglevels:
   return loglevels[leveltype]==logging.getEffectiveLevel()
  else:
   raise WrongInput("Incorrect input provided. It should be none, debug, info, warning, error or critical")
 if leveltype in loglevels.values():
  logging.basicConfig(level=leveltype)
 elif leveltype in loglevels:
  logging.basicConfig(level=loglevels[leveltype])
 else:
  raise WrongInput("Incorrect input provided. It should be none, debug, info, warning, error or critical")
def logfile(targetfile="ros.log"):
 try:
  str(targetfile)
 except BaseException:
  raise ConversionError("Cannot convert type "+str(type(targetfile))+"to str")
 try:
  logging.basicConfig(filename=str(targetfile))
 except BaseException:
  raise WrongInput("Invalid target file specified")
def clipaction(action='get',text=None):
 if action=='get':
  return clipboard.paste()
 elif action=='set':
  clipboard.copy(str(text))
 elif action=='append':
  clipboard.copy(str(clipboard.paste)+str(text))
 elif action=='preceed':
  clipboard.copy(str(text)+str(clipboard.paste))
def text(operation,path,argument):
 operation=operation.lower()
 if operation=='write':
  if os.path.isfile(path):
   fh=open(path,'w')
   fh.write(argument)
  else:
   raise RuntimeError('An Error Has Occured: File Not Found (0012)')
 elif operation=='append':
  if os.path.isfile(path):
   fh=open(path,'a')
   fh.write(argument)
  else:
   raise RuntimeError('An Error Has Occured: File Not Found (0012)')
# Created by pyminifier (https://github.com/liftoff/pyminifier)
