arr = []
n=int(input("enter the number of element you want in array "))
for i in range(0,n):
 element=int(input())
 arr.append(element)
print(arr)
p=arr[0]
arr[0]=arr[-1]
arr[-1]=p
print(arr[0])
print(arr[-1])
print(arr)