#Question Six

x = input("Enter a string : ")

def y(str):
    
    sum = 0
    for c in str:
        if c.isdigit() == True: #Python String isdigit() method is a built-in method used for string handling.
            sum += int(c)

    return sum

print(y(x))