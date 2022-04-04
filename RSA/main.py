from Crypto.Util import number
import os
import string
import base64
from tkinter import *
from tkinter.scrolledtext import ScrolledText
import cfg

class RSA:
    def __init__(self):
        # Creating exponents
        self.p = None
        self.q = None
        self.n = None
        self.phi = None
        self.e = None
        self.d = None

        # Creating GUI
        self.window = Tk()
        self.window.title('Криптер')


        entry_tip = Label(text='Текст: ')
        entry_tip.grid(column=0, row=0)

        self.entry_line = Text(width=40, height=10)
        self.entry_line.grid(column=1, row=0, columnspan=3)

       # p_label = Label(self.window, text='P: ')
       # p_label.grid(row=1, column=0)
       # p_entryLine = Entry(self.window, width=7)
       # p_entryLine.grid(row=1, column=1)
       # q_label = Label(self.window, text='Q: ')
       # q_label.grid(row=1, column=2)
       # q_entryLine = Entry(self.window, width=7)
       # q_entryLine.grid(row=1, column=3)

        self.encrypt_btn = Button(text='Шифровать', command=encrypt)
        self.encrypt_btn.grid(row=2, column=1, sticky=E)

        self.decrypt_btn = Button(text='Дешифровать', command=decrypt)
        self.decrypt_btn.grid(row=2, column=2, sticky=W)

        self.window.mainloop()

    def get_exponents(self):
        # Creating exponents
        self.p = number.getPrime(128)
        self.q = number.getPrime(128)
        self.n = self.p * self.q
        self.phi = (self.p - 1) * (self.q - 1)
        self.e = 65537
        self.d = pow(self.e, -1, self.phi)

    @staticmethod
    def get_filename():
        listdir = os.listdir('files')
        maxNumber = 0

        if len(listdir)<=0:
            return '1'

        else:
            for filename in listdir:
                number = int(filename.split('.')[0])
                maxNumber = max(number, maxNumber)

        return str(maxNumber)


def encrypt():
    global main
    main.get_exponents()
    text = main.entry_line.get('1.0', 'end-1c')
    s = cfg.a


    with open(f'files/log.txt', 'a') as f:
        f.write(f'{main.p}:{main.q}\n')
        for value in text:
            pass




def decrypt():
    global main






if __name__ == '__main__':
    main = RSA()

