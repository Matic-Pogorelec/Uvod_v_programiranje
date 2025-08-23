import gender_guesser.detector as gender
d = gender.Detector()
def zlepi(seznam):
    """Funkcija sprejme seznam in "sešteje" vse elemente, to je zlepi vse nize v enega."""
    if seznam == []:
        return ""
    else:
        return seznam[0] + zlepi(seznam[1:])
    

def odstrani_vejice(število):
    """Funkicja odstrani vejice iz števila, na koncu vrne objekt tipa int"""
    return (zlepi((str(število).split(","))))


def določi_spol(ime):
    """Funkcija na podlagi imena določi spol osebe. Vrne lahko Moški, Ženska in Ni znano."""
    spol = ""
    prvo_ime = str(ime)
    if prvo_ime != "":
        prvo_ime = (prvo_ime).split()[0]
    spol = ""
    if  d.get_gender(prvo_ime) in {"male", "mostly_male"}:
        spol = "Moški"
    elif d.get_gender(prvo_ime) in {"female", "mostly_female"}:
        spol = "Ženska"
    else:
        spol = "Ni znano"
    return spol



