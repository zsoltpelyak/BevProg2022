def betuszamlalo(szoveg):
    d = {}
    for i in szoveg:
        d[i] = szoveg.count(i)
    return d

def main():
    #1.
    mondat = input("Adjon meg egy mondatot: \n")
    print(betuszamlalo(mondat))

    fordított = mondat[::-1]
    print("Fordítva: ", fordított)

    print("Listába rendezve szavanként: ", mondat.split())
    ################################################################################
    #2.

    x = float(input("Adjon meg egy számot és egy mértékegységet (сm/inch):\n"))
    mertek_e = str(input())

    if mertek_e == "cm":
        x *= 0.39
        print(x, "inches")
    elif mertek_e == "inch":
        x *= 2.54
        print(x, "cm")
    else:
        print("Not correct unit!")

if __name__ == "__main__":
    main()
