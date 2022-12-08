# Kelas Stack untuk menyimpan angka-angka biner
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

# Fungsi untuk mengkonversi angka desimal ke biner
def decToBin(decimal):
    # Inisialisasi kelas Stack dan variabel hasil
    stack = Stack()
    result = ""

    # Lakukan pembagian sampai hasilnya 0
    while decimal > 0:
        # Tambahkan sisa pembagian ke dalam kelas Stack
        stack.push(str(decimal % 2))
        decimal = decimal // 2

    # Bangkitkan string biner dengan mengambil angka dari kelas Stack
    while not stack.isEmpty():
        result += stack.pop()

    return result

# Konversi angka desimal ke biner
print(decToBin(10))  # 1010
print(decToBin(42))  # 101010