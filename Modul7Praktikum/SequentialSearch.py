# fungsi sequential search
def sequentialSearch(listData,item):
    index = 0
    found = False
    while index < len(listData) and not found:
        print("iterasi ke-" + str(index+1))

        if listData[index] == item:
            found = True
        else:
            index += 1

    if found == True:
        output = str(item) + (" Di temukan")
    else:
        output = str(item) + (" Tidak ditemukan")

    return output

# Test data dan panggil fungsi
testlist = [1,2,32,8,17,19,42,13,0]
print(sequentialSearch(testlist,3))
print(" ")
print(sequentialSearch(testlist,13))