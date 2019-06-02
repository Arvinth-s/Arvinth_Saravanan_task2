#FEATURES OF SHELL SHORT HAVE BEEN IMPLEMENTED IN THE PROGRAM
from time import sleep
def deg(n,_str):
    count=0
    bridge=n/2
    while bridge >0:
        for i in range (pow(2,count)):
            if (_str[2*i*bridge:(2*i+1)*bridge] !=_str[(2*i+1)*bridge:bridge*2*(i+1)] ) :
                print  count
                return count
        else:
            count+=1
            if (bridge % 2 ==0):
                bridge /= 2
            else:
                break
    print  count
    return count
    
if __name__ == "__main__":
        n=int(raw_input().rstrip())
        _str=raw_input().rstrip()
        count = deg(n, _str)
        sleep(10)
        exit()
                
