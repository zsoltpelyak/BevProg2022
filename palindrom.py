def isPalindrome(str):
    for i in range(0, int(len(str) / 2)):
        if str[i] != str[len(str) - i - 1]:
            return False
    return True

s = str(input("Írd be amit meg szeretnél vizsgálni, hogy palindrom-e: "))
ans = isPalindrome(s)

if (ans):
    print("Yes")
else:
    print("No")