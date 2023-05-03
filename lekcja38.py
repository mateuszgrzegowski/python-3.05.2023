#skrocony operator if,inne zastosowanie if

print("Prawda") if 5 > 2 else print("Nieprawda")

a = "Parzysta" if 10 % 2 == 0 else "Nieparzysta"

print("a")

for i in range(10):
    if i > 5:
        continue
else:
    print("Koniec")

try:
    a = 5/5
except ZeroDivisionError:
    print("bład")
else:
    print("Koniec")
finally:
    print("Zawsze:")