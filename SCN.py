def cal(n, _scn, _ss, x, y, initial):
    count = 0
    for i in range (n):
        count += int(_scn[i]) & int(_ss[i])
    net = count* x - (n -count)*y
    final = initial + net
    return final
if __name__ == "__main__":
    n, r, x, y = raw_input("Type n, r, x, y:").split()
    _ss = raw_input("type your sequence array here").split()
    _scn =  raw_input("type your sequence here").split()
    final = cal(int(n), _scn, _ss, int(x), int(y), int(r))
    if final < int(r) :
        print "demoted"
    elif final > int(r):
        print "promoted"
    else :
        print "no change"
