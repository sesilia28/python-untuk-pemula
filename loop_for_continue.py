# Melewati perulangan jika nilai x adalah angka genap
# Hanya mencetak angka ganjil karena angka genap di-skip dengan continue
for x in range(10):
    if x % 2 == 0:
        continue
    print(x)
