"""
Utwórz listę zawierającą wartości poniższego słownika, bez duplikatów.
"""
days = {'Jan': 31, 'Feb': 28, 'Mar': 31, 'Apr': 30, 'May': 31, 'Jun': 30, 'Jul': 31, 'Aug': 31, 'Sept': 30}
values_list=list(days.values())
non_duplicate=[]
for day in values_list:
    if non_duplicate.count(day)== 0:
        non_duplicate.append(day)
print(non_duplicate)

