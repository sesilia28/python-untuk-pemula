# Membuat Dictionaries untuk menyimpan biodata seseorang
firstPerson = {
    "first_name": "Sesilia",
    "last_name": "Marei",
    "kelas": "XI RPL"
}
# Mengakses item pada Dictionaries dengan 2 cara
# Cara pertama
print(firstPerson["first_name"]) # Sesilia
# Cara kedua dengan method get
print(firstPerson.get("kelas")) # XI RPL
# Mendapatkan semua keys dari Dictionaries
print(firstPerson.keys())
