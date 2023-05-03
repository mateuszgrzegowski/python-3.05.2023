#metody klas i statyczne metody

class Czlowiek:
 def __init__(self, imie):
    self.imie = imie

 def przedstaw(self):
       print("Nazwywam sie" + self.imie)

 @classmethod
 def nowy_czlowiek(cls, imie):
      return cls(imie)

 @staticmethod
 def przywitaj(arg):
     print("Cześć" + arg)

cz1 = Czlowiek.nowy_czlowiek("Mateusz")
cz1.przedstaw()
cz2 = cz1.nowy_czlowiek("Ania")
cz2.przedstaw()

Czlowiek.przywitaj("przyjacielu!")
