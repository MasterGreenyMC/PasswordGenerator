###############################
##     by MasterGreenyMC     ##
## github.com/MasterGreenyMC ##
###############################


def color(color="", word=""):
    global out
    out = ""

    color = color.split(",")
    for i in color:
        if i == "bold":
            out += "\33[1m"
        elif i == "italic":
            out += "\33[3m"
        elif i == "underlined":
            out += "\33[4m"

        elif i == "dark_black":
            out += "\33[38;5;0m"
        elif i == "dark_red":
            out += "\33[38;5;1m"
        elif i == "dark_green":
            out += "\33[38;5;2m"
        elif i == "dark_yellow":
            out += "\33[38;5;3m"
        elif i == "dark_blue":
            out += "\33[38;5;4m"
        elif i == "dark_magenta":
            out += "\33[38;5;5m"
        elif i == "dark_cyan":
            out += "\33[38;5;6m"
        elif i == "dark_white":
            out += "\33[38;5;7m"

        elif i == "light_black":
            out += "\33[38;5;8m"
        elif i == "light_red":
            out += "\33[38;5;9m"
        elif i == "light_green":
            out += "\33[38;5;10m"
        elif i == "light_yellow":
            out += "\33[38;5;11m"
        elif i == "light_blue":
            out += "\33[38;5;12m"
        elif i == "light_magenta":
            out += "\33[38;5;13m"
        elif i == "light_cyan":
            out += "\33[38;5;14m"
        elif i == "light_white":
            out += "\33[38;5;15m"

        elif i == "light_gray":
            out += "\33[38;5;252m"
        elif i == "dark_gray":
            out += "\33[38;5;245m"

    out += word + "\033[0m"

    return out