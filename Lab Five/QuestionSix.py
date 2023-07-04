#Question Six
n = int(input("Enter a Number: "))

def perfectcube(n):

    boolean = False
    limit = round(abs(n)**(1/3))
    for x in range(0,limit + 1):
      if  x**3 == abs(n) :
          boolean = True
      
    if boolean:
        print('Yes,',n,'is a perfect cube')
   
    else:
        print('No,',n,'is not a perfect cube')

    
perfectcube(n)