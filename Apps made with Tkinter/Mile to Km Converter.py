from tkinter import *

def milestokm():
    miles = float(input.get())
    km = miles * 1.689
    kmresult.config(text=f"{km}")


#window object
window = Tk()
#window title
window.title("Mile to Km Converter")
#window size
window.minsize(width=250, height=100)
#padding is optional
window.config(padx=20,pady=20)
#input
input = Entry(width=10)
input.grid(column=1,row=0)
#
label = Label(text="Miles")
label.grid(column=2,row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0,row=1)

kmresult = Label(text="0")
kmresult.grid(column=1,row=1)

KmLabel = Label(text="Km")
KmLabel.grid(column=2,row=1)

calculatebutton = Button(text="Calculate", command=milestokm)
calculatebutton.grid(column=1,row=2)













window.mainloop()

