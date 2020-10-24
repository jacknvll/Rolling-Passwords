# -*- coding: utf-8 -*-
import string
Die_D4 = list(range(1,5))
Die_D8 = ['[', ']', '\\', '<', '>', '+', '=', '_']
Die_D10 = list(string.digits)
Die_D16 = ['-', '/', ';', '.', ',', "'", ':', '(', ')', '$', '&', '@', '"', '?', '!']

Die_D30tmp, letters, numbers = list(), list(string.ascii_lowercase), range(30)
for n in numbers:
    Die_D30tmp.append(letters[n]) if len(Die_D30tmp) < 26 else Die_D30tmp.append("-")
Die_D30 = Die_D30tmp