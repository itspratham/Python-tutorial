from tkinter import *


# import Tkinter


def event_close():
    exit()


class Windows(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("My GUI")
        self.pack(fill=BOTH, expand=1)

        quit_btn = Button(self, text="Quit", command=event_close)
        quit_btn.place(x=100, y=200)

        # Instance of menu bar


tk = Tk()
tk.geometry("800x600")
app = Windows(tk)
tk.mainloop()
