number=[]
n = int(input("enter no of elements"))
for i in range(0,n):
    elements=int(input("enter the number:"))
    number.append(elements)
print("\n",number)
for i in range(0, n):
        if number[i]> 100:
            number[i]='over'
print(number)
