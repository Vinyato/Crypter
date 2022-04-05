import json
from Crypto.Util import number
import os
from tkinter import *
import cfg


def tkinter():
    # Creating GUI
    global entry_line, output_text
    window = Tk()
    window.title('Криптер')

    entry_tip = Label(text='Текст: ')
    entry_tip.grid(column=0, row=0)

    entry_line = Text(width=40, height=10)
    entry_line.grid(column=1, row=0, columnspan=3)

    encrypt_btn = Button(text='Шифровать', command=encrypt)
    encrypt_btn.grid(row=2, column=1, sticky=E)

    decrypt_btn = Button(text='Дешифровать', command=decrypt)
    decrypt_btn.grid(row=2, column=2, sticky=W)

    out_label = Label(text='Вывод дешифрованного сообщения: ')
    out_label.grid(row=4, column=0, sticky=E, columnspan=2)

    output_text = Label()
    output_text.grid(row=5, column=1, columnspan=3)

    window.mainloop()


def get_exponents(p=None, q=None):
    # Creating exponents
    if p is None and q is None:
        p = number.getPrime(64)
        q = number.getPrime(64)

    n = p * q
    phi = (p - 1) * (q - 1)
    e = 65537
    d = pow(e, -1, phi)

    return p, q, n, phi, e, d


def get_filename(path):
    listdir = os.listdir(path)
    maxNumber = 0

    if len(listdir) <= 0:
        return '1'

    else:
        for filename in listdir:
            number = filename.split('.')[0]
            number = number.split('_')[0]
            number = int(number)

            maxNumber = max(number, maxNumber)

    return str(maxNumber+1)


def hex_sum(s):
    sm = 0
    for i in s:
        a = hex(ord(i))
        for j in a:
            if j.isdigit():
                sm += int(j)
    return sm


def encrypt():
    # Getting random exponents
    p, q, n, phi, e, d = get_exponents()

    # Getting the input text
    text = entry_line.get('1.0', 'end-1c')

    if len(text) == 0:
        return

    # Getting the alphabet
    s = cfg.a

    # Loading logs
    with open('log.json', 'r') as f:
        file = json.load(f)

    result = []
    sub_result = ''
    for i in text:
        encoded_letter = str(pow(s.index(i), e, n))
        for j in encoded_letter:
            sub_result += chr(int(j)+100)
        else:
            result.append(sub_result)
            sub_result = ''
    print('=='.join(result).encode("utf-8").decode("utf-8"))
    file[hex_sum("==".join(result))] = ['=='.join(result), p, q]
    with open('log.json', 'w') as f:
        f.write(json.dumps(file))

    with open(f'Зашифрованные/{get_filename("Зашифрованные")}_ЗАШИФРОВАННЫЙ.txt', mode='w', encoding='utf-8') as output:
        output.write('=='.join(result))


def decrypt():
    global output_text
    with open('log.json', 'r') as f:
        file = json.load(f)

    text = entry_line.get('1.0', 'end-1c')
    if len(text) == 0:
        return

    s = cfg.a
    data = file[str(hex_sum(text))]
    cipher_text = data[0]
    p = data[1]
    q = data[2]

    p, q, n, phi, e, d = get_exponents(p, q)

    cipher_text = cipher_text.split('==')

    result = []
    for i in cipher_text:
        sub_result = ''
        for j in i:
            sub_result += str(ord(j)-100)

        else:
            result.append(s[pow(int(sub_result), d, n)])
            print(sub_result)

    print(''.join(result))
    output_text['text']=''.join(result)

if __name__ == '__main__':
    tkinter()
