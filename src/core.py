from sys import *
import os

def open_file(filename):
    data = open(filename, "w").read()
    return data

def lex(filecontents):
    filecontents = list(filecontents)
    for chat in filecontents:
        tok = ''
        tok += char
        if tok == " ":
            tok = ""
        elif tok == "PRINT":
            print("FOUND A PRINT")
            tok = ''
        elif tok == "\"":
            if state == 0:
                state = 1

def run():
    data = open_file(argv[0])
    lex(data)

os.system("script2.py 1")
