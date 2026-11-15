animals = ["Kucing", "Kelinci", "Burung"]
# Menghapus item tertentu dengan method remove
animals.remove("Kelinci")
print(animals)
# Menghapus item terakhir dengan method pop
animals = ["Kucing", "Kelinci", "Burung"]
animals.pop()
print(animals)
# Menghapus item berdasarkan posisinya dengan pop(0)
animals = ["Kucing", "Kelinci", "Burung"]
animals.pop(0)
print(animals)
# Menghapus semua item dengan method clear
animals = ["Kucing", "Kelinci", "Burung"]
animals.clear()
print(animals)
# Menggabungkan sebuah lists dengan lists lainnya
animals = ["Kucing", "Kelinci", "Burung"]
otherAnimals = ["Ayam", "Bebek", "Sapi"]
animals.extend(otherAnimals)
print(animals)
fruits = ["Apel", "Mangga", "Pisang"]
otherFruits = ["Durian", "Semangka", "Jeruk"]
allFruits = fruits + otherFruits
print(allFruits)
