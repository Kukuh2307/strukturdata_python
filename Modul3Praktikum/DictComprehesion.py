# fungsi generate dictionary angka kuadrat

def  angka_kuadrat(jumlah):
    kuadrat = {x: x*x for x in range(jumlah)}
    return print(kuadrat)

angka_kuadrat(7)