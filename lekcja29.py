#ukrywanie danych -klasy hermetyzacja
class Test:
  _lista = []
  def dodaj(self, arg):
       self._lista.append(arg)

  def zdejmij(self):
       if len(self._lista) > 0:
           return self._lista.pop(len(self._lista) - 1)
       else:
           return

obj = Test()
obj.dodaj("A")
obj.dodaj("B")
obj.dodaj("C")
print(obj.zdejmij())
print(obj._lista)