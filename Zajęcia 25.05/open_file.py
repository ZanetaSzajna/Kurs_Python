import os.path


def read_file(file):

    if not os.path.exists(file):
        print("plik nie istnieje")
        return None
    elif os.path.getsize(file) == 0:
        print("plik jest pusty")
        return None
    else:
        with open(file, "r", encoding="UTF-8") as f:
            content = f.read()
            return content

def write_file(file, content):
    if os.path.exists(file) and os.path.getsize(file) > 0:
        print("plik już istnieje i nie jest pusty")
        return None
    else:
        with open(file, "w", encoding="UTF-8") as f:
            f.write(content)
            print("Plik został zapisany")

