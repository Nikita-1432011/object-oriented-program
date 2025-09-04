class parrot:
    species = "bird"

    def __init__(self,name,age):
        self.name = name
        self.age = age

Blu = parrot("Blu",10)
Woo = parrot("Woo",15)

print(f"Blu is a {(Blu.species)}")
print(f"Woo is also a {(Woo.species)}")
print("{} is {} years old".format(Blu.name,Blu.age))
print("{} is {} years old".format(Woo.name,Blu.age))