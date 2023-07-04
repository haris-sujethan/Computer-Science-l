#Question Fifteen 

x = input("Enter a Number")

total = 0

i = 0

while i < len(x):
   if int(x[i]) % 2 != 0:
       total += int(x[i])
   i += 1

print(total)