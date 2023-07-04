#The following code is the savings Calculator, it will tell you how many months it will take to reach your savings goal.
#The Code will ask for your savings goal, monthly income, monthly expenses, and determine how many months it will take to reach that goal.


SavingsGoal = int(input("Welcome to Savings Calculator, Please Enter Your Savings Goal: ")) #Asks the user for thier savings goal
while(SavingsGoal<=0):
    SavingsGoal=int(input('Please Enter a Valid Amount: ')) #Line x and y will keep asking the user for a postive number, if they previously inputed a negative 0
    
    
MonthlyIncome = int(input("Please Enter Your Monthly Income: ")) #Asks the user for thier monthly goal
while(MonthlyIncome<=0):
    MonthlyIncome = int(input('Please Enter a Valid Amount: ')) #Line x and y will keep asking the user for a postive number, if they previously inputed a negative or 0


MonthlyExpenses = int(input("We will now begin you monthly expences, How MANY monthly Expeses Do You Have?")) #Asks the user for how MANY expenses they have. For example, Vechicle payment, waterbill, Netflix, would be 3. 
    
def MonthlyExpenseCalculator(b): #This function makes the code more effecient, insted of asking each possible expense it asked for the number of expenses inputed from the user previously.
    x = 0
    s = 0
    while(x<b):
        s +=int(input("Enter Amount: ")) #Adds each of the expenses inputed from the user.
        x+=1
    return s
                                           # The while loop runs untill x<b is false. 
x = MonthlyExpenseCalculator(MonthlyExpenses)# x has been set to the total monthly expenses 

y = MonthlyIncome - abs(x) #y has been set to the calculation of the gross monthly income (Monthly income - Monthly Expenses)

if y == 0: # this if statment only runs when the gross monthly income == 0 
    print("Monthly Income and Monthly Expenses Are the Same. No Money Can be Saved")
    exit() #When this if statment is true, the code runs the print, and exits the code. This is done so the rest of the code is not ran.

AmountofMonths = SavingsGoal/(y) #AmountofMonths has been set to calculate the number of months it will take to reach the users savings goaln


if MonthlyExpenses==0:# If their is no monthly expenses, this if will run.
    print("It Will Take",SavingsGoal/MonthlyIncome,"Months to Reach your Savings Goal") 
    
elif x>=MonthlyIncome: #if monthly expenses is greater than monthly income this if will run. 
    print("Resulted in a Negative Number (Monthly Income to Low, or/and Monthly Expeses to High. Can't Save Money")

else: #if all the other if's and elif dont run, this will. 
    print('Therefore it will take',AmountofMonths,'months to reach your savings goal')
    print('Or',AmountofMonths*30.4167,'days') # will convert months to days and display it
    print('Or',AmountofMonths/12,'years')     # will convert months to years and display it
    
    