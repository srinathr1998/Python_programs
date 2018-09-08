# stone paper scissors game
import random
def printmenu():
    print('Enter 1 for stone: ')
    print('Enter 2 for paper: ')
    print('Enter 3 for scissors: ')
print ('Welcome')
user=0
cpu=0
choice=True
while(choice):
        printmenu()
        u=int(input())
        if(u!=1 and u!=2 and u!=3):
            print("Sorry only 3 choices available")
        c=random.randint(1,3)
        if(c==1):
            print('cpu picks stone')
        elif (c==2):
            print('cpu picks paper')
        else:
            print('cpu picks scissors')
        if(u==c):
            print("Its a draw")
        if(u==1 and c==3):
            print("You won")
            user=user+1
        if(u==1 and c==2):
            print('Sorry but you suck at this game')
            cpu=cpu+1
        if(u==2 and c==1):
            print("You won")
            user=user+1
        if(u==2 and c==3):
            print('Sorry but you suck at this game')
            cpu=cpu+1
        if(u==3 and c==2):
            print("You won")
            user=user+1
        if(u==3 and c==1):
            print('Sorry but you suck at this game')
            cpu=cpu+1
        print("Do you want to continue playing?(yes/no)")
        x=input()
        if(x=='no'):
            print("The scores so far are user: ",user," and cpu : ",cpu)
            if (user>=cpu):
                print('good job')
            else:
                print('You cant beat this beast of a program')
            choice=False
        elif(x=='yes'):
            choice=True
        else:
            print('pick yes or no for fucks sake')
            exit()
         
