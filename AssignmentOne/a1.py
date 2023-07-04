#The following code is a savings calculator, it will tell you how many months it will take to reach your savings goal.
#The Code will ask for your savings goal, monthly or yearly income, monthly/yearly expenses, and determine how many months/years it will take to reach that goal.

SavingsGoal = int(input("Welcome to Savings Calculator, Please Enter Your Savings Goal (Do Not Include Commas, decimals, words, or $): ")) #Asks the user for their savings goal
while(SavingsGoal<=0):
    SavingsGoal=int(input('Please Enter a Valid Amount: ')) #Line 5 and 6 will keep asking the user for a positive integer, only if the user previously inputted a negative integer or 0
        
divideByZero = False

MorY = input("Please Enter Month or Year (This Will Determine if the Calculations Should be Monthly or Yearly): ") #Asks the user to input month or year

while not (MorY == "Year" or MorY == "year" or MorY ==  "Month" or MorY ==  "month" or MorY ==  "M" or MorY == "m" or MorY == "Y" or MorY == "y"): #Includes common variations
    MorY = input("Please enter a valid answer, Month or Year ") #Will ask for input agian, if previous input was invalid.
    
if (MorY == "Year" or MorY == "year" or MorY == "Y" or MorY == "y" ):
    YearlyIncome = int(input("Please Enter Your Yearly Income: ")) #Asks the user for there yearly income
    while(YearlyIncome<=0):
        YearlyIncome = int(input('Please Enter a Valid Amount: ')) #Line 17 and 18 will keep asking the user for a positive integer, only if the user previously inputted a negative integer or 0
    YearlyExpenses = int(input("We will now begin you yearly expenses, How MANY yearly expenses do You have?: ")) #Asks the user for how MANY expenses they have. For example, Vehicle payment, water bill, Netflix, would be 3.
    
    def YearlyExpenseCalculator(b): #This function makes the code more efficient, instead of asking each possible expense it asked for the number of expenses inputed from the user previously.
        x = 0
        s = 0
        while(x<b):
            s +=(int(input("Enter Amount: "))) #Adds each of the expenses imputed from the user.
            x+=1
        return s
                                               # The while loop runs until x<b is false. 
   
    x = YearlyExpenseCalculator(YearlyExpenses) # x has been set to the total yearly expenses
    
    print('Total Yearly Expense',x,)
    
    y = YearlyIncome - abs(x) #y has been set to yearly gross income, (yearly income-yearly expenses)
    
    if y == 0 or SavingsGoal==y==x: # this if statement only runs when the gross yearly income is equal to 0 
        print("Yearly Income minus Yearly Expenses result in 0. No Money Can be Saved")
        divideByZero = True
    if not divideByZero:
        AmountofYears = SavingsGoal/(y) #AmountofYears has been set to calculate the number of years it will take to reach the users savings goal
    
    if YearlyExpenses==0:# If their is no yearly expenses, this if will run.
        print("It Will Take",SavingsGoal/YearlyIncome,"years to Reach your Savings Goal") 
        
    elif abs(x)>=YearlyIncome and not divideByZero: #if yearly expenses is greater than yearly income this if will run. 
        print("Resulted in a Negative Number (Yearly Income to Low, or/and Yearly Expenses to High. Can't Save Money")
    
    elif(not divideByZero): #if all the other if's and elif dont run, this will. 
        print('Therefore it will take',AmountofYears,'years to reach your savings goal')
        print('Or',AmountofYears*365,'days') # will convert years to days and display it
        print('Or',AmountofYears*52,'weeks')     # will convert years to weeks and display it
else:
   
        
    MonthlyIncome = int(input("Please Enter Your Monthly Income: ")) #Asks the user for their monthly goal
    while(MonthlyIncome<=0):
        MonthlyIncome = int(input('Please Enter a Valid Amount: ')) #Line 54 and 55 will keep asking the user for a positive integer, only if the user previously inputted a negative integer or 0
    
    
    MonthlyExpenses = int(input("We will now begin you monthly expenses, How MANY monthly expenses Do You Have?: ")) #Asks the user for how MANY expenses they have. For example, Vehicle payment, water bill, Netflix, would be 3. 
        
    def MonthlyExpenseCalculator(b): #This function makes the code more efficient, instead of asking each possible expense it asked for the number of expenses imputed from the user previously.
        x = 0
        s = 0
        while(x<b):
            s +=(int(input("Enter Amount: "))) #Adds each of the expenses imputed from the user.
            x+=1
        return s
                                               # The while loop runs until x<b is false. 
                                               
    x = MonthlyExpenseCalculator(MonthlyExpenses)# x has been set to the total monthly expenses 
    
    print('Total Monthly Expense',x,)
    
    y = MonthlyIncome - abs(x) #y has been set to the calculation of the gross monthly income (Monthly income - Monthly Expenses)

    if y == 0 or SavingsGoal==y==x: # this if statement only runs when the gross monthly income == 0 
        print("Monthly Income Minus Monthly Expenses result in zero. No Money Can be Saved")
        divideByZero = True
    
    if not divideByZero:  
        AmountofMonths = SavingsGoal/(y) #AmountofMonths has been set to calculate the number of months it will take to reach the users savings goal
    
    
    if MonthlyExpenses==0:# If there is no monthly expenses, this if will run.
        print("It Will Take",SavingsGoal/MonthlyIncome,"Months to Reach your Savings Goal") 
 
        
    elif abs(x)>=MonthlyIncome and not divideByZero: #if monthly expenses is greater than monthly income this if will run. 
        print("Resulted in a Negative Number (Monthly Income to Low, or/and Monthly Expenses to High. Can't Save Money")
    
    elif(not divideByZero): #if all the other if's and elif dont run, this will. 
        print('Therefore it will take',AmountofMonths,'months to reach your savings goal')
        print('Or',AmountofMonths*30.4167,'days') # will convert months to days and display it
        print('Or',AmountofMonths/12,'years')     # will convert months to years and display it
        
        
        
        
        
        
        
        
        
        