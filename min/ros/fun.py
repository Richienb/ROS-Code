import random
def captcha():
 tryanswer=''
 numbervalues={'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10}
 numbertext=['one','two','three','four','five','six','seven','eight','nine','ten']
 if random.randint(1,2)==2:
  parta=random.choice(numbertext)
 else:
  parta=random.randint(1,10)
 if random.randint(1,2)==2:
  partb=random.choice(numbertext)
 else:
  partb=random.randint(1,10)
 tryanswer=input('CAPTCHA: What\'s '+str(parta)+' + '+str(partb)+'? Your Answer (In Digits): ')
 if not bool(isinstance(parta,int)):
  parta=numbervalues[parta]
 if not bool(isinstance(partb,int)):
  partb=numbervalues[partb]
 try:
  tryanswer=int(tryanswer)
 except BaseException:
  return False
 return parta+partb==tryanswer
def psrgame(choice):
 choice=choice.lower()
 choices={'paper':1,'papers':1,'scissor':2,'scissors':2,'rock':3,'rocks':3}
 pcchoice=random.randint(0,3)
 if pcchoice==choices[choice]:
  return 'Tie'
 elif pcchoice<choices[choice]:
  return 'Win'
 elif pcchoice>choices[choice]:
  return 'Loose'
def diceroll(dicecount=1,dicesize=6,alwayslist=False):
 dicecount=int(dicecount)
 if dicecount==1 and alwayslist is False:
  return random.randint(1,dicesize)
 resultlist=[]
 for _ in range(dicecount):
  resultlist.append(random.randint(1,dicesize))
 return resultlist
def yesnogame(includemaybe=False):
 if includemaybe is True:
  maxnum=3
 else:
  maxnum=2
 afternum=random.randint(1,maxnum)
 if afternum==1:
  return "Yes"
 elif afternum==2:
  return "No"
 return "Maybe"
def truthorliegame():
 truthnum=random.randint(1,4)
 if truthnum==1:
  return 'Truth'
 elif truthnum==2:
  return 'Maybe'
 elif truthnum==3:
  return 'Maybe'
 return 'Lie'
def face(facetype='smiley'):
 facetype=facetype.lower()
 if facetype=='smiley':
  print('😃')
 elif facetype=='straight':
  print('😐')
 elif facetype=='sad':
  print('☹')
# Created by pyminifier (https://github.com/liftoff/pyminifier)
