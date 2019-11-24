from tkinter import Tk
from GUI import Window

if __name__ == "__main__":
    #initializing the root which tkinter requires and running the app
    root = Tk()
    app = Window(root)
    app.set_win()
    app.mainloop()