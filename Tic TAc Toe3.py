# Tic Tac Toe

from os import truncate
import weakref


class Spielfeld:

    def __init__(self):
    
        self.felder = {
        "A1":0,      # Felderdict 0 = leer, +1 = Spieler 1, -1 = Spieler 2
        "A2":0,
        "A3":-1,
        "B1":0,
        "B2":1,
        "B3":-1,
        "C1":0,
        "C2":1,
        "C3":0}

        self.fuellfeld = {
        "A1":"",  # Felderdict mit Strings für die Darstellung des Spielfelds wird nach jedem Zug aus Felder befüllt
        "A2":"",
        "A3":"",
        "B1":"",
        "B2":"",
        "B3":"",
        "C1":"",
        "C2":"",
        "C3":""}
        
        self.players = []
        
    def felderfuellen(self):    # Methode um Fuellfeld mit "X" und "O" Strings zu befüllen 
        for x in self.felder:
            
            if self.felder[x] == 1:
                self.fuellfeld[x] = "X"
                print(x, "X")
            elif self.felder[x] == -1:
                self.fuellfeld[x] = "O"
                print(x, "O")
                
            else:
                self.fuellfeld[x] = ""
                print(x, "nix")


class Spielzug:

    winlist=(("A1", "A2",  "A3"),  ("B1", "B2", "B3"), ("C1", "C2", "C3"), ("A1", "B1", "C1"),  ("A2", "B2", "C2"),  ("A3", "B3", "C3"), ("A3", "B2", "C1"), ("A1", "B2", "C3"))

    def __init__(self, player, zugnr):
        self.player = player
        self.zugnr = zugnr
        self.zug = ""
    
    def zeichensetzen(self,  zug, plwert):
        print(zug)
        print(spiel1.felder)
        spiel1.felder[zug] = plwert
        print(spiel1.felder)

    def listefuehren(self):
        pass
        
    def summe(self, sum1, sum2, sum3):
        summ = sum1+sum2+sum3
        return summ
        
    def winpruef(self):
        """if spiel1.felder["A1"+"A2"+"A3"]==3 or spiel1.felder["A1"+"A2"+"A3"]==-3:
            nowin = False
        elif spiel1.felder["B1"+"B2"+"B3"]==3 or spiel1.felder["B1"+"B2"+"B3"]==-3:
            nowin = False
        elif spiel1.felder["C1"+"C2"+"C3"]==3 or spiel1.felder["C1"+"C2"+"C3"]==-3:
            nowin = False
        elif spiel1.felder["A1"+"B1"+"C1"]==3 or spiel1.felder["A1"+"B1"+"C1"]==-3:
            nowin = False
        elif spiel1.felder["A2"+"B2"+"C2"]==3 or spiel1.felder["A2"+"B2"+"C2"]==-3:
            nowin = False
        elif spiel1.felder["A3"+"B3"+"C3"]==3 or spiel1.felder["A3"+"B3"+"C3"]==-3:
            nowin = False
        elif spiel1.felder["A1"+"B2"+"C3"]==3 or spiel1.felder["A1"+"B2"+"C3"]==-3:
            nowin = False
        elif spiel1.felder["A3"+"B2"+"C1"]==3 or spiel1.felder["A3"+"B2"+"C1"]==-3:
            nowin = False
        else:
            nowin = True"""
        
        
        
        for tripel in Spielzug.winlist:
            #print(tripel[1])
            f1 = tripel[0]
            f2 = tripel[1]
            f3 = tripel[2]
            """print("Feldwert F1: ", f1)
            print("FeldtypF1: ", type(f1))
            print("Wert F2:",  f2)
            print("wert F3", f3)"""
            
            
            w1 = spiel1.felder[f1]
            #print("Wert v W1: ", w1)
            w2 = int(spiel1.felder[f2])
            w3 = int(spiel1.felder[f3])
            
            z = self.summe(w1,  w2,  w3)
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

    def vollpruef(self):
        vp = True
        for spf in spiel1.felder:            
            if spf != 0:
                vp +=1
        if vp == 9:
            return False
        else:
            return True
    
    def korrfeld(self, zug):    # Sub - Funktion des Eingabeprüfungsloop in Zugpruefvorausf: Beantwortet die Frage ob das eingegebene Feld überhaupt existiert
        if zug not in spiel1.felder:
            print("Bitte geben Sie ein gültiges Feld ein")
            return False
        else:
            return True
    
    def belegtesfeld(self, zug):   # Sub - Funktion des Eingabeprüfungsloop in Zugpruefvorausf: Beantwortet die Frage ob das eingegebene Feld schon belegt ist
        if spiel1.felder.get(zug) != 0:
            print("Das Feld ist bereits belegt")
            return False
        else:
            return True
    
    def Zugpruefvorausf(self, zug):
        wdh = True      # Variable zum prüfen ob 
        while wdh:      # Eingabeprüfungsloop: kontrolliert ob die Eingabe korrekt ist.
            kf = spielzug1.korrfeld(zug)
            if kf == True:
                bf = spielzug1.belegtesfeld(zug)
                if bf == True:
                    wdh = False
        return True
        






class Player:
    
    Players = []
    
    def __init__(self, playername, playernr, playersign):
        self.playername = playername
        self.playernr = playernr
        self.playersign = playersign
        
        Player.Players.append(self) 



if __name__=='__main__':
    
    spiel1 = Spielfeld()
    spieler1 = Player("Michi", 1, "X")
    spieler2 = Player("Muschi", -1, "O")
    korrzug = True
    fliste  = []
    spielzug1 = Spielzug("spieler1", 1)
    aktZug = ""
           
    print(Player.Players)
    print("winprüf = ", spielzug1.winpruef())
    print("vollprüf =", spielzug1.vollpruef())
    
    while spielzug1.winpruef() or not spielzug1.vollpruef():
        
        for pl in Player.Players:
            if spielzug1.winpruef() == True:

                print("{} ist am Zug!".format(pl.playername))
                print("######################################################")        
             
            while korrzug:
                
                aktZug = input("Ihr Zug: ")
                if aktZug not in spiel1.felder:
                    print("Bitte geben Sie ein gültiges Feld ein")

                elif spiel1.felder.get(aktZug) != 0:
                    print("Das Feld ist bereits belegt, wählen Sie ein anderes aus!")

                else:
                    print("Sie haben ",  aktZug,  " eingeAgeben. Dies ist ein gültiges Feld")
                    korrzug = False
                
                spielzug1.zeichensetzen(aktZug, pl.playernr)
        
                spiel1.felderfuellen()
        
                if not spielzug1.winpruef():
                    print("GEWONNEN")
                    break
    
    
    print(spiel1.felder)
    print(spiel1.fuellfeld)
    print(Player.Players)
    print()
