#wyrazenia reguralne c.d

import re

if re.match("^[A-Z][a-z]*$", "ALa"):
    print("Dopasowano!")
else:
    print("Nie dopasowano!")

if re.match("^[A-Z][a-z]+$", "ALa"):
    print("Dopasowano!")
else:
    print("Nie dopasowano!")

if re.match("^[A-Z][a-z]?[A-Z]$", "ALa"):
    print("Dopasowano!")
else:
    print("Nie dopasowano!")

if re.match("^[A-Z][a-z]{2, 5}$", "ALa"):
    print("Dopasowano!")
else:
    print("Nie dopasowano!")