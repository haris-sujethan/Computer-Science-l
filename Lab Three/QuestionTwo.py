#Question Two 

x = float(input('Enter a Number'))

ouputString = ""

if x>0:
    ouputString += 'postive '
else:
    ouputString += 'negative '
    
if abs(x) < 1:
    ouputString += 'small'
elif abs(x) > 1000:
    ouputString +='large'
    

if x==0:
    ouputString = 'zero'
print(ouputString)





