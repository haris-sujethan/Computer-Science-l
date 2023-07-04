#Question Nine
x = int(input("Enter a Number "))

epsilon = float(input("Enter a Number "))
 
def squareRoot(x, epsilon):
    
     epsilonX2 = epsilon**2
     
     Guess = 0
     
     answer = 0.0
     
     while abs(answer**2 - x) >= epsilon and answer<=x:
         answer += epsilonX2
     Guess += 1
    
     if abs(answer**2 - x) >= epsilon:
         print('Failed')
         
     else:
         print(str(answer),' is close to the square root of ',str(x))

squareRoot(x, epsilon)