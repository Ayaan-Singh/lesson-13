op = (input("enter what you want do "))
num1 = int(input(f"please enter a number you want to {op} by ") )
num2 = int(input(f"please enter a number you want to {op} from {num1} ")  )
def add(n1,n2):
    sum = n1+ n2
    return sum
def sub(n1,n2):
    sub = n1- n2
    return sub
def times(n1,n2):
    times = n1* n2
    return times
def div(n1,n2):
    div = n1/n2
    return div
if (op == "add"):
    print(add(num1,num2))
elif  (op == "sub"):
       print(sub(num1,num2))  
elif  (op == "times"):
       print(times(num1,num2)) 
elif (op == "div"):
     print(div(num1,num2))
else:
     print ("invalid input")     