
def ma_dlzku(heslo, min_dlzka=8):
    # vráti True/False
    return len(heslo) >= min_dlzka

def ma_velke_pismeno(heslo):
    # prejde znaky cyklom, hľadá veľké písmeno
    for znak in heslo:
        if znak.isupper():
            return True
    return False

def ma_male_pismeno(heslo):
    for znak in heslo:
        if znak.islower():
            return True
    return False

def ma_cislicu(heslo):
    for znak in heslo:
        if znak.isdigit():
            return True
    return False

def ma_specialny_znak(heslo):
    specialne = "!@#$%^&*()-_=+[]{};:,.<>?"
    for znak in heslo:
        if znak in specialne:
            return True
    return False

def je_caste_heslo(heslo):

    caste_hesla = [
    # Číselné postupnosti
    "123456",
    "12345678",
    "123456789",
    "1234567890",
    "12345",
    "111111",
    "000000",
    "1234",
    "666666",
    "654321",

    # Klasické slová
    "password",
    "password1",
    "passw0rd",
    "qwerty",
    "qwerty123",
    "abc123",
    "admin",
    "welcome",
    "letmein",
    "login",
    "iloveyou",
    "monkey",
    "dragon",
    "master",
    "sunshine",
    "princess",
    "football",
    "superman",
    "batman",

    # Klávesnicové vzory
    "qwertyuiop",
    "asdfghjkl",
    "zxcvbnm",
    "1qaz2wsx",
    "qazwsx",

    # Slovenské / české časté
    "heslo",
    "heslo123",
    "slovensko",
    "tajne",
    "milujem",

    # Opakované / jednoduché
    "aaaaaa",
    "abcabc",
    "abcdef",
    "abcd1234",
]
    for caste_heslo in caste_hesla:
        if heslo.lower() == caste_heslo:
            return True        
    return False

def vyhodnot_heslo(heslo):
    # zavolá všetky kontroly, spočíta skóre, vypíše výsledok
    skore = 0
    if ma_dlzku(heslo):
        skore += 1
    else: 
        print("Heslo je príliš krátke. Musí mať aspoň 8 znakov.")
    if ma_velke_pismeno(heslo):
        skore += 1
    else:
        print("Heslo neobsahuje veľké písmeno.")
    if ma_male_pismeno(heslo):
        skore += 1
    else:
        print("Heslo neobsahuje malé písmeno.")
    if ma_cislicu(heslo):
        skore += 1
    else:
        print("Heslo neobsahuje číslicu.")
    if ma_specialny_znak(heslo):
        skore += 1
    else:
        print("Heslo neobsahuje špeciálny znak.")
    if not je_caste_heslo(heslo):
        skore += 1
    else:
        print("Heslo je príliš časté a ľahko uhádnuteľné.")
    print(f"Skóre hesla: {skore}/6")
    return skore

# Hlavný program
import getpass
while True:
    heslo = getpass.getpass("Zadaj heslo na kontrolu: ")
    skore = vyhodnot_heslo(heslo)
    if skore < 6:
        print("Heslo nie je dostatočne silné. Skús to znova.")
        continue
    elif skore == 6:
        print("Zadali ste dostatočne silné heslo.")
        break
        
