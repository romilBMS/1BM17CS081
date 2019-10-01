def numSquareSum(n): 
    squareSum = 0; 
    while(n): 
        squareSum += (n % 10) * (n % 10); 
        n = int(n / 10); 
    return squareSum;   

def isHappynumber(n): 
  
    
    slow = n; 
    fast = n; 
    while(True): 
          
        
        slow = numSquareSum(slow); 
  
         
        fast = numSquareSum(numSquareSum(fast)); 
        if(slow != fast): 
            continue; 
        else: 
            break; 
  
     
    return (slow == 1)


def createFiles():
    fPrime= open("fPrime.txt",'w')
    fHappy= open("fHappy.txt",'w')

    for val in range(1000):   
        if(isHappynumber(val)):
            fHappy.write(str(val)+"\n")   
    
        if val > 1: 
            for n in range(2, val): 
                if (val % n) == 0: 
                    break
            else: 
                fPrime.write(str(val)+"\n")
    fPrime.close()
    fHappy.close()

def findHapyPrimes():
    fHappy=open("fHappy.txt", 'r')
    fPrime=open("fPrime.txt", 'r')
    common=[]
    for i in fHappy.readlines():
        fPrime.seek(0)
        for j in fPrime.readlines():
            if int(i) == int(j) and int(i) not in common:
                common.append(int(i))
    print(common)  
# createFiles()
findHapyPrimes()


    
 