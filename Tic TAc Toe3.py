# Tic Tac Toe

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
    
    def pruefen(zug):
        pass
        


    def zeichensetzen(self,  zug):
        print(zug)
        print(spiel1.felder)
        spiel1.felder[zug] = 1
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
            print(tripel[1])
            f1 = tripel[0]
            f2 = tripel[1]
            f3 = tripel[2]
            print("Feldwert F1: ", f1)
            print("FeldtypF1: ", type(f1))
            print("Wert F2:",  f2)
            print("wert F3", f3)
            
            
            w1 = spiel1.felder[f1]
            print("Wert v W1: ", w1)
            w2 = int(spiel1.felder[f2])
            w3 = int(spiel1.felder[f3])
            
            z = self.summe(w1,  w2,  w3)
            print("Summe der w Werte: ", z)
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

class Player:
    
    players = []
    
    def __init__(self, playername, playernr, playersign):
        self.playername = playername
        self.playernr = playernr
        self.playersign = playersign
        
        spiel1.players.append([weakref.ref(self), playername, playernr,  playersign])



if __name__=='__main__':
    
    spiel1 = Spielfeld()
    spieler1 = Player("Michi", 1, "X")
    spieler2 = Player("Muschi", 2, "O")
    korrzug = True
    fliste  = []
    spielzug1 = Spielzug("spieler1", 1)
       
    
    while korrzug:
        
        aktZug = input("Ihr Zug:")
        if aktZug not in spiel1.felder:
            print("Bitte geben Sie ein gültiges Feld ein")
        else:
            print("Sie haben ",  aktZug,  " eingegeben. Dies ist ein gültiges Feld")
            korrzug = False
            
    spielzug1.zeichensetzen(aktZug)
    
    spiel1.felderfuellen()
    
    if not spielzug1.winpruef():
        print("GEWONNEN")
    
    
    print(spiel1.felder)
    print(spiel1.fuellfeld)
    print(spiel1.players)
    print()
