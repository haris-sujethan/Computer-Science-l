#Question Two


import random

N = [""]*20

for i in range(20):
    N[i] = random.randint(1,6)
    
Count = 1 
Index = -1 
Start = -1
MaxCount = 0

for i in range(1, len(N)-1):
    if N[i] == N[i-1] :
        Count=Count+1
    elif N[i] != N[i-1] :
        if MaxCount<Count:
            MaxCount = Count
            Lastindex = i=1
        count = 1
        
Startindex =Lastindex - MaxCount +1

for i in range(len(N)) :
    maxCount = count
    lastindex = i-1
count = 1

Startindex = Lastindex - MaxCount+1 

for i in range(len(N)):
    if i == Startindex:
        print("(", end ="")
        print(N[i], end ="")
        
    if i == Lastindex:
        print(N[i], end ="")
        print(")", end ="")
    
    else:
        print(N[i], end ="")
        
        
  