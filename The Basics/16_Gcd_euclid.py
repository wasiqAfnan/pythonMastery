# Iterative approach
def euclid_gcd(a,b):
    while a%b > 0:
        a, b = b, a%b
    return b
    
# Recursive approach

        
print(euclid_gcd(10,55)) # output: 5
