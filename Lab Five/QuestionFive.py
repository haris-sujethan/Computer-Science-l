#Question Five
n = int(input("Enter a Number: "))

def timestable(n):

    for m in range(1,n+1):
        for t in range(1,n+1):
            print(m*t, end="\t")
        print("\n") #\n creates new line 

timestable(n)