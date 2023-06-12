dict_graf={
    "dom": ["kościół", "kino", "szkoła", "szpital", "teatr", "bar"],
    "kościół":["dom", "kino", "szkoła", "szpital", "teatr", "bar"],
    "kino":["kościół", "dom", "szkoła", "szpital", "teatr", "bar"],
    "szkoła":["kościół", "kino", "dom", "szpital", "teatr", "bar"],
    "szpital":["kościół", "kino", "szkoła", "dom", "teatr", "bar"],
    "teatr":["kościół", "kino", "szkoła", "szpital", "dom", "bar"],
    "bar":["kościół", "kino", "szkoła", "szpital", "teatr", "dom"]
}

print(dict_graf)
