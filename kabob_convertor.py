def main(string):
    return_ = ""
    for word in string.lower():
        if word == "ё":
            return_ += "e"
        elif word == "й":
            return_ += "u"
        elif word == "ц":
            return_ += "U,"
        elif word == "у":
            return_ += "y"
        elif word == "к":
            return_ += "K"
        elif word == "е":
            return_ += "e"
        elif word == "н":
            return_ += "H"
        elif word == "г":
            return_ += "r"
        elif word == "ш":
            return_ += "LLI"
        elif word == "щ":
            return_ += "LLI,"
        elif word == "з":
            return_ += "3"
        elif word == "х":
            return_ += "x"
        elif word == "ъ":
            return_ += "`b"
        elif word == "ф":
            return_ += "qp"
        elif word == "ы":
            return_ += "bl"
        elif word == "в":
            return_ += "B"
        elif word == "а":
            return_ += "a"
        elif word == "п":
            return_ += "I7"
        elif word == "р":
            return_ += "p"
        elif word == "о":
            return_ += "o"
        elif word == "л":
            return_ += "Jl"
        elif word == "д":
            return_ += "D"
        elif word == "ж":
            return_ += "}l{"
        elif word == "э":
            return_ += "e"
        elif word == "я":
            return_ += "9l"
        elif word == "ч":
            return_ += "4"
        elif word == "с":
            return_ += "c"
        elif word == "м":
            return_ += "M"
        elif word == "и":
            return_ += "u"
        elif word == "т":
            return_ += "T"
        elif word == "ь":
            return_ += "b"
        elif word == "б":
            return_ += "6"
        elif word == "ю":
            return_ += "I-0"
        else:
            return_ += word
    return return_

while 1:
    print(main(input("\n\n\n TEXT>>>")))
        

        

