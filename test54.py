def translnum():
    transl = {
        "One": "Один",
        "Two": "Два",
        "Three": "Три",
        "Four": "Четыре",
    }
    with open("text54inpt.txt", "r") as infile:
        with open("text54out.txt", "w") as outfile:
            for line in infile:
                str = line.split("-")
                print(f"{transl.get(str[0])}-{str[1]}", file=outfile)

translnum()





