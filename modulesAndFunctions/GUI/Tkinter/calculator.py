import tkinter

mainWindow = tkinter.Tk()

mainWindow.title('Calculator')
mainWindow.geometry('480x480')
mainWindow['padx'] = 22
mainWindow['pady'] = 22

# Result box

result = tkinter.Entry(mainWindow)
result.grid(row=0, column=0, sticky='nsew', columnspan=4)

keys = [
    [('C', 1), ('CE', 1)],
    [('7', 1), ('8', 1), ('9', 1), ('+', 1)],
    [('4', 1), ('5', 1), ('6', 1), ('-', 1)],
    [('1', 1), ('2', 1), ('3', 1), ('+', 1)],
    [('0', 1), ('=', 2), ('/', 1)]
]

keyPad = tkinter.LabelFrame(mainWindow)
keyPad.grid(row=1, column=0, sticky='nsew')

row = 0
for keyRow in keys:
    col = 0
    for key in keyRow:
        tkinter.Button(keyPad, text=key[0]).grid(
            row=row, column=col, columnspan=key[1], sticky=tkinter.E + tkinter.W)
        col += key[1]
    row += 1

cancelButton = tkinter.Button(keyPad, text='Exit', command=mainWindow.destroy)
cancelButton.grid(row=6, column=0, columnspan=4, sticky='news')

mainWindow.update()
mainWindow.minsize(keyPad.winfo_width() + 22, result.winfo_height() + keyPad.winfo_height() + 22)
mainWindow.maxsize(keyPad.winfo_width() + 22 + 22, result.winfo_height() + keyPad.winfo_height() + 22 + 22)

mainWindow.mainloop()
