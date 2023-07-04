#Question Ten
n = int(input("Enter a Number ")) 

def decimalToBinary(n):
    global binary # Global is visible throughout the program
    binary = []
    while n >=1 :   
        binary.append(n%2)
        n = n//2
        
    binary.reverse()
    print("The Binary Number is: ", binary) 

decimalToBinary(n)