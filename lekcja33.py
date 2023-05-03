#wyrazenia reguralne c.d

import re

if re.match("^[A-Z]o.$", "kot"):
    print("Dopasowano!")
else:
    print("Nie dopasowano!")