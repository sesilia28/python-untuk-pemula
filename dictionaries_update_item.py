firstPerson = {
    "first_name": "Sesilia",
    "last_name": "Marei",
    "kelas": "XI RPL"
}
# Cara pertama mengubah value dengan key
firstPerson["kelas"] = "XI RPL A"
# Cara kedua dengan method update
# Jika key sudah ada maka value diubah, jika belum ada maka item baru ditambahkan
firstPerson.update({"kelas": "XI RPL B"})
firstPerson.update({"hair_color": "black"})
print(firstPerson)
