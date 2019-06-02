from time import sleep
print "________________________DECOMPOSING THE STRING______________________"
def decompose(n, _str, f):
    a, b=[], []
    x, y = "", ""
    _min=0
    uppercap=pow(2,n-f)
    num = deci(n, _str, f,)
    if num == uppercap -1 or num <= uppercap/2 :
        return -1,-1,-1
    else:
        lucky_num = 1000
        _min = min(uppercap - num, num - (uppercap/2))

        while _min <= 0:
            sleep(10)
        while lucky_num > _min:
            lucky_num =1
        n1 = num - lucky_num
        n2 = num + lucky_num
        a= binary(n, n1, n-first_num_alt(n1))
        b= binary(n, n2, n-first_num_alt(n2))
        if a==-1 or b==-1:
            return -1
        else:
            for i in a:
                x += str(i)
            for i in b:
                y += str(i)
            print x, "  ", y
            return 1, 1, num
        
def deci(n, _str, f):
    num=0
    for i in range (f, n):
        num += int(_str[i])*pow(2, n-1-i)   
    return num

def deci_list(n, _str, f):
    num=0
    for i in range (f, n):
        num += (_str[i])*pow(2, n-1-i)   
    return num
        
def binary(n, num, f):
    code=[]
    for o in range(f):
        code.append(0)
    while(num/2>0):
        code.append(num%2)
        num /=2
    code.append(num%2)
    for i in range(f,f+(n-f)/2):
        code[i], code[n-1-i+f] = code[n-i-1+f], code[i]
    if len(code) != n:
        return -1
    else:
        return (code)


def first_num(_str):
    f=0
    while(f < n and _str[f]==0):
        f+=1
    return f

def first_num_alt(n1):
    h=1
    while((n1)/pow(2,h)>0):
        h+=1
        
    return h

if __name__ == "__main__":     
            n = int(raw_input())
            _str = raw_input().rstrip()
            x, y, num =decompose(n, _str, 0,)
            if x==-1:
                print -1
            sleep(10)
            exit()
