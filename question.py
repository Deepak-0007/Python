a = int(input("Enter a number:"))

for i in range(a):
    for j in range(a-i):
        print(' ',end='')
    for k in range(i+1):
        print(i + ' ',end='')
    print('')
    
        
    