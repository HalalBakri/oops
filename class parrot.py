class Parrot:
    species = "Bird"
    def __init__(self, name, age):
        self.name = name
        self.age = age
parrot1 = Parrot("Polly", 3)
parrot2 = Parrot("Kiki", 5)
print("Species:", Parrot.species)
print("Parrot 1 - Name:", parrot1.name, ", Age:", parrot1.age)
print("Parrot 2 - Name:", parrot2.name, ", Age:", parrot2.age)
