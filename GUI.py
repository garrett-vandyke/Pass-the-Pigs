import tkinter as tk
import PassThePigs as ptp
from PIL import ImageTk, Image

LARGE_FONT = ("Verdana", 24, 'bold')

class GUI(tk.Tk):

    def __init__(self, *args, **kwargs):            

        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # dictionary to hold frames
        self.frames = {}
        for F in (WelcomePage, GamePage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame('WelcomePage')
        self.title('Pass the Pigs')

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

class WelcomePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        welcomeMessage = tk.Label(self, text='Welcome to Pass the Pigs!', font=LARGE_FONT)
        welcomeMessage.grid(row=0, columnspan=2, pady=10, padx=10)

        detailMessage = tk.Label(self, text = 'A game created just for you by Matthew Devine, Garrett Van Dyke, and their brilliant friends.\nTuck your shirt in, and get ready to roll.', font='Times')
        detailMessage.grid(row=1, columnspan=2, pady=10, padx=10)

        enterButton = tk.Button(self, text='Play', command=lambda: controller.show_frame("GamePage"))
        enterButton.config(height=2, width=15, activebackground='blue')
        enterButton.grid(row=2, columnspan=2, pady=10)

class GamePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Pass the Pigs', font=LARGE_FONT)
        label.grid(row=0, columnspan=2, pady=10, padx=10)

        rollButton = tk.Button(self, text='Roll', command=self.rolling)
        rollButton.config(height=2, width=15, activebackground='blue')
        rollButton.grid(row=1, columnspan=2)

        self.numRolls = 1
    
    def rolling(self):
        # dictionary of punishments
        punishmentDict = {('Leaning Jowler', 'Leaning Jowler'):'Middle name of firstborn', ('Leaning Jowler','Snouter'):"Next pet's name", ('Leaning Jowler','Trotter'):'Tattoo', ('Leaning Jowler','Razorback'):'Lip tattoo', ('Leaning Jowler','Sider'):'Super dare', ('Snouter','Snouter'):'Winner!',('Snouter','Trotter'):'Dye hair', ('Snouter','Razorback'):'Jump in pool', ('Snouter','Sider'):'Dare',('Trotter','Trotter'):'Spin the bottle',('Trotter','Razorback'):'Shot/Shotgun',('Trotter','Sider'):'Choose a chooser 5 sec.',('Razorback','Razorback'):'Drink a full (alone)',('Razorback','Sider'):'Notecard (veto finish)',('Sider','Sider'):'Drink every roll until new double sider'}
        
        # get results
        resultList = ptp.passThePigs()
        
        # activate and populate text widgets
        text1 = tk.Text(self, height=2, width=30)
        text2 = tk.Text(self, height=2, width=30)
        rollWidget = tk.Text(self, height=2, width=30)
        punishmentWidget = tk.Text(self, height=2, width=60)

        text1.grid(row=5, column=0)
        text2.grid(row=5, column=1)
        rollWidget.grid(row=3, columnspan=2)
        punishmentWidget.grid(row=4, columnspan=2)

        text1.tag_configure('center', justify='center')
        text2.tag_configure('center', justify='center')
        rollWidget.tag_configure('center', justify='center')
        punishmentWidget.tag_configure('center', justify='center')

        text1.insert(tk.END, resultList[0], 'center')
        text2.insert(tk.END, resultList[1], 'center')
        rollWidget.insert(tk.END, 'Roll ' + str(self.numRolls), 'center')

        # find the correct punishment to display
        for key, value in punishmentDict.items():
            if sorted(key) == sorted(resultList):
                punishmentWidget.insert(tk.END, value, 'center')

        # activate and populate picture widgets
        imageCanvas1 = tk.Canvas(self, width = 70, height=100)
        imageCanvas2 = tk.Canvas(self, width = 70, height=100)

        imageCanvas1.grid(row=6, column=0)
        imageCanvas2.grid(row=6, column=1)

        self.image1 = ImageTk.PhotoImage(Image.open(resultList[0].lower().replace(' ','') + '.gif'))
        imageCanvas1.create_image(20, 20, anchor='nw', image=self.image1)

        self.image2 = ImageTk.PhotoImage(Image.open(resultList[1].lower().replace(' ','') + '.gif'))
        imageCanvas2.create_image(20, 20, anchor='nw', image=self.image2)
        
        # roll counter
        self.numRolls += 1
        
app = GUI()
app.mainloop()