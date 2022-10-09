def osztas(szam1, szam2):
    try:
        print(szam1 / szam2)
    except ZeroDivisionError:
        print("Division by zero not allowed")
    finally:
        print("Out of try except blocks")

while True:
    szam3 = float(input("Enter 'a' value: "))
    szam4 = float(input("Enter 'b' value: "))
    osztas(szam3, szam4)
