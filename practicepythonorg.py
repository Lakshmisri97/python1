#ex.1 program to get the user name and their current age. out put will be the year they will turn 100


import datetime
name=str(input("What is your name? "))
age=int(input("enter your age in years and as an integer: "))
today=str(datetime.date.today())
year=int(today[0:4])    #getting the yy part of the year
century=(year)+100-age  #gettin the year the user will turn 100
print(name," will turn 100 in the year, ",century,"AD")



#ex.2 is the number odd or even

numb=int(input("Ener an integer: "))
if numb==0:
    print("The number entered is 0")
elif numb%2==0:
    print("The number entered is even")
else:
    print("the number entered is odd")

    

#ex.3 make a list, asking the user for the elements to be entered. then make another list with the elements from the previous list but having the elements less than a value given by the user

def list1():

    
    list1=[]
    while list1==[] or prompt.upper()=="Y":
        element=input("Enter an element to be appended in the list: ")
        try:
            element==float(element)
            
        except:
            element=element
        list1.append(element)
        prompt=input("Do you want to enter more lements? Y/N: ")
    print(list1)
    constraint=input("Enter a number, so tha the new list has numbers less than the one you give: ")
    newlist=[]
    print(constraint)
    for elem in list1:
        
        if elem<constraint:
            newlist.append(elem)
    print(newlist)



# ex.4 to find divisor for a number given by the user

def divisor():
    try:
        value=int(input("enter a positive integer: "))
        div=1
        divlist=[1]
        
        if value<=0:
            print("invalid")
        elif value==1:
            print(divlist)
        else:
            for div in range(2,value//2+1):
                if value%div==0:
                    divlist.append(div)
            divlist.append(value)
            print(divlist)
    except:
        print("invalid entry")



#ex.5 a program to create a new list that contains only the common elements from 2 lists
#     and not have duplicate value


list1=[]
list2=[]
nodup1=[]
nodup2=[]
nodup=[]
n1=int(input("enter the number of items in list1: "))
for x in range(0,n1):
    x=int(input("enter the items in list1: "))
    list1.append(x)
print("list1= ",list1)
for x in list1:
    if x not in nodup1:
        nodup1.append(x)
print("nodup1:",nodup1)
n2=int(input("enter the number of items in list2: "))

for y in range(0,n2):
    y=int(input("enter the items in list2: "))
    list2.append(y)
print("list2: ",list2)
for y in list2:
    if y not in nodup2:
        nodup2.append(y)
        if y in nodup1:
            nodup.append(y)
print("nodup2:",nodup2)
print("new combined list without duplicate: ",nodup)

#ex.6 check if the string is a palindrome

string=str(input("enter a string: "))
length=len(string)
palindrome=""
for x in range(0,length):
        char=string[length-1-x]
        palindrome=palindrome+char
print(palindrome)
if string.upper()==palindrome.upper():
    print("'",string,"'"," is a palindrome")
else:
    print("'",string,"'"," is not a palindrome")
    

           
#ex.7 from the list make a list with only even numbers

list1=[]
prompt="Y"
list2=[]
while prompt.upper()=="Y":
        numb=int(input("enter number: "))
        list1.append(numb)
        if numb%2==0:
                 list2.append(numb)

        prompt=input("Do you want to enter more numbers? Y/N): ")
print("original list- ",list1)
print("new list with even numbers- ",list2)


 
#ex.8 rock paper scissors game

def rps():
 

 player1=input('player 1 choice-Rock/Paper/Scissors: ')
 if player1.lower() in ('rock','paper','scissors'):
    player2=input('player 2 choice-Rock/Paper/Scissors: ')
    if player2.lower() not in ('rock','paper','scissors'):
        print('invalid entry')
    else:
        if player1.lower()==player2.lower():
            print("no winners.both selected the same")
        if (player1.lower()=='rock' and player2.lower()=='paper') or(player1.lower()=='scissors' and player2.lower()=='rock')or (player1.lower()=='paper' and player2.lower()=='scissors'):
             print("player 2 is the winner")
        elif (player1.lower()=='rock' and player2.lower()=='scissors') or(player1.lower()=='paper' and player2.lower()=='rock') or (player1.lower()=='scissors' and player2.lower()=='paper'):
            print('player1 is the winner')
            
 else:
    print("wrong entry")
                                

#ex.9 guess the random number generated

def rand():
    import random
    prompt='Y'
    correct=0
    wrong=0
    total=0
    while prompt.upper()=='Y':
        ran=random.randint(1,9)
        #print(ran)
        guess=int(input('Guess the random number between 1 and 9(both inclusive): '))
        if guess< ran:
            print(ran ," is the random number and it is greater.")
            wrong=wrong+1
        elif guess>ran:
            print(ran," is the random number and it is smaller")
            wrong=wrong+1
        elif guess==ran:
            print('Congratulations!')
            correct=correct+1
        prompt=input("Do you want to guess more?(Y/N): ")
    total=correct+wrong
    print("Total number of guesses: ",total)
    print("correct guesses: ",correct)
    print("wrong guesses: ",wrong)

        
 #ex.10 (same as example5)
#ex.11 Find if a number given by the user is prime

def prime():
    try:
        value=int(input("enter a positive integer: "))
        div=1
        divlist=[1]
        
        if value<=0:
            print("invalid")
        elif value==1:
            print(divlist)
            print("1 is a prime number")
        else:
            for div in range(2,value//2+1):
                if value%div==0:
                    divlist.append(div)
            divlist.append(value)
            print(divlist)
            if divlist==[1,value]:
                print(value," is a prime number")
            else:
                print(value," is not a prime number")
    except:
        print("invalid entry")
