sentence = input("Please enter a sentence --> ")
shift = int(input("Please enter the number of places to shift "))
encrypted =''
k=0
for letetr in sentence:
    print(letetr)
    letetr.islower()
    print(letetr.islower())
    if letetr.isupper() == True:
        k=k+1
    else:
        k=k
    print(k)