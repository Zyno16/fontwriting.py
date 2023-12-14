import tkinter
from tkinter import ttk

form = tkinter.Tk()
form.geometry("700x500")

lbl1 = ttk.Label(form,text= "Label header")
lbl2 = ttk.Label(form ,text= "Label1")
lbl3 = ttk.Label(form,text= "Label2")
lbl1.config(background ="navy" ,foreground ="lightblue" ,font =("aurial",30))
lbl1.pack()
lbl2.pack()
lbl3.pack()
form.mainloop()

