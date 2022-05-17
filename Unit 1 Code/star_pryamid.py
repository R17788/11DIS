layers = int(input("How many layers would you like you pryamid to be? "))

print(" " * (layers+1), end="")
print("  *")
print(" " * (layers+1), end="")

for i in range(layers):
    print(" *" * (i+2))
    print(" " * (layers-i), end="")
