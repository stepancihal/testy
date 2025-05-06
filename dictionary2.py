# Funkce pro vytvoření útulku
def vytvor_utulek():
    return {}

# Funkce pro přidání zvířete do útulku
def pridej_zvire(utulek, jmeno, druh, vek):
    utulek[jmeno] = {"druh": druh, "vek": vek}

# Funkce pro výpis všech zvířat v útulku
def vypis_zvirata(utulek):
    for jmeno, info in utulek.items():
        druh = info["druh"]
        vek = info["vek"]
        if vek == 1:
            print(f"{jmeno} je {druh} a je mu {vek} rok.")
        elif 2 <= vek <= 4:
            print(f"{jmeno} je {druh} a jsou mu {vek} roky.")
        else:
            print(f"{jmeno} je {druh} a je mu {vek} let.")

# Funkce pro výpis zvířat podle druhu
def vypis_podle_druhu(utulek, druh):
    for jmeno, info in utulek.items():
        if info["druh"] == druh:
            vek = info["vek"]
            if vek == 1:
                print(f"{jmeno} je {druh} a je mu {vek} rok.")
            elif 2 <= vek <= 4:
                print(f"{jmeno} je {druh} a jsou mu {vek} roky.")
            else:
                print(f"{jmeno} je {druh} a je mu {vek} let.")

# Hlavní část programu
utulek = vytvor_utulek()

while True:
    print("\nMožnosti:")
    print("1 - Přidat zvíře do útulku")
    print("2 - Vypsat všechna zvířata")
    print("3 - Vypsat zvířata podle druhu")
    print("4 - Ukončit program")
    
    volba = int(input("Zadejte číslo volby: "))
    
    if volba == 1:
        jmeno = input("Zadejte jméno zvířete: ")
        druh = input("Zadejte druh zvířete: ")
        vek = int(input("Zadejte věk zvířete: "))
        pridej_zvire(utulek, jmeno, druh, vek)
    elif volba == 2:
        print("Všechna zvířata v útulku:")
        vypis_zvirata(utulek)
    elif volba == 3:
        druh = input("Zadejte druh zvířete: ")
        print(f"Zvířata podle druhu ({druh}):")
        vypis_podle_druhu(utulek, druh)
    elif volba == 4:
        print("Ukončuji program.")
        break
    else:
        print("Neplatná volba, zkuste to znovu.")
