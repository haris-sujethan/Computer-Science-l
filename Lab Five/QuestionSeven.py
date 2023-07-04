#Question Seven
list=[]
numbers = int(input('Enter a Number '))
list+=[numbers]
while(numbers!=0):
    numbers=int(input('Enter a Number '))
    if numbers==0:
        break
    list+=[numbers]
    
        
def biggestOdd(n: list):

    print(n)
    for x in n:
        if abs(x)%2 ==1:
            max = x
            odd = True
            break;
            print(max)
        
    
            
    for y in n:
        if abs(y)%2 == 1:
            if abs(y)> abs(max):
                max = y
                


    elif odd=False:
        print('No Odd Numbers')
            
        
    else:
        print(max)
    
        
    
    
biggestOdd(list)
list1 = [-55, -33, -10, 100, -5, 0]
biggestOdd(list1)
