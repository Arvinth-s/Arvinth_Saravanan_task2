from time import sleep
def cal(n, _scn, _ss, x, y, initial):
    count = 0
    for i in range (n):
        count += int(_scn[i]) & int(_ss[i])
    net = count* x - (n -count)*y
    final = initial + net
    return final
if __name__ == "__main__":
    n, r, x, y = raw_input().split()
    _ss = raw_input().split()
    _scn =  raw_input().split()
    final = cal(int(n), _scn, _ss, int(x), int(y), int(r))
    if final < int(r) :
        print "demoted"
    elif final > int(r):
        print "promoted"
    else :
        print "no change"
    sleep(10)
    exit()
