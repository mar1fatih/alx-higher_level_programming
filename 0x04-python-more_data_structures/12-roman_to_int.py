#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != type("") or roman_string is None:
        return 0
    s = 0
    i = 0
    while i < len(roman_string):
        if roman_string[i] == "I":
            v = i + 1
            if v < len(roman_string):
                if roman_string[v] == "V":
                    s += 4
                    i += 2
                elif roman_string[v] == "X":
                    s += 9
                    i += 2
                else:
                    s += 1
                    i += 1
            else:
                s += 5
                i += 1

         elif roman_string[i] == "V":
             s += 5
             i += 1
        elif roman_string[i] == "X":
            v = i + 1
            if v < len(roman_string):
                if roman_string[v] == "L":
                    s += 40
                    i += 2
                elif roman_string[v] == "C":
                    s += 90
                    i += 2
                else:
                    s += 10
                    i += 1
            else:
                s += 10
                i += 1
        elif roman_string[i] == "L":
            s += 50
            i += 1
        elif roman_string[i] == "C":
            v = i + 1
            if v < len(roman_string):
                if roman_string[v] == "D":
                    s += 400
                    i += 2
                elif roman_string[v] == "M":
                    s += 900
                    i += 2
                else:
                    s += 100
                    i += 1
            else:
                s += 100
                i += 1
        elif roman_string[i] == "D":
            s += 500
            i += 1
        elif roman_string[i] == "M":
            s += 1000
            i += 1
        else:
            return s
    return s
