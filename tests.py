from config import me


def read():
    print(me["name"])

    if "heigth" in me:
        print(me["heigth"])

def modify():
    me["age"] = 98
    print(me)

def create():
    me["preferred_color"] = "blue"
    print(me)


def remove():
    me["hobbies"].pop()
    print(me)


# call fns
read()
modify()
create()
remove()