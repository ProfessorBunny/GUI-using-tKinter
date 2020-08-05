from tkinter import *

window = Tk()


def km_to_miles():
    result = float(e1_value.get())*1.6
    t1.insert(END, result)


b2 = Button(window, text='Execute', command=km_to_miles)
b2.grid(row=0, column=0)

e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

t1 = Text(window, height=1, width=10)
t1.grid(row=0, column=2)

window.mainloop()
