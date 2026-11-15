# Class Cat dengan constructor __init__
class Cat:
    color = "white"

    def __init__(self, color):
        self.color = color

# Membuat objek baru dengan mengirim nilai color
cati = Cat("gray")
print(cati.color) # gray
