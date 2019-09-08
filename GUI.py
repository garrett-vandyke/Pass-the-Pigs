import tkinter as tk
import PassThePigs as ptp
import time

def showGUI():

    LARGE_FONT= ("Verdana", 12)

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
        
        def show_frame(self, cont):

            frame = self.frames[cont]
            frame.tkraise()
        
    class GamePage(tk.Frame):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            label = tk.Label(self, text="Pass the Pigs", font=LARGE_FONT)
            label.grid(row=0, columnspan=2, pady=10, padx=10)

            rollButton = tk.Button(self, text='Roll', command=self.rolling, bg='blue')
            rollButton.config(height=2, width=15, activebackground='blue')
            rollButton.grid(row=1, columnspan=2)
        
        def rolling(self):
            resultList = ptp.passThePigs()
            
            text1 = tk.Text(self, height=2, width=30)
            text2 = tk.Text(self, height=2, width=30)
            
            text1.grid(row=3, column=0)
            text2.grid(row=3, column=1)
            
            text1.insert(tk.END, resultList[0])
            text2.insert(tk.END, resultList[1])

    app = GUI()
    app.mainloop()

showGUI()