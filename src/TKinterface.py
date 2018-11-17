import tkinter # note that module name has changed from Tkinter in Python 2 to tkinter in Python 3
from tkinter import *
from PIL import Image, ImageTk

def donothing():
    filewin = Toplevel(root)
    button = Button(filewin, text="Do nothing button")
    button.pack()

class Window(Frame):
    # Define settings upon initialization. Here you can specify
    def __init__(self, master=None):

        # parameters that you want to send through the Frame class.
        Frame.__init__(self, master)

        #reference to the master widget, which is the tk window
        self.master = master

        #with that, we want to then run init_window, which doesn't yet exist
        self.init_window()

    #Creation of init_window
    def init_window(self):

        # changing the title of our master widget
        self.master.title("Lucas & Ronald")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

         # creating a menu instance
        menu = Menu(self.master)
        self.master.config(menu=menu)
        # create the file object)
        file = Menu(menu)
        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        file.add_command(label="Exit", command=self.client_exit)

        #added "file" to our menu
        menu.add_cascade(label="File", menu=file)


        # create the file object)
        edit = Menu(menu)

        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        edit.add_command(label="Show Img", command=self.showImg)
        edit.add_command(label="Show Text", command=self.showText)
        #added "file" to our menu
        menu.add_cascade(label="Edit", menu=edit)

        #added "file" to our menu
        menu.add_cascade(label="Edit", menu=edit)

    def showImg(self):
        load = Image.open("interface.png")
        render = ImageTk.PhotoImage(load)

        # labels can be text or images
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)
    def showText(self):
        text = Label(self, text="Hey there good lookin!")
        text.pack()

    def client_exit(self):
        exit()
