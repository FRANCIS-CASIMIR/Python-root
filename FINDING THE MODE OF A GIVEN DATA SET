# Mode of a data set
a=[]
print("THE DATA SET CAN BE UN-SORTED AND THE ELEMENTS NEED NOT BE UNIQUE")
print("*** **** *** *** ** ********* *** *** ******** **** *** ** ******")
print("PRESS * TO STOP ENETRING ELEMENTS")
print("******* ** **** ******** ********")
n=input("Enter the first element")
while(n!='*'):
    y=int(n)
    a.append(y)
    n=input("Enter the next element")
print("You have eneterd the following set of data:",a)
modes=[]
old_count=0
new_count=0
i=0
evalted=[]
for x in a:
    if x in evalted:
        pass
    else:
        new_count=a.count(x)
        if old_count<new_count:
            modes[0:]=[]
            modes.append(x)
            old_count=new_count
        elif old_count==new_count:
            modes.append(x)
            old_count=new_count
        evalted.append(x)
    i+=1
print("The mode/s  is/are:",modes)
