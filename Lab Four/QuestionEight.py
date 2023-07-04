#Question Eight 

y=int(input('Enter a positive number: '))
while(y<0):
    print('Please enter postive numbers')
    y=int(input('Enter a positive number: '))
    
        


start = 0
end = y
var = True
ans = 0
# Set precision
e = 0.0000001
while (var) :

        mid = (start + end) / 2
        if (y > (mid * mid)) :
            error = (y - (mid * mid))
        else :
            error = ((mid * mid) - y)

        if ((mid * mid) > y) :
                end = mid
        else :
                start = mid
                
        if (error <= e):
            var = False
            ans = mid

print("Square root of", y, "is",round(ans,7))