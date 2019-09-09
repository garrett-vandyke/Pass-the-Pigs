import tkinter as tk
import PassThePigs as ptp
import time
from PIL import ImageTk, Image

def showGUI():

    LARGE_FONT = ("Verdana", 24, 'bold')

    class GUI(tk.Tk):

        def __init__(self, *args, **kwargs):

            tk.Tk.__init__(self, *args, **kwargs)

            container = tk.Frame(self)
            container.pack(side="top", fill="both", expand=True)
            container.grid_rowconfigure(0, weight=1)
            container.grid_columnconfigure(0, weight=1)

            self.frames = {}

            frame = GamePage(container, self)
            self.frames[GamePage] = frame
            frame.grid(row=0, column=0, sticky="nsew")

            self.show_frame(GamePage)
            self.title('Pass the Pigs')
        
        def show_frame(self, cont):

            frame = self.frames[cont]
            frame.tkraise()
        
    class GamePage(tk.Frame):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            label = tk.Label(self, text='Pass the Pigs', font=LARGE_FONT)
            label.grid(row=0, columnspan=2, pady=10, padx=10)

            rollButton = tk.Button(self, text='Roll', command=self.rolling, bg='blue')
            rollButton.config(height=2, width=15, activebackground='blue')
            rollButton.grid(row=1, columnspan=2)

            self.numRolls = 1
        
        def rolling(self):
            resultList = ptp.passThePigs()
            
            text1 = tk.Text(self, height=2, width=30)
            text2 = tk.Text(self, height=2, width=30)
            rollWidget = tk.Text(self, height=2, width=30)

            text1.grid(row=4, column=0)
            text2.grid(row=4, column=1)
            rollWidget.grid(row=3, columnspan=2)

            text1.tag_configure('center', justify='center')
            text2.tag_configure('center', justify='center')
            rollWidget.tag_configure('center', justify='center')

            text1.insert(tk.END, resultList[0], 'center')
            text2.insert(tk.END, resultList[1], 'center')
            rollWidget.insert(tk.END, 'Roll ' + str(self.numRolls), 'center')

            imageCanvas1 = tk.Canvas(self, width = 70, height=100)
            imageCanvas2 = tk.Canvas(self, width = 70, height=100)

            imageCanvas1.grid(row=5, column=0)
            imageCanvas2.grid(row=5, column=1)

            self.image1 = ImageTk.PhotoImage(Image.open(resultList[0].lower().replace(' ','') + '.gif'))
            imageCanvas1.create_image(20, 20, anchor='nw', image=self.image1)

            self.image2 = ImageTk.PhotoImage(Image.open(resultList[1].lower().replace(' ','') + '.gif'))
            imageCanvas2.create_image(20, 20, anchor='nw', image=self.image2)

            self.numRolls += 1
            
    app = GUI()
    app.mainloop()

showGUI()