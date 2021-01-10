class Spiel:
    pass

class Spielfeld:

    #die Klassenvariablen bilden den aktuellen Stand des Spielfeldes ab.
    felder = {
    "A1":1,      # Felderdict 0 = leer, +1 = Spieler 1, -1 = Spieler 2
    "A2":1,
    "A3":-1,
    "B1":-1,
    "B2":1,
    "B3":-1,
    "C1":1,
    "C2":1,
    "C3":-1}

    feld = {
    "A1":"",  # Felderdict mit Strings für die Darstellung des Spielfelds wird nach jedem Zug aus Felder befüllt
    "A2":"",
    "A3":"",
    "B1":"",
    "B2":"",
    "B3":"",
    "C1":"",
    "C2":"",
    "C3":""}

    
    @staticmethod
    def fuellfeld():
        for x in Spielfeld.felder:
            
            if Spielfeld.felder[x] == 1:
                Spielfeld.feld[x] = "X"
                print(x, "X")
            elif Spielfeld.felder[x] == -1:
                Spielfeld.feld[x] = "O"
                print(x, "O")
                
            else:
                Spielfeld.feld[x] = " "
                print(x, "nix")

    @staticmethod
    def feldaufbau():
        print("  | A | B | C")
        print("--+---+---+--")
        print(" 1| {0:s} | {1:s} | {2:s}".format(Spielfeld.feld["A1"], Spielfeld.feld["B1"], Spielfeld.feld["C1"]))
        print("--+---+---+--")
        print(" 2| {0:s} | {1:s} | {2:s}".format(Spielfeld.feld["A2"], Spielfeld.feld["B2"], Spielfeld.feld["C2"]))
        print("--+---+---+--")
        print(" 3| {0:s} | {1:s} | {2:s}".format(Spielfeld.feld["A3"], Spielfeld.feld["B3"], Spielfeld.feld["C3"]))

class Spielzug:
    
    spzg = []
    winlist=(("A1", "A2",  "A3"),  ("B1", "B2", "B3"), ("C1", "C2", "C3"), ("A1", "B1", "C1"),  ("A2", "B2", "C2"),  ("A3", "B3", "C3"), ("A3", "B2", "C1"), ("A1", "B2", "C3"))


    def __init__(self, spieler, nr):
        self.spieler = spieler
        self.nr = nr
        
        Spielzug.spzg.append(self)
    
    @staticmethod
    def summe(sum1, sum2, sum3):
        summ = sum1+sum2+sum3
        return summ
    
    @staticmethod
    def winpruef():
        for tripel in Spielzug.winlist:
            
            f1 = tripel[0]
            f2 = tripel[1]
            f3 = tripel[2]            
            
            w1 = Spielfeld.felder[f1]
            #print("Wert v W1: ", w1)
            w2 = int(Spielfeld.felder[f2])
            w3 = int(Spielfeld.felder[f3])
            
            z = Spielzug.summe(w1,  w2,  w3)
            #print("Summe der w Werte: ", z)
            if z == 3:
                nowin = False
                break
            elif z == -3:
                nowin = False
                break
            else:
                nowin = True
        print("wert von  Nowin:", nowin)
        return nowin

    @staticmethod
    def vollpruef():
        vp = True
        for spf in Spielfeld.felder:            
            if spf != 0:
                vp +=1
        if vp == 9:
            return False
        else:
            return True
    
    @staticmethod
    def korrfeld(zug):    # Sub - Funktion des Eingabeprüfungsloop in Zugpruefvorausf: Beantwortet die Frage ob das eingegebene Feld überhaupt existiert
        if zug not in Spielfeld.felder:
            print("Bitte geben Sie ein gültiges Feld ein")
            return False
        else:
            return True

    @staticmethod
    def belegtesfeld(zug):   # Sub - Funktion des Eingabeprüfungsloop in Zugpruefvorausf: Beantwortet die Frage ob das eingegebene Feld schon belegt ist
        if Spielfeld.felder.get(zug) != 0:
            print("Das Feld ist bereits belegt")
            return False
        else:
            return True
    
    @staticmethod
    def Zugpruefvorausf(zug):
        wdh = True      # Variable zum prüfen ob 
        while wdh:      # Eingabeprüfungsloop: kontrolliert ob die Eingabe korrekt ist.
            kf = Spielzug.korrfeld(zug)
            if kf == True:
                bf = Spielzug.belegtesfeld(zug)
                if bf == True:
                    wdh = False
        return True

class Spieler:
    
    splist = []

    def __init__(self, name, nr, zeichen):
        self.name = name
        self.nr = nr
        self.zeichen = zeichen

        Spieler.splist.append(self)


if __name__ == '__main__':

    sp1 = Spieler("Nummer 1", 1, "X")
    sp2 = Spieler("Nummer 2", 2, "O")
    print(Spieler.splist)
    
    zug = ""

    while True:

        for spieler in Spieler.splist:

            if Spielzug.winpruef or Spielzug.vollpruef:
                print("Spielabbruch weil Abbruchbedingung erfüllt")
                break
            else:
                print("Spieler " + spieler.name + " ist an der Reihe")
                print("")
                Spielfeld.fuellfeld()
                Spielfeld.feldaufbau()
                input("Dein Zug:", zug)
                # Jetzt werden die Zugprüfungsmethoden der Spielzug Klasse aufgerufen und anschließend eine neue Spielzuginstanz kreiert.
                


    Spielfeld.fuellfeld()
    Spielfeld.feldaufbau()
