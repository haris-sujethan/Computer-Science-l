# Question Seven

x = int(input('Enter a Number'))
y = int(input('Enter a Number'))
z = int(input('Enter a Number'))

outputString=""

if x<=y<=z or x>=y>=z:
    outputString += "in order "
else:
    outputString += "not in order "
    
if x<=y<=z:
    outputString += "ascending"

elif x>=y>=z:
    outputString += "descending"
    
print(outputString)

