from time import sleep
from itertools import combinations
print "________________________DECOMPOSING THE STRING______________________"
def decompose(n, _str, f, g):
    print "binary number:", _str
    a, b=[], []
    _min=0
    uppercap=pow(2,n-f)
    num = deci(n, _str, f, "num:")
    #print num
    if num == uppercap -1 or num <= uppercap/2 :
        return -1,-1,-1
    else:
        lucky_num = 1000
        _min = min(uppercap - num, num - (uppercap/2))

        while _min <= 0:
            sleep(10)
        while lucky_num > _min:
            if g==0:
                print "number of possible solutions is", _min-1, " say ur lucky number(the number should be between 1 and the possible solutions)"
                lucky_num = int(raw_input())
            else:
                lucky_num =1
            if lucky_num > _min :
                print "omg, the system is almost crashed! please read the instructions carefully"
        n1 = num - lucky_num
        n2 = num + lucky_num
        a= binary(n, n1, n-first_num_alt(n1))
        b= binary(n, n2, n-first_num_alt(n2))
        if a==-1 or b==-1:
            return 
        else:
            print " "
            print a, ' ----------', b,
            print " "
            return deci_list(n, a, f, "lower number:"), deci_list(n, b, f, "higher number"), num
            #print "want to continue (y/n)"
            #ch = raw_input()
            #if ch == 'n':
            #    exit()
        
        
        

def deci(n, _str, f, ch):
    num=0
    for i in range (f, n):
        num += int(_str[i])*pow(2, n-1-i)   
    print "the decimal value of  "+ch, num
    return num

def deci_list(n, _str, f, ch):
    num=0
    for i in range (f, n):
        num += (_str[i])*pow(2, n-1-i)   
    print "the decimal value of  "+ch, num
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
        print "OOPS, something went wrong. Pls give me another chance", "len code:", len(code)
        return -1
    else:
        return (code)

def bin_gen(n):
    tmp=[]
    m=[]
    k=[]
    count =-1
    #creating a n sized list containing 0
    #creating list with elements 0 to n-1 for combination
    for i in range(n):          
        tmp.append(i)
        k.append(0)
        
    c=[]
    #c contains the set of all combination
    for i in range(n+1):
        t=combinations(tmp, i)
        #for each loop c[i] contains the combinations in which i+1 elements contains 1
        c.append(list(t))
        #q contains one tuple at a time for each combination
        for q in c[i]:
            count+=1
            m.append(k[:])
            for j in (q):
                m[count][j]=1
    return m

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
    print "hello bro, tired/bored of entering the string input? Try automated input, which prints the input, output and whether they match"
    print "Want to try automated?(y/n)"
    choice=raw_input().rstrip()
    if choice == 'y':
        print 'Thank you for choosing this'
        n= int(raw_input("select the size of the array(<=22)"))
        #q=bin_gen(n)
        m= bin_gen(n)
        while True:
            print" "
            for i in range(len(m)):
                _str= [i for i in m[i]]
                f= first_num(_str)
                x, y, num = decompose(n, _str, f,-1)
                print (x+y)==2*num
                if x==-1:
                    print -1
                    print " "
                    print "------------------------------------------------"
                    continue
                if (x+y) != 2*num:
                    print "something went wrong, :("
                    print "please help me in debugging"
                    sleep(60)
                
            
                print " "
                print " "
                print " "
                print "----------------------------------------------------"
                sleep(10)
            print "All the possible combinations have been tested :), do you want to recheck?(y/n)"
            e=raw_input().rsptrip()
            if (e == 'n'):
                exit()
            
    else :
            print" "
            print "U can proceed"
            n = int(raw_input("length of string: "))
            _str = raw_input("string: ").rstrip()
            x, y, num =decompose(n, _str, 0, 0)
            print (x+y)==2*num
            if x==-1:
                print -1
            elif x==num:
                print 'same number'
            elif (x+y) != 2*num:
                print "something went wrong, :("
                sleep(60)
                print "please help me in debugging"
            sleep(2)
            print " "
            print " "
            print " "
            print "----------------------------------------------------"
