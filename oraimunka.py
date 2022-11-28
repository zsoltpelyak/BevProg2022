def beolvas():
    dalok = {"eloado": [], "cim": [], "mufaj": [], "hossz": []}
    with open("playlist.csv", "r") as a:
        sor = a.readline()
        while sor:
            temp = sor.split(";")
            dalok["eloado"].append(temp[0])
            dalok["cim"].append(temp[1])
            dalok["mufaj"].append(temp[2])
            dalok["hossz"].append(int(temp[3]))
            sor = a.readline()
            lista = []
        for s in dalok.keys():
            lista.append(dalok[s])
        return lista

def teljes_hossz(lista):
    teljes = 0
    for s in lista[3]:
        teljes+= s
    perc = int(teljes/60)
    masodperc = teljes%60
    with open("02_hossz.txt", "w") as a:
        a.write(str(perc) + ":" + str(masodperc))


def leghosszabb_rockzene(lista):
    place = []
    for i, s in enumerate(lista[2]):
        if s == "rock":
            place.append(i)
    max = 0
    for s in place:
        if lista[3][s] > lista[3][max]:
            max = s
    print(lista[1][max])


def leggyakoribb_mufaj(lista):
    mufajok = []
    for s in lista[2]:
        mufajok.append(s)
    most_common = str(max(set(mufajok), key = mufajok.count))
    with open("04_kedvenc_mufaj.txt", "w") as a:
        a.write(most_common.upper())


def zeneket_csoportosit(lista):
    eloadok = set(lista[0])
    out = {}
    ossz = 0
    for s in eloadok:
        for i, d in enumerate(lista[3]):
            if s == lista[0][i]:
                ossz += int(d)
        out[s] = ossz
        ossz = 0
    print(out)


def zeneket_listaz(lista, eloado):
    if eloado in lista[0]:
        with open("06_" + str(eloado).replace(" ", "_") + "_dalok.txt", "w") as a:
            places = []
            for i, s in enumerate(lista[0]):
                if str(s).lower() == str(eloado).lower():
                    places.append(i)
            for s in places:
                a.write(str(lista[1][s]) + ";" + str(lista[2][s]) + ";" + str(lista[3][s]) + "\n")
    else:
        print("Nincs ilyen eloado a lejatszasi listaban!")


def main():
    teljes_hossz(beolvas())
    leghosszabb_rockzene(beolvas())
    leggyakoribb_mufaj(beolvas())
    zeneket_csoportosit(beolvas())
    zeneket_listaz(beolvas(), "Powerwolfasd")

if _name_ == '_main_':
    main()