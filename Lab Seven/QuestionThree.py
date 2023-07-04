#Question Three


def longestFalse(L):
    start=0
    curStart=0
    curEnd=0
    end=0
    length=0
    while curEnd != len(L) and curEnd < len(L):
        curEnd=curStart+1
        while curEnd<len(L) and not L[curEnd]:
            curEnd=curEnd+1
        if (curEnd-curStart)>length:
            length=curEnd-curStart
            start=curStart
            end=curEnd-1
        curStart=curEnd+1
    if start == 0 and end == 0:
        for x in range(0, len(L)):
            if L[x] == False:
                return x,x
    return start,end

print(longestFalse([False,False,True,False,False,False,False,True,True,False,False]))


