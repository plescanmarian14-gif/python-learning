from functools import wraps

def repeta(n):
    def decorator(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            rezultat=0
            for _ in range(n):
                rezultat=func(*args,**kwargs)
            return rezultat
        return wrapper
    return decorator

@repeta(n=3)
def saluta(nume):
    print(f"{nume}")
if __name__=="__main__":
    saluta("mai")