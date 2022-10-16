class Team:
    def __init__(self, name, project, role):
        self.name = name
        self.project = project
        self.role = role
        print(self)

    def __str__(self):
        return f"-- Developer Létrehozva. --\n{self.name} a {self.project}-en dolgozik {self.role} szerepkörben."

    def getName(self):
        return self.name
    def getProject(self):
        return self.project
    def getPost(self):
        return self.role


dolgozok = []

dolgozo1 = dolgozok.append(Team("Ricsi", "SolArch", "Frontend"))
dolgozo2 = dolgozok.append(Team("Angéla", "ZerTeng", "Tesztelő"))
dolgozo3 = dolgozok.append(Team("Peti", "KefERP", "Backend"))
dolgozo4 = dolgozok.append(Team("Éva", "KefERP", "Frontend"))

seen = []
for i in dolgozok:
    for j in dolgozok:
        if i.getProject() == j.getProject() and i.getName() != j.getName() and str(i.getName() + ":" + j.getName()) not in seen:
            print(i.getName() + " és " + j.getName() + " dolgoznak egy projekten.")
            seen.append(i.getName() + ":" + j.getName())
            seen.append(j.getName() + ":" + i.getName())