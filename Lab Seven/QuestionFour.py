#Question Four


import math
def occupy(n):
    nestStr = ""
    strBool=[]
    for x in range(0,n):
        nestStr += "_"
        strBool += [False]
    print(nestStr)
        
    while not all(strBool):
        nums = longestFalse(strBool)
        mid = math.ceil((nums[1]-nums[0])/2) + nums[0]
        nestStr = replace_str(nestStr, mid, "X")
        strBool[mid] = True
        print(nestStr)
    
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


def replace_str(string,index=0,replacement=''):
    return '%s%s%s'%(string[:index],replacement,string[index+1:])