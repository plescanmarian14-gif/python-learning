import random
def random_1():
    nr=0
    while True:
        rand=random.randint(1,100)
        if rand==1:
            print(f"Ai ghicit numarul din {nr} incercari!")
            break
        else:
            nr+=1
            print("M-ai baga o fisa!")
random_1()
