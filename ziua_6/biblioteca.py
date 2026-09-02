class Carte:

  def __init__(self, titlu, autor, disponibila=True):
    self.titlu = titlu
    self.autor = autor
    self.disponibila = disponibila


class Biblioteca:

  def __init__(self):
    self.carti = []  # Începem cu o listă goală de cărți

  def adauga_carte(self, carte):
    self.carti.append(carte)

  def imprumuta_carte(self, titlu):
    gasita = False
    for carte in self.carti:
      if carte.titlu.lower() == titlu.lower():
        gasita = True
        if carte.disponibila:
          carte.disponibila = False  # O marcăm ca împrumutată
          print(f"Cartea '{carte.titlu}' a fost împrumutată cu succes!")
        else:
          print(f"Cartea '{carte.titlu}' este deja împrumutată.")
        break  # Am găsit cartea, oprim căutarea

    if not gasita:
      print(f"Nu avem cartea '{titlu}' în bibliotecă.")

  def afiseaza_disponibile(self):
    print("\n--- Cărți disponibile ---")
    exista = False
    for carte in self.carti:
      if carte.disponibila:
        print(f"- '{carte.titlu}' de {carte.autor}")
        exista = True
    if not exista:
      print("Nu există cărți disponibile.")


# --- Meniul și utilizarea ---

bibli = Biblioteca()  # Creezi biblioteca O SINGURĂ DATĂ în afara buclei

while True:
  raspuns = input("\nVrei să adaugi o carte? (Da/Nu): ").strip().lower()
  if raspuns == "da":
    titlu = input("Titlu: ")
    autor = input("Autor: ")
    carte_noua = Carte(titlu, autor)  # disponibila va fi True implicit
    bibli.adauga_carte(carte_noua)
  else:
    break

# Testăm metodele după finalizarea adăugării
titlu_cautat = input("\nIntrodu titlul cărții pe care vrei să o împrumuți: ")
bibli.imprumuta_carte(titlu_cautat)

bibli.afiseaza_disponibile()