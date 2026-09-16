from functools import wraps
import time
def masoara_tip():
    def decodor(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            start=time.time()
            rezultat=func(*args,**kwargs)
            print( f"{time.time()-start:.4f} am asteptat")
            return rezultat
        return wrapper
    return decodor
@masoara_tip()
def suma(n):
    return sum(range(n))

if __name__=="__main__":
    suma(1576580)