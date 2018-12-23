import tkinter
import os

mainWindow = tkinter.Tk()

mainWindow.title("grid demo")
mainWindow.geometry('640x480-8-200')
mainWindow['padx'] = 8

label = tkinter.Label(mainWindow, text='tkinter grid demo')
label.grid(row=0, column=0, columnspan=3)

mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.columnconfigure(2, weight=3)
mainWindow.columnconfigure(3, weight=3)
mainWindow.columnconfigure(4, weight=3)

mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=10)
mainWindow.rowconfigure(2, weight=1)
mainWindow.rowconfigure(3, weight=3)
mainWindow.rowconfigure(4, weight=3)

listBox = tkinter.Listbox(mainWindow)
listBox.grid(row=1, column=0, sticky='news', rowspan=2)
listBox.config(border=2, relief='sunken')

for zone in os.listdir('/usr/bin'):
    listBox.insert(tkinter.END, zone)

listScroll = tkinter.Scrollbar(mainWindow, orient=tkinter.VERTICAL,
                               command=listBox.yview)
listScroll.grid(row=1, column=1, sticky='nws', rowspan=2)
listBox['yscrollcommand'] = listScroll.set

# Frame for radio buttons

optionFrame = tkinter.LabelFrame(mainWindow, text='File Details')
# The reason to use LabelFrame is it will create a border unlike Frame fn .
optionFrame.grid(row=1, column=2, sticky='ne')

rbValue = tkinter.IntVar()
rbValue.set(1)
# Set will set the default value . In this case it is 1 .

# Radio buttons
button1 = tkinter.Radiobutton(optionFrame, text='File Name', value=1, variable=rbValue)
button2 = tkinter.Radiobutton(optionFrame, text='Time Stamp', value=2, variable=rbValue)
button3 = tkinter.Radiobutton(optionFrame, text='Path', value=3, variable=rbValue)
button1.grid(row=0, column=0, sticky='w')
button2.grid(row=1, column=0, sticky='w')
button3.grid(row=2, column=0, sticky='w')

# Widget to display the result
resultLabel = tkinter.Label(mainWindow, text='Result')
resultLabel.grid(row=2, column=2, sticky='nw')
result = tkinter.Entry(mainWindow)
result.grid(row=2, column=2, sticky='sw')

# Frame for the time spinners .

timeFrame = tkinter.LabelFrame(mainWindow, text="Time")
timeFrame.grid(row=3, column=0, sticky='new')
# Time spinners
hourSpinner = tkinter.Spinbox(timeFrame, width=2, values=tuple(range(0, 24)))
minuteSpinner = tkinter.Spinbox(timeFrame, width=2, values=tuple(range(0, 60)))
secondSpinner = tkinter.Spinbox(timeFrame, width=2, from_=0, to=59)
# From and to is another way of assigning the values .
hourSpinner.grid(row=0, column=0)
tkinter.Label(timeFrame, text=':').grid(row=0, column=1)
minuteSpinner.grid(row=0, column=2)
tkinter.Label(timeFrame, text=':').grid(row=0, column=3)
secondSpinner.grid(row=0, column=4)
timeFrame['padx'] = 36
# Padding it to center with 36 from both sides .

# Frame for day spinners .

dateFrame = tkinter.LabelFrame(mainWindow)
dateFrame.grid(row=4, column=0, sticky='new')

# Day Labels .
dayLabel = tkinter.Label(dateFrame, text='Day')
monthLabel = tkinter.Label(dateFrame, text='Month')
yearLabel = tkinter.Label(dateFrame, text='Year')
dayLabel.grid(row=0, column=0, sticky='w')
monthLabel.grid(row=0, column=1, sticky='w')
yearLabel.grid(row=0, column=2, sticky='w')

# Day spinners .
daySpin = tkinter.Spinbox(dateFrame, width=10, values=tuple(range(0, 31)))
monthSpin = tkinter.Spinbox(dateFrame, width=10, values=('january', 'february', 'march',
                                                         'april', 'may', "june", 'july', 'august'
                                                         'september', 'october',
                                                         'november', 'december'))
yearSpin = tkinter.Spinbox(dateFrame, width=10, from_=1990, to=2018)
daySpin.grid(row=1, column=0)
monthSpin.grid(row=1, column=1)
yearSpin.grid(row=1, column=2)
dateFrame['padx'] = 22
# Padding date frame .

# Buttons .

okButton = tkinter.Button(mainWindow, text='ok')
cancelButton = tkinter.Button(mainWindow, text='cancel', command=mainWindow.destroy)
okButton.grid(row=4, column=3, sticky='e')
cancelButton.grid(row=4, column=4, sticky='w')
# okButton['padx'] = 22

mainWindow.mainloop()
