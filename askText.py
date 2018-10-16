from tkinter import *

class askText:
    def __init__(self):
        self.master = Tk()
        self.master.title("Set prefix and suffix")
        self.master.geometry("200x80+600+300")
        self.master.iconbitmap('icon.ico')
        Label(self.master, text="Prefix Name").grid(row=1)
        Label(self.master, text="Suffix Name").grid(row=2)

        self.prefix = Entry(self.master) #predpona
        self.suffix = Entry(self.master) #pripona
        self.ret = []

        self.prefix.grid(row=1, column=2)
        self.suffix.grid(row=2, column=2)
        Button(self.master, text='Rename', command=self.send).grid(row=4, column=2, sticky=W, pady=4)
        mainloop()

    def send(self):
        self.ret.append(self.prefix.get())
        self.ret.append(self.suffix.get())
        self.master.quit()
