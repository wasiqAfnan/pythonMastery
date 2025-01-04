# Iterative approach
def euclid_gcd(a,b):
    while a%b > 0:
        a, b = b, a%b
    return b
    
# Recursive approach
def rec_gcd(a,b):
    if a%b == 0:
        return b
    return rec_gcd(b, a%b)
        
print(euclid_gcd(10,55)) # output: 5
print(rec_gcd(10,55)) # output: 5
