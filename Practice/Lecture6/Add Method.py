class Animal:
    pass
class Pets(Animal):
    pass
class Dogs(Pets):
    @staticmethod
    def bark():
        print("Bow Bow Bow!!!!")

d= Dogs()
d.bark()
