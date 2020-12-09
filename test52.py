def strwordcount():
    with open("text52.txt", "r") as inpf:
        text = inpf.readlines()
        print(f"Количество строк в файле - {len(text)}")
        for i, str  in enumerate(text, 1):
            word = str.split()
            print(f"В {i} строке - {len(word)} слов")


strwordcount()
