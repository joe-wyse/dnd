# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 22:12:24 2019

@author: Joseph
"""
import random

playerdict = {
        'Emily':14,
        'Colin':13,
        'Joe':9,
        'Joey':10,
        }

npcdict = {
        'npc1':0,
        'npc2':0,
        'npc3':3,
        }


def initroll(playername):
    return playerdict[playername]+random.randrange(1,20,1)

def npcinitroll(dex):
    return npcdict[dex]+random.randrange(1,20,1)


initdict={}

for name in list(playerdict):
    initdict[name] = initroll(name)
    
for npc in list(npcdict):
    initdict[npc] = npcinitroll(npc)


import operator
init_order = sorted(initdict.items(),key=operator.itemgetter(1), reverse=True)

for x in list(init_order):
    print(x)