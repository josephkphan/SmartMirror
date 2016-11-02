from Tkinter import *

root = Tk()

#A frame is like creation sections
#if you had 2 frames you can put stuff in the top frame or bottom frame
#it is generally sued to help with layout
topFrame = Frame(root)
topFrame.pack()

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)	#parameter in bottom frame add in where to display

button1 = Button(topFrame, text="Button 1", fg="red")	#parameters Frame,Text displayed, color
buttona = Button(topFrame, text="should be on the right of button 1", fg="blue")
button2 = Button(bottomFrame, text="test", fg = "green")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
buttona.pack(side=LEFT)
#packing happens on top of each other unless specified like side=LEFT which means
#pack it as far left as you can
#frames divided will always be on top of each other.
root.mainloop()