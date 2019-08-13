def Fibo(n): 
      
    t1 = 0
    t2 = 1
    if (n < 1): 
        return
    for x in range(0, n): 
        print(t2, end = " ") 
        temp = t1 + t2 
        t1 = t2 
        t2 = temp



    Fibo(7)
