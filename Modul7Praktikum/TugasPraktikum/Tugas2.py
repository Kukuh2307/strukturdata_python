def cariMahasiswa(listData,item):
    index = 0
    while index <= max(listData): 
        if listData[index] == listData[item]:
            output = str(item) + (" ditemukan")
        else:
            index += 1
            output = str(item) + (" Tidak ditemukan")
    return output

dataMahasiswa = {
    1234:{'nama':'vara','kelas':'2A'},
    1235:{'nama':'amel','kelas':'2B'},
    1236:{'nama':'aurel','kelas':'2C'},
    1237:{'nama':'raya','kelas':'2D'}
}

print(cariMahasiswa(dataMahasiswa,1234))