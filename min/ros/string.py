def catwalk(text):
 return ' '.join(text.split())
def converttabs(text,spaces=4):
 return text.replace('\t',' '*spaces)
def shortentext(text,minlength,placeholder='...'):
 return textwrap.shorten(text,minlength,placeholder=str(placeholder))
def wraptext(text,maxlength):
 return textwrap.wrap(text,maxlength)
def unindent(text):
 return textwrap.dedent(text)
def paraspace(paragraphspaces=1):
 for _ in range(paragraphspaces):
  print('',end='\n')
def randomstr(valuelist):
 try:
  return random.choice(valuelist)
 except IndexError:
  raise RuntimeError('An Error Has Occured: List Not Specified (0018)')
# Created by pyminifier (https://github.com/liftoff/pyminifier)
