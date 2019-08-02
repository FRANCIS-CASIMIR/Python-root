def PrintNear(a):
    import math
    
    diff = math.fabs(a[0]-a[1])
    num1,num2 = a[0],a[1]
    l =len(a)
    
    for x in range(0,l-1):
        for y in range(x+1,l):
            if(diff>math.fabs(a[x]-a[y])):
                diff = math.fabs(a[x]-a[y])
                num1,num2 = a[x],a[y]  
    
    print(num1,num2)
