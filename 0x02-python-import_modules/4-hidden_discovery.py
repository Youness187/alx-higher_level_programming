#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    names = dir(hidden_4)
    for name in namess:
        if name[0:2] != "__":
            print(name)
