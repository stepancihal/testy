def registrace_darce():
    print("Registrace dárce krve")
    jmeno = input("Zadejte své jméno: ")
    vek = input("Zadejte svůj věk: ")
    vek = int(vek)

    if vek >= 18:
        krevni_skupina = input("Zadejte svou krevní skupinu (např. A+, 0-, AB+): ")
        print("Děkujeme,", jmeno, "byl jste úspěšně zaregistrován jako dárce krve.")
        print("Věk:", vek)
        print("Krevní skupina:", krevni_skupina)
    else:
        print("Dárce musí být starší než 18 let.")

if __name__ == "__main__":
    registrace_darce()