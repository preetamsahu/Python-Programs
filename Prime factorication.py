from math import sqrt
n=int(input())
def factorization(n):
    factor = []
    for i in range(1,int(sqrt(n))+1):
        if n%i==0:
            factor.append(i)
            if i!=n//i:
                factor.append(n//i)
    return factor

def is_prime(n):
    if len(factorization(n))==2:
        return 1
    else:
        return 0

factors=factorization(n)
prime=[]
for i in factors:
    if is_prime(i):
        prime.append(i)

prime_factorization=""
ind=0
i=prime[ind]
while n>=0:
    if n%i==0:
        prime_factorization=prime_factorization+ str(i)+" * "
        n=n//i
    else:
        try:
            ind+=1
            i=prime[ind]
        except:
            break
prime_factorization=list(prime_factorization)
prime_factorization.remove(prime_factorization[-1])
prime_factorization="".join(prime_factorization)
print(prime_factorization)




