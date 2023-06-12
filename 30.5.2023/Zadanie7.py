while True:
    try:
        name_file = input("How want you save your file-->  ")
        with open(f"{name_file}.txt") as plik:
            sentence = plik.readlines()
            print(sentence)

    except FileNotFoundError as error:
        print(error)