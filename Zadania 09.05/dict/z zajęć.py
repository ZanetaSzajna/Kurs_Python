grades = {}.fromkeys(['Math','English','Art'], 3)
print(grades)

k = 'Math'
for key, value in grades.items():
   print (key, value)
print( list(sorted(grades.keys())))
print (tuple(sorted(grades.keys())))
