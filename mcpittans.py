import matplotlib.pyplot as plt 

a=int(input("enter the input:"))
b=int(input("enter the input2:"))
weight=2
weight1=2
theshold=4
if (a*weight+b*weight1>=theshold):
    print(1)
    plt.plot([1,0],[0,1])
    plt.show()
else:
    print(0)
    
    

 

    