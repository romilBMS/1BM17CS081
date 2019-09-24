def checkIfValid(str):
    dict ={ ')':'(', '}':'{', ']':'[' }
    stack=[]
    flag=0
    for ch in str:
        if ch in dict.values():
            stack.append(ch)
        else:
            if dict[ch]!= stack[-1]:  
                flag=1       
                break
            else:
                stack.pop(-1)
    if flag == 1 or len(stack)!=0:
        print("INVALID")
    else:
        print("VALID")

checkIfValid('(){')
        
    


            

