from os import system


def compilefile(filepath):
    system("run-file.py " + str(filepath), shell=False)
