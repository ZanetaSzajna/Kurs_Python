a,b,c = [5, 13, 2]
tmp = ''

if a>b:
    tmp=a
else:
    tmp=b
if c > tmp:
    print('Największa funkcja to ', c)
else:
    print("Największa to ", tmp)

def maximum_of(a, b, c):

    tmp1=''
    if a >b:
        tmp1=a
    else:
        tmp1=b
    if c>tmp1:
        return c
    else:
        return tmp1

def max_of_two(val1, val2):
    #return val1 if val1 > val2 else val2
    if val1 > val2:
        return val1
    else:
        return val2

def maximum_of_three(a,b,c):
    return max_of_two(c, max_of_two(a,b))

def main():
    x,y,z =[15,2,15]
    result=maximum_of_three(x,y,x)
    print(result)
main()