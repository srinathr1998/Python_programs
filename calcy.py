# calculator program
def print_menu():
    print("Enter 1 for addition")
    print("Enter 2 for subtraction")
    print("Enter 3 for multiplication")
    print("Enter 4 for division")
choice=True
while(choice==True):
    print('Welcome')
    input1=float(input('Please enter the first number :'))
    input2=float(input('Please enter the second number :'))
    print_menu()
    ch=int(input("Please enter your choice: "))
    if(ch==1):
        print("The answer is :",input1+input2)
    elif(ch==2):
        print("The answer is :",input1-input2)
    elif(ch==3):
        print("The answer is :",input1*input2)
    elif(ch==4):
        try:
           print("The answer is :",input1/input2)
        except:
           print('Dont give zero as denominator')
    else:
        print('Please enter a valid number as choice ')
        continue
    print('Do you want continue or exit?(y,n)')
    a=input()
    if(a=='y'):
        choice=False

        
       
