# -*- coding: utf-8 -*-
"""
DnD dice
"""


import random

#You can also set them equal to 1 or 0
usedict = {
    'd20':True,
    'd100':True,
    'd12':True,
    'd10':True,
    'd8':True,
    'd6a':True,
    'd6b':True,
    'd4':True,
    }

rolldict = {
    'd20':0,
    'd100':0,
    'd12':0,
    'd10':0,
    'd8':0,
    'd6a':0,
    'd6b':0,
    'd4':0,
    }

setdict = {
        'd20':(1,20,1),
        'd100':(10,100,10),
        'd12':(1,12,1),
        'd10':(1,10,1),
        'd8':(1,8,1),
        'd6a':(1,6,1),
        'd6b':(1,6,1),
        'd4':(1,4,1),
        }


'''
rolldict['d20'] = random.randrange(1,20,1)*int(usedict['d20'])
rolldict['d100'] = random.randrange(10,100,10)*int(usedict['d100'])
rolldict['d12'] = random.randrange(1,12,1)*int(usedict['d12'])
rolldict['d10'] = random.randrange(1,10,1)*int(usedict['d10'])
rolldict['d8'] = random.randrange(1,8,1)*int(usedict['d8'])
rolldict['d6a'] = random.randrange(1,6,1)*int(usedict['d6a'])
rolldict['d6b'] = random.randrange(1,6,1)*int(usedict['d6b'])
rolldict['d4'] = random.randrange(1,4,1)*int(usedict['d4'])
'''

#totalroll = d20roll+d100roll+d12roll+d10roll+d8roll+d6aroll+d6broll+d4roll

totalroll = 0

for d in rolldict.keys():
    if bool(usedict[d])==True:
        rolldict[d] = random.randrange(setdict[d][0],setdict[d][1],setdict[d][2])
        print(d + ' rolls '+ str(rolldict[d]))
        totalroll = totalroll + rolldict[d]

print('Total = ' + str(totalroll))
