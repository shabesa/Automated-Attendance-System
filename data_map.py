from datetime import datetime
import os
import tkinter
import matplotlib.pyplot as pl
import pandas as pd
import numpy as np

class DataMapper:

    def __init__(self):
        self.now = datetime.now()
        self.fileName = self.now.strftime('%d-%m-%Y')
        self.month = self.now.strftime('%B')
        self.dir = f'attendance/{self.month}'
        self.csvList = os.listdir(self.dir)
        print(self.csvList)
        self.splitList = []
        for i in self.csvList:
            entry = i.split('.')
            self.splitList.append(entry[0])
        print(self.splitList)

    def read(self):
        self.dataList = []
        for file in self.csvList:
            self.df = pd.read_csv(f'attendance/{self.month}/{file}')
            print(len(self.df.index))
            self.dataList.append(len(self.df.index))
        
        numRange = range(1, len(self.dataList)+1)
        self.numList = list(numRange)
        
        # print(self.dataList)
        print(self.numList)
        
    def graphUI(self):
        graphTypes = ['line', 'bar', 'pie']

        graphPage = tkinter.Tk()
        graphPage.geometry("600x300")
        graphPage.title('Automated Attendance System')
        graphPage.resizable(False, False)

        headLabel = tkinter.Label(master=graphPage, text="Data Grapher", width=30)
        headLabel.place(relx=0.3, rely=0.05)

        typeLabel = tkinter.Label(master=graphPage, text='Graph Type: ', width=10)
        typeLabel.place(relx=0.135, rely=0.2)

        def select():
            print(var.get())
            selection = "You selected the " + graphTypes[var.get()] + " graph"
            statusLabel.config(text = selection)

        def plotCommand():
            self.read()
            if var.get() == 0:
                pl.plot(self.splitList, self.dataList)
            elif var.get() == 1:
                pl.bar(self.splitList, self.dataList)
            elif var.get() == 2:
                pl.pie(self.dataList, labels=self.splitList, autopct='%1.1f%%')
            pl.show()


        var = tkinter.IntVar()

        Rad1 = tkinter.Radiobutton(master=graphPage, text=f'{graphTypes[0]}', variable=var, value=0, command=select)
        Rad1.place(relx=0.135, rely=0.3)

        Rad2 = tkinter.Radiobutton(master=graphPage, text=f'{graphTypes[1]}', variable=var, value=1, command=select)
        Rad2.place(relx=0.135, rely=0.4)

        Rad3 = tkinter.Radiobutton(master=graphPage, text=f'{graphTypes[2]}', variable=var, value=2, command=select)
        Rad3.place(relx=0.135, rely=0.5)


        statusLabel = tkinter.Label(master=graphPage, text="You selected the " + graphTypes[var.get()] + " graph")
        statusLabel.place(relx=0.135, rely=0.6)
        
        plotButton = tkinter.Button(master=graphPage, text='Plot', command=plotCommand, width=30)
        plotButton.place(relx=0.3, rely=0.675)

        graphPage.mainloop()

DataMapper().graphUI()