#Question One


import random
List = [random.randrange(1, 7) for i in range(20)]
runs = []
inRun = False

run = ""

for i in range(len(List)):
    if inRun:
        if List[i] != List[i-1]:
            runs.append(run)
            
            
            run = ""
            inRun = False
            
        else:
            run += str(List[i])
            
    if inRun == False:
        if i != len(List)-1:
            if List[i] == List[i+1]:
                run += str(List[i])

                inRun = True


runs = sorted(runs, key=len)

output = ""

if (len(runs) > 0):
    output = output.join(str(x) for x in List)

    output = output.replace(runs[-1], "(" + runs[-1] + ")" , 1) 

print(output)