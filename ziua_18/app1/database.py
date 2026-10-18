from app.database import id_counter
from app1.schemas import ProdusResponse

baza_de_date=[
    ProdusResponse(nume="Mari",pret=3.05,categorie="Electrocasnic",in_stoc=True),
    ProdusResponse(nume="Maria",pret=3.25,categorie="Electro",in_stoc=True)
]

id_counter=3