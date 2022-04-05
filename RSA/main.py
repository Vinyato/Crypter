import json
from Cryptodome.Util import number
import os
import string
import base64
from tkinter import *
from tkinter.scrolledtext import ScrolledText
import cfg


def tkinter():
    # Creating GUI
    global entry_line
    window = Tk()
    window.title('Криптер')

    entry_tip = Label(text='Текст: ')
    entry_tip.grid(column=0, row=0)

    entry_line = Text(width=40, height=10)
    entry_line.grid(column=1, row=0, columnspan=3)

    # p_label = Label(self.window, text='P: ')
    # p_label.grid(row=1, column=0)
    # p_entryLine = Entry(self.window, width=7)
    # p_entryLine.grid(row=1, column=1)
    # q_label = Label(self.window, text='Q: ')
    # q_label.grid(row=1, column=2)
    # q_entryLine = Entry(self.window, width=7)
    # q_entryLine.grid(row=1, column=3)

    encrypt_btn = Button(text='Шифровать', command=encrypt)
    encrypt_btn.grid(row=2, column=1, sticky=E)

    decrypt_btn = Button(text='Дешифровать', command=decrypt)
    decrypt_btn.grid(row=2, column=2, sticky=W)

    window.mainloop()


def get_exponents():
    # Creating exponents
    p = number.getPrime(64)
    q = number.getPrime(64)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 65537
    d = pow(e, -1, phi)

    return p, q, n, phi, e, d


def get_filename():
    listdir = os.listdir('files')
    maxNumber = 0

    if len(listdir) <= 0:
        return '1'

    else:
        for filename in listdir:
            number = int(filename.split('.')[0])
            maxNumber = max(number, maxNumber)

    return str(maxNumber)


def encrypt():
    p, q, n, phi, e, d = get_exponents()

    text = entry_line.get('1.0', 'end-1c')
    s = cfg.a
    with open('log.json', 'r') as f:
        file = json.load(f)

    result = []
    for i in text:
        result.append(str((pow(s.index(i), e, n))))

    file['_'.join(result)]=[p, q]
    with open('log.json', 'w') as f:
        f.write(json.dumps(file))


def decrypt():
    pass


if __name__ == '__main__':
    tkinter()
