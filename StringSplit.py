from dataclasses import fields


profil = "Rashford*Pemain-Bola*19"
fields = profil.split("*")
print(fields)

pekerjaan = fields[1].split("-")
print(pekerjaan)