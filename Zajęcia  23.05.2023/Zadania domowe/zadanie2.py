import os

# nazwa ścieżki

path = os.getcwd()

# rozmiar pliku
size = os.path.getsize(path)
print("Size of my file: ", path, size)