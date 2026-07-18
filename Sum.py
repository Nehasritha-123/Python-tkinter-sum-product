from tkinter import *
root = Tk()
root.title("Getting Started with Widgets")
root.geometry('400x400')

lbl = Label(text="This application calculates the sum.")
num1_entry = Entry()
num2_entry = Entry()

def calculate():
    n1 = int(num1_entry.get())
    n2 = int(num2_entry.get())
    total = n1 + n2
    
    text_box.delete("1.0", END) 
    text_box.insert(END, total)
text_box = Text(height=3)
btn = Button(text="Calculate Sum", command=calculate)

lbl.pack()
num1_entry.pack()
num2_entry.pack()
btn.pack()
text_box.pack()
root.mainloop()