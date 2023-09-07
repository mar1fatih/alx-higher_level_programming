#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4 as hd
    for j in dir(hd):
        if j[:2] != "__":
            print(j)
