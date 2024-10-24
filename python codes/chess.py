s=input()
black="aceg"
white="bdfh"
if s[0]in black:
    if s[1] in "1357":
        print("black")
    else:
        print("white")
else:
    if s[1] in "1357":
        print("black")
    else:
        print("white")
        