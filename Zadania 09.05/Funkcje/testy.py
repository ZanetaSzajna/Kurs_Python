def my_mood(answer):
    print("My mood today: ")
    print(answer)

res = input("How are you ")

my_mood(res)

def my_mood2(answer):
    return  answer*2
res = input("How are you ")
twiced=my_mood2(res)
print("My mood is like ", twiced)