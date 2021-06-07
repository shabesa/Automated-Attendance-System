import csv
import tkinter
from tkinter.constants import BOTTOM, CENTER, DISABLED, LEFT, NORMAL, RIGHT, TOP
from card_reader import Reader

class CardUI:

    def __init__(self):
        pass

    def main(self):
        self.reader = Reader('COM7', 9600)
        main = tkinter.Tk()
        main.title('Card Mapper')
        main.geometry('320x140')
        main.resizable(False, False)
        
        
        def readCard():
            readButton['state'] = DISABLED
            while True:
                readCard.data = self.reader.read()
                # print(data)
                if(len(readCard.data) > 1):
                    readButton['state'] = NORMAL
                    UIDValLabel.config(text=f'{readCard.data}')
                    # print('done')
                    break

        def mapDetails():
            name = name_var.get()
            if len(name) > 1:
                with open('cards.csv', 'r+', newline="") as file:
                    writer = csv.writer(file)
                    dataList = file.readlines()
                    cardList=[]
                    for line in dataList:
                        entry = line.split(',')
                        cardList.append(entry[0])
                        print(cardList)
                    if name not in cardList:
                        file.writelines(f'\n{name},{readCard.data}')
                        name_var.set("")
                        UIDValLabel.config(text='')

        name_var = tkinter.StringVar()
        

        headingLabel = tkinter.Label(master=main, text='Map a Card to Student')
        headingLabel.place(relx=0.3, rely=0)

        nameLabel = tkinter.Label(master=main, text='Name: ')
        nameLabel.place(relx=0.05, rely=0.175)

        nameEntry = tkinter.Entry(master=main, textvariable=name_var, width=35)
        nameEntry.place(relx=0.2, rely=0.2)

        UIDLabel = tkinter.Label(master=main, text='UID:')
        UIDLabel.place(relx=0.048, rely=0.4)

        UIDValLabel = tkinter.Label(master=main, text=None)
        UIDValLabel.place(relx= 0.2, rely=0.4)

        readButton = tkinter.Button(master = main, text='Read Card', width=40, command=readCard)
        readButton.place(relx=0.048, rely=0.6)

        mapButton = tkinter.Button(master=main, text='MAP',width=40, command=mapDetails)
        mapButton.place(relx=0.048, rely=0.8)

        main.mainloop()

main = CardUI().main()