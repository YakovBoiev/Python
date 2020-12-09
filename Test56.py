def counttreinhours():
    with open("text56.txt", "r", encoding="utf-8") as infile:
        less = {}
        for line in infile:
            str = line.split(":")
            less[str[0]] = sum(extrnumber(str[1]))
    print(less)

def extrnumber(string):
    listnumb = []
    numb = ""
    for char in string:
        if char.isdigit():
            numb += char
        else:
            if numb != "":
                listnumb.append(int(numb))
                numb = ""
    if numb != "":
        listnumb.append(int(numb))
    return listnumb

counttreinhours()