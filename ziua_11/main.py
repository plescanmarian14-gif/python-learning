import functools

def logheaza(functie):
    @functools.wraps(functie)
    def wrapper(*args, **kwargs):
        print(f"Apelez {functie.__name__}")
        rezultat = functie(*args, **kwargs)
        print(f"{functie.__name__} a terminat")
        return rezultat
    return wrapper

@logheaza
def aduna(a, b):
    return a + b

print(aduna(3, 5))