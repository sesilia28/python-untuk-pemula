# Menggunakan package camelcase yang dipasang dengan pip
import camelcase

c = camelcase.CamelCase()
txt = "halo saya sesilia belajar python"
print(c.hump(txt))
