import gender_guesser.detector as gender
d = gender.Detector()

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



