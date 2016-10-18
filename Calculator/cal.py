# -*- coding: UTF-8 -*-
import sys
from Tkinter import *

vyzva = u'Vlož počet kusů'

class App:

	def __init__(self, master):
	
		frame = Frame(master)
		frame.pack()
		
		self.label = Label(frame, text=vyzva)
		self.label.pack(side=TOP)
		
		self.kusy = Entry(pocet)
		
		self.konec = Button(frame, text=u'Ukonči kalkulačku', command=master.destroy)
		self.konec.pack(side=BOTTOM)
#


root = Tk()
app = App(root)
root.mainloop()




#tisk_vyzvy = Label(Moje_okno,text=vyzva)
#tisk_vyzvy.pack()
#Moje_okno.mainloop()



s = raw_input ()


try: 
	cislo=int(s)
	print cislo
except ValueError: 
	print (u'Příště vlož počet kusů')
	#print 'Try integer next time'
#






#app = Tkinter.Tk()
#app.mainloop()



