###############################
##     by MasterGreenyMC     ##
## github.com/MasterGreenyMC ##
###############################


from color_code import color
from string import ascii_letters, punctuation, digits
from random import randint, choice
from sys import argv


def __init__():
    print(color("bold,light_red",
                "\n#################################\n## by MasterGreenyMC on GitHub ##\n##  "
                "github.com/MasterGreenyMC  ##\n#################################"
                "\n\nCmd args: mode, pw length, execution times\n"))

    global mode
    mode = ""
    if len(argv) == 1:
        mode = input(color("bold,light_green", "\n[INPUT] ") + "Mode (random, words, exit): ").lower()
        while mode != "exit" and mode != "e":
            if mode == "random" or mode == "r":
                print(random() + "\n")
            elif mode == "words" or mode == "w":
                print(words() + "\n")
            if len(argv) == 1:
                mode = input(color("bold,light_green", "\n[INPUT] ") + "Mode (random, words, exit): ").lower()

    if len(argv) >= 2:
        if len(argv) == 4 and argv[3].isdigit():
            for i in range(int(argv[3])):
                if argv[1] == "random" or argv[1] == "r":
                    print(random())
                elif argv[1] == "words" or argv[1] == "w":
                    print(words())
            print("\n")
        else:
            if argv[1] == "random" or argv[1] == "r":
                print(random() + "\n")
            elif argv[1] == "words" or argv[1] == "w":
                print(words() + "\n")


def random():
    global pwl
    pwl = ""
    if len(argv) == 1:
        pwl = input(color("bold,light_green", "\n[INPUT] ") + "Pw length: ")
    elif len(argv) >= 3:
        pwl = argv[2]
    if pwl != "":
        while not pwl.isdigit() and len(argv) == 1:
            pwl = input(color("bold,light_green", "\n[INPUT] ") + "Pw length: ")

    pw = ""
    for i in range(int(pwl) - 1):
        pw += random_characters(1)
    pw += random_characters(1)

    return color("bold,light_green", "[OUTPUT] ") + pw


def words():
    load_files()

    global pwl
    pwl = ""
    if len(argv) < 3:
        pwl = input(color("bold,light_green", "\n[INPUT] ") + "Pw length: ")
    elif len(argv) >= 3:
        pwl = argv[2]
    if pwl != "":
        while not pwl.isdigit() and len(argv) == 1:
            pwl = input(color("bold,light_green", "\n[INPUT] ") + "Pw length: ")

    pw = ""
    if pwl <= "1":
        pw += adjective() + "_" + noun()
    elif pwl >= "1":
        for i in range(int(pwl) - 1):
            pw += adjective() + "_" + noun() + "" + random_characters() + ""
        pw += adjective() + "_" + noun()

    return color("bold,light_green", "[OUTPUT] ") + pw


def load_files():
    global nouns
    global adjectives
    nouns = open("nouns.txt", "r").read().split("\n")
    adjectives = open("adjectives.txt", "r").read().split("\n")


def noun():
    return nouns[randint(0, len(nouns) - 1)]


def adjective():
    return adjectives[randint(0, len(adjectives) - 1)]


def random_characters(times=randint(1, 4)):
    out = ""
    for var in range(times):
        out += choice([ascii_letters[randint(0, len(ascii_letters) - 1)],
                       digits[randint(0, len(digits) - 1)],
                       punctuation[randint(0, len(punctuation) - 1)]])
    return out


__init__()
