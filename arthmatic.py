a=int(input("enter the First number"))
b=int(input("enter the second number"))
def add(a,b):
    add=a+b
    print(add)
    
    def sub(a,b):
        sub=a-b
    print(sub)
def mul(a,b):
    mul=a*b
    print(mul)
def div(a,b):
    div=a/b
    print(div)
op=str(input("enter the operator"))
if op=='+':
    add(a,b)    
elif op=='-':
    sub(a,b)
elif op=='*':
    mul(a,b)
elif op== '/':
    div(a,b)
