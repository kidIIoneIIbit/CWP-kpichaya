text = input()

if text != "":
    print("none")
else:
    i = 0
    while i <= 10:
        line = "Table de " + str(i) + ": "
        j = 0
        while j <= 10:
            line = line + str(i * j)
            if j != 10:
                line = line + " "
            j = j + 1
        print(line)
        i = i + 1