n=int(input("Spuneti un nr: "))
def este_par(n):
    if n%2==0:
        return "numar par"
    else:
        return "impar"
print(este_par(n))

def factorial(n):
    fac=1
    for i in range(2,n+1):
        fac=fac*i
    return fac
print(factorial(n))

def is_prim(n):
    d=2
    while d<=n/d:
        if n%d==0:
            return "nu este prim"
        d+=1
    return "prim"
print(is_prim(n))