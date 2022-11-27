data = [row.strip() for row in open("hazi.txt", "r", encoding="utf-8").readlines()]
data = [row for row in data if len(row) !=0][::3]
cleaned = []

marks= 'aáeéoóöőuúüűiíAÁEÉIÍOÓUÚÜŰÖŐ.!?:-;<>,()"'
nr = ""

for row in data:
    for c in row:
        if c not in marks:
            nr+=c
    cleaned.append(nr)
    nr = ""

print(cleaned)

with open("output.txt", "w") as file:
    for row in cleaned:
        file.write(f"{row}\n")