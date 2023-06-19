names = []
name = input("Enter a name  ")

while name != "END":
    names.append(name)
    print("Name:", name)
    name = input("Enter a name  ")

print("I am done.")

print("Entered names:")
for name in names:
    print(name)
