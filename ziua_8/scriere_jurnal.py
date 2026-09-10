from datetime import datetime
def adauga():
    while True:
        text=input("Introduceti o notita zilnica: ")
        if text=="nu":
            break
        time=datetime.now().strftime("%Y-%m-%d %H:%M")
        with open("notite.csv","a") as f :
            f.write(f"[{time}]{text} .\n")
def afiseaza():
    try:
        with open("notite.csv","r") as f:
             for linie in f:
                print(linie)
    except FileNotFoundError:
        print("Jurnal gol!")
adauga()
afiseaza()
