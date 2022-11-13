def  angka_kuadrat(jumlah):
    kuadrat = {x: x*x for x in range(jumlah)if x%2==1}
    return print(kuadrat)

angka_kuadrat(7)