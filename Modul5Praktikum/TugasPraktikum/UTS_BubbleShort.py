def BubbleSort(huruf,angka):
    n = len(huruf)-1
    for i in range (n):
        for j in range(n):
            # jika ingin sorting secara desc tinggal mengubah lebih besar menjadi lebih kecil
            if huruf[j] > huruf[j+1]: 
                # swap langsung
                huruf[j], huruf[j+1] = huruf[j+1],huruf[j]
                angka[j], angka[j+1] = angka[j+1],angka[j]
                strHuruf = str(huruf)
                strAngka = str(angka)
        print(f'tahap {i+1}\n'+strHuruf+'\n'+strAngka)

mahasiswa = ["K","U","K","H","U","H","A","G","U","N","G","P"]
npm = [2,1,1,3,0,2,0,2,8,1,0,0]
print("Sebelum di shortin diurutkan berdasarkan huruf secara asc\n",mahasiswa,"\n",npm)
BubbleSort(mahasiswa,npm)
print("Selesai\n",mahasiswa,"\n",npm)