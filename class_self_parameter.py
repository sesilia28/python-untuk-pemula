# Mengubah penamaan parameter self dengan nama myParam
class Cat:
    color = "white"

    def say(myParam):
        print("My color is %s" % myParam.color)

# Membuat objek baru
cati = Cat()

# Memanggil method di dalam Class
cati.say()
