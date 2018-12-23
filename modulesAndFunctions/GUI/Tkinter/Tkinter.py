try:
    import tkinter
except ImportError:
    # for python 2 tkinter is Tkinter
    import Tkinter as tkinter

# print(tkinter.TkVersion)
# print(tkinter.TclVersion)

# tkinter._test()

# mainWindow = tkinter.Tk()
#
# mainWindow.title("hello world")
# mainWindow.geometry('720x480')
#
# label = tkinter.Label(mainWindow, text='hello world')
# label.pack(side='top')
#
# leftFrame = tkinter.Frame(mainWindow)
# leftFrame.pack(side='left', fill=tkinter.Y, expand=True)
#
# canvas = tkinter.Canvas(leftFrame, relief="raised", borderwidth= 1)
# canvas.pack(side="left", fill=tkinter.Y, expand= True)
# # canvas.pack(side='left')
#
# rightFrame = tkinter.Frame(mainWindow)
# rightFrame.pack(side='right', fill=tkinter.Y, expand=True)
#
# save = tkinter.Button(rightFrame, text='ok')
# dontSave = tkinter.Button(rightFrame, text="don't save and exit")
# cancel = tkinter.Button(rightFrame, text="cancel")
#
# save.pack(side='left', anchor='s')
# dontSave.pack(side='left', anchor='s')
# cancel.pack(side='left', anchor='s')
#
# mainWindow.mainloop()


#-------------------------------------------------------------------------------------


mainWindow = tkinter.Tk()

mainWindow.title("hello world")
mainWindow.geometry('720x480')

lable = tkinter.Label(mainWindow, text='hello world')
lable.grid(row=0, column=0)

leftFrame = tkinter.Frame(mainWindow)
leftFrame.grid(row=1, column=0)

canvas = tkinter.Canvas(leftFrame, relief="raised", borderwidth= 1)
canvas.grid(row=1, column=0)
# canvas.pack(side='left')

rightFrame = tkinter.Frame(mainWindow)
rightFrame.grid(row=1, column=1)

save = tkinter.Button(rightFrame, text='ok')
dontSave = tkinter.Button(rightFrame, text="don't save and exit")
cancel = tkinter.Button(rightFrame, text="cancel")

save.grid(row=2, column=0)
dontSave.grid(row=2, column=1)
cancel.grid(row=2, column=2)

mainWindow.mainloop()
