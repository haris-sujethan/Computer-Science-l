#Question Nine 

y = int(input('Enter an Intger'))
y= abs(y)

start = 0
end = y
var = True
x = 0
# Set precision
e = 0.0000001
while (var) :
        mid = (start + end) / 2
        if (y > (mid * mid * mid)) :
            error = (y - (mid * mid * mid))
        else :
            error = ((mid * mid * mid) - y)

        if ((mid * mid * mid) > y) :
                end = mid
        else :
                start = mid
                
        if (error <= e):
            var = False
            x = mid

print("Cubed root of", y, "is",round(x, 7))