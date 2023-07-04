num = int(input("Enter an integer: "))
pwr = 2
root = 0 
numList = [] 
found = False
if num < 0:
    neg = True
else:
    neg = False
while pwr < 6:
    while abs(root**pwr) <= abs(num):
        if root**pwr == num:
            numList += [[root, pwr]]
            found = True
        if abs(root) > abs(num):
            root = 0
        elif neg:
            root -= 1
        else:
            root +=1
    pwr += 1
    root = 0
    
print(numList)
if not found:
    print("No pair of integers, 'root' and 'pwr', exists such that 1 < pwr < 6 and root**pwr = " + str(num))
else:
    lowNum = numList[0]
    for x in range(0,len(numList)):
        if lowNum[0] > numList[x][0]:
            lowNum = numList[x]
    print(str(lowNum[0]) + "**" + str(lowNum[1]) + " = " + str(num))