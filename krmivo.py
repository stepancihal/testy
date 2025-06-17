celkova_krmna_davka = 0.0

while True:
    vaha = float(input("Zadej váhu kočky v kg: "))
    davka = vaha * 30 + 70
    print(f"Kočka váží {vaha} kg a měla by dostat {davka} gramů krmení denně.")
    celkova_krmna_davka += davka
    dalsi = input("Chceš zadat další kočku? (ano/ne): ")
    if dalsi == "ne":
        break

print(f"Celková krmná dávka pro všechny kočky: {celkova_krmna_davka} gramů.")