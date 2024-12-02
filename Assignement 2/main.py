from calc import *
while(True):
    inp=input("please enter the operation : 1)add , 2)sub , 3)mul , 4)div \n")
    x1=input("please enter the first number \n")
    x2=input("please enter the second number \n")
    if inp=='add':
        print(f"the sum of {x1} and {x2} = {add_1(x1,x2)} \n")
    elif inp=='sub':
        print(f"the subtraction of {x1} and {x2} = {sub(x1,x2)} \n")
    elif inp=='mul':
        print(f"the mult of {x1} and {x2} = {mult(x1,x2)} \n")
    elif inp=='div':
        print(f"the div of {x1} and {x2} = {dev(x1,x2)} \n")     
    else:
        print("wrong operation! \n")
    cont=input("do you want to make another calculation? yes/no \n") 
    if cont=='yes':
        continue
    break