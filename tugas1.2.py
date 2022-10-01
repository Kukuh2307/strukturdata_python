def kalkulator(angka1,angka2,option):
  if option == '+':
    return angka1 + angka2
  elif option == '-':
    return angka1 - angka2
  elif option == '/':
    return angka1/angka2
  elif option == '*':
    return angka1 * angka2
  else: print('format option salah')

print('=========================================')
print('                 KALKULATOR              ')
print('=========================================')
angka1 = int(input('masukkan angka ke 1: '))
angka2 = int(input('masukkan angka ke 2: '))
option = input('masukkan option(+,-,/,*): ')
print(kalkulator(angka1,angka2,option))
