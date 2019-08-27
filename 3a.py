div=[]
n=int(input("Enter the element"))
for i in range(1,n+1):
    if n%i==0:
        div.append(i)

print(div)

