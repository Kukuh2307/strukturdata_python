# Sequential Search
def CariMahasiswa(npm, data):
    for i in range(len(data)):
        if data[i]['npm'] == npm:
            return 'NPM ' + str(data[i]['npm']) + ' Bernama ' + data[i]['nama'] + ' Kelas ' + data[i]['kelas']

    return 'NPM tidak ditemukan'


# Contoh Penggunaan
data = [
    {'npm': 1234, 'nama': 'Vara', 'kelas': '2A'},
    {'npm': 4567, 'nama': 'Lara', 'kelas': '3B'},
    {'npm': 8901, 'nama': 'Dara', 'kelas': '4C'},
]

print(CariMahasiswa(1234, data))  # Output: Vara Kelas 2A
print(CariMahasiswa(4567, data))  # Output: Lara Kelas 3B
print(CariMahasiswa(8901, data))  # Output: Dara Kelas 4C
print(CariMahasiswa(2345, data))  # Output: NPM tidak ditemukan
