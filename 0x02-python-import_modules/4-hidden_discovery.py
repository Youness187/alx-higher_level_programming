#!/usr/bin/python3
if __name__ == "__main__":
    import hidden

    files = dir(hidden)
    for f in files:
        if f[0:2] != "__":
            print(f)
