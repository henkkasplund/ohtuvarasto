from varasto import Varasto


def tulosta_luomiset(mehua, olutta):
    print("Luonnin jälkeen:")
    print(f"Mehuvarasto: {mehua}")
    print(f"Olutvarasto: {olutta}")


def tulosta_getterit(olutta):
    print("Olut getterit:")
    print(f"saldo = {olutta.saldo}")
    print(f"tilavuus = {olutta.tilavuus}")
    print(f"paljonko_mahtuu = {olutta.paljonko_mahtuu()}")


def kokeile_settereita(mehua):
    print("Mehu setterit:")
    print("Lisätään 50.7")
    mehua.lisaa_varastoon(50.7)
    print(f"Mehuvarasto: {mehua}")
    print("Otetaan 3.14")
    mehua.ota_varastosta(3.14)
    print(f"Mehuvarasto: {mehua}")


def kokeile_virheellista_luomista():
    print("Virhetilanteita:")
    print("Varasto(-100.0);")
    print(Varasto(-100.0))
    print("Varasto(100.0, -50.7)")
    print(Varasto(100.0, -50.7))


def kokeile_virheellista_lisaysta(mehua, olutta):
    print(f"Olutvarasto: {olutta}")
    print("olutta.lisaa_varastoon(1000.0)")
    olutta.lisaa_varastoon(1000.0)
    print(f"Olutvarasto: {olutta}")

    print(f"Mehuvarasto: {mehua}")
    print("mehua.lisaa_varastoon(-666.0)")
    mehua.lisaa_varastoon(-666.0)
    print(f"Mehuvarasto: {mehua}")


def kokeile_ottoa(varasto, nimi, maara):
    print(f"{nimi}: {varasto}")
    print(f"ota_varastosta({maara})")
    saatiin = varasto.ota_varastosta(maara)
    print(f"saatiin {saatiin}")
    print(f"{nimi}: {varasto}")


def main():
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)

    tulosta_luomiset(mehua, olutta)
    tulosta_getterit(olutta)
    kokeile_settereita(mehua)
    kokeile_virheellista_luomista()
    kokeile_virheellista_lisaysta(mehua, olutta)
    kokeile_ottoa(olutta, "Olutvarasto", 1000.0)
    kokeile_ottoa(mehua, "Mehuvarasto", -32.9)


if __name__ == "__main__":
    main()
# push before pull kommentti
