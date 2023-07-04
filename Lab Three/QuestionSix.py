#Question Six

x = int(input('Enter a Number'))
y = int(input('Enter a Number'))
z = int(input('Enter a Number'))

q = input("strict or lenient")


if q =='strict':

   if x<y<z:
       print('increasing')
   elif x>y>z:
       print('decreasing')
   else:
       print('nethier') 
  

 
if q =='lenient':
    
   if x==z==y:
      print('increasing and decreasing')

   elif x<=y<=z:
       print('increasing')
   elif x>=y>=z:
       print('decreasing')
   else:
       print('nethier') 

