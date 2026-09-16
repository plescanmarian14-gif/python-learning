from functools import wraps

dic={}

def decorator(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        rezultat=func(*args,**kwargs)
        n=args[0]
        dic[n]=rezultat
        return rezultat
    return wrapper

@decorator
def factori(n):
    fac=1
    for i in range(1,n+1):
        fac*=i
    return fac

if __name__=="__main__":
    print(factori(10))
    print(factori(5))
    print(dic)