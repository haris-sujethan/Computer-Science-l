#Question Eight
def biggestBuried(s): 
    num, num2 = 0, 0
      
    # start traversing the given string 
    for i in range(len(s)):
          
        if s[i] >= "0" and s[i] <= "9":
            num = num * 10 + int(int(s[i]) - 0)
        else:
            num2 = max(num2, num)
            num = 0
          
    return max(num2, num)


print(biggestBuried('abcd51kkk3kk19ghi')) 
print(biggestBuried('kkk32abce@@-33bb14zzz')) 
print(biggestBuried('this15isast22ring-55'))