def function():
    try:
        a = input("Say two numbers: ")
        b = input("Say two numbers: ")
        a=int(a)
        b=int(b)
        if a==0 or b==0:
            raise ValueError("Ati introdus unul dintre numere 0!")
        else:
            c=a//b
    except ValueError as e:
        print(f"Eroare: {e}")
    else:
        print(f"Impartirea este: {c}")
    finally:
        print("Bloc executat!")

function()