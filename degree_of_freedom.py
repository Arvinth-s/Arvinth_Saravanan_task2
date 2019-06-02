#FEATURES OF SHELL SHORT HAVE BEEN IMPLEMENTED IN THE PROGRAM
def deg(n,_str):
    count=0
    bridge=n/2
    while bridge >0:
        for i in range (pow(2,count)):
            if (_str[2*i*bridge:(2*i+1)*bridge] !=_str[(2*i+1)*bridge:bridge*2*(i+1)] ) :
                print " Degree_of_freedom: ", count
                return count
        else:
            count+=1
            if (bridge % 2 ==0):
                bridge /= 2
            else:
                break
    print " Degree_of_freedom: ", count
    return count
    print "confusing"
    
if __name__ == "__main__":
    while(1):
        n=int(raw_input("The length of the string").rstrip())
        _str=raw_input("Type your array here").rstrip()
        count = deg(n, _str)
                
