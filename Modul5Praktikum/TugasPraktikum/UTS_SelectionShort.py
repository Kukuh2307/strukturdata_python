def SelectionSort(huruf,angka):
    n = len(angka)
    for i in range (n):
        index = i
        for j in range (i+1,n):
            # jika ingin sorting secara desc tinggal mengubah lebih besar menjadi lebih kecil
            if angka[j] < angka[index]:
                index = j
                angka[i], angka[index] = angka[index], angka[i]
                huruf[i], huruf[index] = huruf[index], huruf[i]
                strHuruf = str(huruf)
                strAngka = str(angka)
        print(f'tahap {i+1}\n'+strHuruf+'\n'+strAngka)

mahasiswa = ["B","R","I","L","I","A","N","T","A","P","R","I","L","I","O"]
npm = [2,1,1,3,0,2,0,2,7,3]
print("Sebelum di shortin diurutkan berdasar npm secara asc\n",mahasiswa,"\n",npm)
SelectionSort(mahasiswa,npm)
print("Selesai\n",mahasiswa,"\n",npm)