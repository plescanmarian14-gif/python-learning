def salutari(**kwargs):
    # Extragem valorile din dicționarul kwargs
    ora = kwargs.get("ora")
    nume = kwargs.get("nume")

    if ora is not None:
        if ora < 10:
            return f"Buna dimineata, {nume}"
        elif 10 <= ora <= 18:
            return f"Buna ziua, {nume}"
        else:
            return f"Buna seara, {nume}"
    else:
        return f"Salut, {nume}"

# Atenție la ghilimelele simple 'Florin' din interior!
print(f"salutari de la Marian: {salutari(ora=9, nume='Florin')}")