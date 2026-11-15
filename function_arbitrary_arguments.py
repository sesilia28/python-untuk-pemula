# Arbitrary Arguments dengan nama names
def belajar_python(*names):
    for name in names:
        print("Halo, Saya %s" % name)
belajar_python("Sesilia", "Dina", "Rani")
