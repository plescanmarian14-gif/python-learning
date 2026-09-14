def este_email_valid(text):
    if "@" in text:
        return f"{text} adresa este valida!"
    else:
        return f"Nu"
def este_numar_telefon_valid(text):
    if len(text)==10 and text.isdigit()==True:
        return f"{text} numarul este valid!"
    else:
        return f"Nu"