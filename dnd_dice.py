# -*- coding: utf-8 -*-
"""
DnD dice
"""


import random
from tkinter import *
from tkinter.ttk import *

#return all the dice to zero - probably not necessary
#might be better to return the dict to empty, except other functions
#reference this dict's keys
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

#settings for the random function
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

window = Tk()
 
window.title("Dice")

roll_label = Label(window,text='Ready to roll')
roll_label.grid(column=2,row=1)

def roll_dice():
    usedict = {
    'd20':d20combo.get(),
    'd100':d100combo.get(),
    'd12':d12combo.get(),
    'd10':d10combo.get(),
    'd8':d8combo.get(),
    'd6a':d6acombo.get(),
    'd6b':d6bcombo.get(),
    'd4':d4combo.get(),
    }

    for x in usedict.keys():
        if usedict[x] == 'True': usedict[x]=True
        if usedict[x] == 'False': usedict[x]=False

    totalroll = 0
    for d in rolldict.keys():
        if bool(usedict[d])==True:
            rolldict[d] = random.randrange(setdict[d][0],setdict[d][1],setdict[d][2])
            print(d + ' rolls '+ str(rolldict[d]))
            totalroll = totalroll + rolldict[d]

    roll_result = ('Total = ' + str(totalroll))
    roll_label.configure(text = roll_result)



d20 = Label(window, text='D20')
d20.grid(column=0,row=0)
d20combo = Combobox(window)
d20combo['values'] = (True,False)
d20combo.grid(column=1,row=0)
d20combo.current(1)

d100 = Label(window, text='D100')
d100.grid(column=0,row=1)
d100combo = Combobox(window)
d100combo['values'] = (True,False)
d100combo.grid(column=1,row=1)
d100combo.current(1)

d12 = Label(window, text='D12')
d12.grid(column=0,row=2)
d12combo = Combobox(window)
d12combo['values'] = (True,False)
d12combo.grid(column=1,row=2)
d12combo.current(1)

d10 = Label(window, text='D10')
d10.grid(column=0,row=3)
d10combo = Combobox(window)
d10combo['values'] = (True,False)
d10combo.grid(column=1,row=3)
d10combo.current(1)

d8 = Label(window, text='D8')
d8.grid(column=0,row=4)
d8combo = Combobox(window)
d8combo['values'] = (True,False)
d8combo.grid(column=1,row=4)
d8combo.current(1)

d6a = Label(window, text='D6a')
d6a.grid(column=0,row=5)
d6acombo = Combobox(window)
d6acombo['values'] = (True,False)
d6acombo.grid(column=1,row=5)
d6acombo.current(1)

d6b = Label(window, text='D6b')
d6b.grid(column=0,row=6)
d6bcombo = Combobox(window)
d6bcombo['values'] = (True,False)
d6bcombo.grid(column=1,row=6)
d6bcombo.current(1)

d4 = Label(window, text='D4')
d4.grid(column=0,row=7)
d4combo = Combobox(window)
d4combo['values'] = (True,False)
d4combo.grid(column=1,row=7)
d4combo.current(1)


window.geometry('350x200')




btn = Button(window, text = "Roll", command=roll_dice)
btn.grid(column=2,row=0)

window.mainloop()