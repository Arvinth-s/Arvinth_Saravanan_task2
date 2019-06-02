'''
    Exponential binary search
    worst case:total number of queries: 39
    average number of queries for 1 to 1000000 is 36.902891

    Binary search:
    worst case: total  number of queries 20
    average number of queries for 1 to 1000000 is 19.951423
    '''
from  time import sleep
from sys import stdout

def bin_search():
    count =0
    mid = 500000
    l= 0
    r= 1000000
    while l< r and mid < r:
        x = raw_input(mid)
        stdout.flush()
        if x == ">=":
            l = mid
            count += 1
        else:
            r = mid
            count += 1
        mid = (r+l)/2
        if mid == l:
            print "!", mid
            stdout.flush()
            return count

if __name__ == "__main__":
    print "Welcome to the guess game, I hope you know the rules"
    stdout.flush()
    no_of_queries = bin_search()
    sleep(10)
    exit()
