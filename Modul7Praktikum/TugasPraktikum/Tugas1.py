def cariMahasiswa(listData,item):
    cari = str(item)
    index = 0
    found = False
    while index < len(listData) and not found:
        looping = index +1
        print("iterasi ke-" + str(looping))

        if listData[looping] == listData[item]:
            found = True
            output = str(item) + (" Di temukan "+str(listData[item]['nama']+ str(len(listData)))) + str(listData[looping]['npm']) + str(listData[item]['npm'])
            
        else:
            index += 1
            output = str(item) + (" Tidak ditemukan")

    return output

def tampildata(array,item):
    index = 0
    if array[item] == array[index]:
        output = print(array[item]['nama'])
    else:
        index += 1
    return output

dataMahasiswa = {
    1234:{'nama':'vara','kelas':'2A'},
    1235:{'nama':'amel','kelas':'2B'},
    1236:{'nama':'aurel','kelas':'2C'},
    1237:{'nama':'raya','kelas':'2D'}
}

Mahasiswa = {
    1:{'npm':1234,'nama':'vara','kelas':'2A'},
    2:{'npm':1235,'nama':'amel','kelas':'2B'},
    3:{'npm':1236,'nama':'aurel','kelas':'2C'},
    4:{'npm':1237,'nama':'raya','kelas':'2D'}
}
# print("Bernama " + dataMahasiswa.get(1234).get('nama','nama tidak di temukan'))
# print("Kelas " + dataMahasiswa.get(1234).get('kelas','nama tidak di temukan'))
# print(Mahasiswa[1]['nama'])
print(cariMahasiswa(Mahasiswa,3))
print(Mahasiswa[2]['npm'])

