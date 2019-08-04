# Function Defifnition
def GCD(n1,n2):
# n1 and n2 are any arbitrary non_zero Positive integers
# Returns the gcd
    
    while(n2 % n1 != 0):
        if(n1>n2):
          # Making n2 as a larger number
          n1,n2 = n2,n1
        n2 = n2 % n1
    
    return(n1)

#---------------------------------------------------

# Driver Code

n1 = int(input("Enter any Non_zero Positive Integer"))
# Checking for invalid inputs
while(n1 <= 0):
    n1 = int(input("Enter any Non_zero Positive Integer"))

    
n2 = int(input("Enter any Non_zero Positive Integer"))
# Checking for invalid inputs
while(n2 <= 0):
    n2 = int(input("Enter any Non_zero Positive Integer"))
    
gcd = GCD(n1,n2)
print("The GCD of ", n1,n2," is ", gcd)
