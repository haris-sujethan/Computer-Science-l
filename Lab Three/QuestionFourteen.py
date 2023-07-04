#Question Fourteen

y= int(input('Enter a Number'))
z= int(input('Enter a Number'))

sum = 0
for x in range(y,z):
    if x % 2 != 0:
        sum = sum+x

print(sum)

