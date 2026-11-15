# Arbitrary Keyword Arguments
def belajar_python(**student):
    print("Halo, Saya %s. Nilai saya %d" % (student["name"], student["nilai"]))
belajar_python(nilai=88, name="Sesilia")
