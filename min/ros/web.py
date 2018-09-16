import webbrowser
import urllib
def mailto(to,cc,bcc,subject,body,autorun=True):
 mailurl='mailto:'+str(to)
 if cc is None and bcc is None and subject is None and body is None:
  if autorun is True:
   webbrowser.open_new_tab(str(mailurl))
  return str(mailurl)
 mailurl+='?'
 if cc is not None:
  mailurl+='cc='+str(cc)
  added=True
 added=False
 if bcc is not None:
  if added is True:
   mailurl+='&'
  mailurl+='bcc='+str(cc)
  added=True
 if subject is not None:
  if added is True:
   mailurl+='&'
  mailurl+='subject='+str(subject)
  added=True
 if body is not None:
  if added is True:
   mailurl+='&'
  mailurl+='body='+str(body)
  added=True
 if autorun is True:
  webbrowser.open_new_tab(str(mailurl))
 else:
  return mailurl
def openurl(url):
 try:
  webbrowser.open(url)
 except webbrowser.Error:
  raise RuntimeError('An Error Has Occured: Unable To Open URL (0017)')
def newwindow(url):
 try:
  webbrowser.open_new(url)
 except webbrowser.Error:
  raise RuntimeError('An Error Has Occured: Unable To Open URL (0017)')
def newtab(url):
 try:
  webbrowser.open_new_tab(url)
 except webbrowser.Error:
  raise RuntimeError('An Error Has Occured: Unable To Open URL (0017)')
def getbrowser():
 try:
  webbrowser.get(using=None)
 except BaseException:
  return None
def filedownload(source,destination):
 if not isempty(source):
  if not isempty(destination):
   try:
    urllib.request.urlretrieve(source,destination)
   except BaseException:
    raise RuntimeError('An Error Has Occured: File Download Error (0010)')
  else:
   raise RuntimeError('An Error Has Occured: Source Or Destination Invalid (0011)')
 else:
  raise RuntimeError('An Error Has Occured: Source Or Destination Invalid (0011)')
# Created by pyminifier (https://github.com/liftoff/pyminifier)
