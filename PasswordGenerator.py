###############################
##     by MasterGreenyMC     ##
## github.com/MasterGreenyMC ##
###############################

from color_code import color
from string import digits, punctuation, ascii_letters
from random import randint, choice


def __init__():
    print(color("bold,light_green",
                "\n#################################\n## by MasterGreenyMC on GitHub ##\n##  "
                "github.com/MasterGreenyMC  ##\n#################################"))

    mode = input(color("bold,light_green", "\n[INPUT] ") + "Mode (random, words, exit): ").lower()
    while mode != "exit":
        if mode == "random":
            print(random())
        elif mode == "words":
            print(words())
        mode = input(color("bold,light_green", "\n[INPUT] ") + "Mode (random, words, exit): ").lower()


def random():
    pwl = input(color("bold,light_green", "\n[INPUT] ") + "Pw length: ")
    if pwl != "":
        while not pwl.isdigit():
            pwl = input(color("bold,light_green", "\n[INPUT] ") + "Pw length: ")

    pw = ""
    for i in range(int(pwl) - 1):
        pw += choice([letters(), dp()])
    choice([letters(), dp()])

    return color("bold,light_green", "\n[OUTPUT] ") + pw


def words():
    load_files()

    pwl = input(color("bold,light_green", "\n[INPUT] ") + "Pw length (noun + digit/punctuation + adjective): ")
    if pwl != "":
        while not pwl.isdigit():
            pwl = input(color("bold,light_green", "\n[INPUT] ") + "Pw length (noun + digit/punctuation + adjective): ")

    pw = ""
    if pwl <= "1":
        pw += adjective() + dp() + noun()
    elif pwl >= "1":
        for i in range(int(pwl) - 1):
            pw += adjective() + dp() + noun() + dp()
        pw += adjective() + dp() + noun()

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


def dp(times=randint(1, 4)):
    out = ""
    for var in range(times):
        out += choice([digits[randint(0, len(digits) - 1)], punctuation[randint(0, len(punctuation) - 1)]])
    return out


def letters():
    return ascii_letters[randint(0, len(ascii_letters) - 1)]


__init__()
