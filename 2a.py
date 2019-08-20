def search(list,ele):
    if ele in list:
        return True
    else:
        return False

lis=[]
while True:
    a=int(input("Enter element"))
    if a!=-1:
        lis.append(a)
    else:
        break
    
b=int(input("Enter element to be searched"))
print(search(lis,b))


    
