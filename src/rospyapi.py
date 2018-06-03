from os import system

def compilefile(filepath):
    system("compile.py " + str(filepath))
