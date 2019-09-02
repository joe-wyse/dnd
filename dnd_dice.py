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

roll_message = Message(window,text='Ready to roll')
roll_message.grid(column=2,row=1,rowspan=len(rolldict),sticky=N)

def roll_dice():
    usedict = {
    'd20':used20.get(),
    'd100':used100.get(),
    'd12':used12.get(),
    'd10':used10.get(),
    'd8':used8.get(),
    'd6a':used6a.get(),
    'd6b':used6b.get(),
    'd4':used4.get(),
    }

#    for x in usedict.keys():
#        if usedict[x] == 'True': usedict[x]=True
#        if usedict[x] == 'False': usedict[x]=False

    totalroll = 0
    message = ''
    for d in rolldict.keys():
        if bool(int(usedict[d]))==True:
            rolldict[d] = random.randrange(setdict[d][0],setdict[d][1],setdict[d][2])
            print(d + ' rolls '+ str(rolldict[d]))
            message = message+(d + ' rolls '+ str(rolldict[d])+'\n')
            totalroll = totalroll + rolldict[d]

    roll_result = message+('Total = ' + str(totalroll))
    roll_message.configure(text = roll_result)



d20 = Label(window, text='D20')
d20.grid(column=0,row=0)
used20 =IntVar()
d20button = Checkbutton(window, variable = used20)
#d20button['values'] = (True,False)
d20button.grid(column=1,row=0)


d100 = Label(window, text='D100')
d100.grid(column=0,row=1)
used100 = IntVar()
d100button = Checkbutton(window, variable = used100)
#d100button['values'] = (True,False)
d100button.grid(column=1,row=1)

d12 = Label(window, text='D12')
d12.grid(column=0,row=2)
used12 = IntVar()
d12button = Checkbutton(window, variable = used12)
#d12button['values'] = (True,False)
d12button.grid(column=1,row=2)

d10 = Label(window, text='D10')
d10.grid(column=0,row=3)
used10 = IntVar()
d10button = Checkbutton(window, variable = used10)
#d10button['values'] = (True,False)
d10button.grid(column=1,row=3)

d8 = Label(window, text='D8')
d8.grid(column=0,row=4)
used8 = IntVar()
d8button = Checkbutton(window, variable = used8)
#d8button['values'] = (True,False)
d8button.grid(column=1,row=4)

d6a = Label(window, text='D6a')
d6a.grid(column=0,row=5)
used6a = IntVar()
d6abutton = Checkbutton(window, variable = used6a)
#d6abutton['values'] = (True,False)
d6abutton.grid(column=1,row=5)

d6b = Label(window, text='D6b')
d6b.grid(column=0,row=6)
used6b = IntVar()
d6bbutton = Checkbutton(window, variable = used6b)
#d6bbutton['values'] = (True,False)
d6bbutton.grid(column=1,row=6)

d4 = Label(window, text='D4')
d4.grid(column=0,row=7)
used4 = IntVar()
d4button = Checkbutton(window, variable = used4)
#d4button['values'] = (True,False)
d4button.grid(column=1,row=7)


window.geometry('350x200')




btn = Button(window, text = "Roll", command=roll_dice)
btn.grid(column=2,row=0)

window.mainloop()