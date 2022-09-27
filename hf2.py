def main():
    print("Adja meg a háromszög három oldalát cm-ben: ")
    a = int(input("a oldal (cm): "))
    b = int(input("b oldal (cm): "))
    c = int(input("c oldal (cm): "))

    if (a + b) > c:
        if (a + c) > b:
            if (b + c) > a:
                print("A", a, b, "és", c, "oldalú háromszög szerkeszthető.")
            else:
                print("A", a, b, "és", c, "oldalú háromszög NEM szerkeszthető.")
        else:
            print("A", a, b, "és", c, "oldalú háromszög NEM szerkeszthető.")
    else:
        print("A", a, b, "és", c, "oldalú háromszög NEM szerkeszthető.")

if __name__ == "__main__":
    main()