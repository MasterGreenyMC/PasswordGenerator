###############################
##     by MasterGreenyMC     ##
## github.com/MasterGreenyMC ##
###############################


from color_code import color
from string import ascii_letters, punctuation, digits
from random import randint, choice
from sys import argv


def __init__():
    print(color("bold,light_green",
                "\n#################################\n## by MasterGreenyMC on GitHub ##\n##  "
                "github.com/MasterGreenyMC  ##\n#################################"))

    mode = input(color("bold,light_green", "\n[INPUT] ") + "Mode (random, words, exit): ").lower()
    while mode != "exit":
        if mode == "random":
            print(random())
        elif mode == "r":
            print(random())
        elif mode == argv[0]:
            print(random())
        elif mode == "words":
            print(words())
        elif mode == "w":
            print(words())
        elif mode == argv[0]:
            print(words())
        mode = input(color("bold,light_green", "\n[INPUT] ") + "Mode (random, words, exit): ").lower()


def random():
    pwl = input(color("bold,light_green", "\n[INPUT] ") + "Pw length: ")
    if pwl != "":
        while not pwl.isdigit():
            pwl = input(color("bold,light_green", "\n[INPUT] ") + "Pw length: ")

    pw = ""
    for i in range(int(pwl) - 1):
        pw += r(1)
    pw += r(1)

    return color("bold,light_green", "\n[OUTPUT] ") + pw


def words():
    load_files()

    pwl = input(color("bold,light_green", "\n[INPUT] ") + "Pw length (noun + digit/punctuation + adjective): ")
    if pwl != "":
        while not pwl.isdigit():
            pwl = input(color("bold,light_green", "\n[INPUT] ") + "Pw length (noun + digit/punctuation + adjective): ")

    pw = ""
    if pwl <= "1":
        pw += adjective() + r() + noun()
    elif pwl >= "1":
        for i in range(int(pwl) - 1):
            pw += adjective() + r() + noun() + r()
        pw += adjective() + r() + noun()

    return color("bold,light_green", "\n[OUTPUT] ") + pw


def load_files():
    global nouns
    global adjectives
    nouns = open("nouns.txt", "r").read().split("\n")
    adjectives = open("adjectives.txt", "r").read().split("\n")


def noun():
    return nouns[randint(0, len(nouns) - 1)]


def adjective():
    return adjectives[randint(0, len(adjectives) - 1)]


def r(times=randint(1, 4)):
    out = ""
    for var in range(times):
        out += choice([ascii_letters[randint(0, len(ascii_letters) - 1)],
                       digits[randint(0, len(digits) - 1)],
                       punctuation[randint(0, len(punctuation) - 1)]])
    return out


__init__()
