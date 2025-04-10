negativos = 0

for i in range(1, 11, 1):
    number = int(input("Digite um número:"))
    if number < 0:
        negativos += 1

print(f"{negativos} números foram negativos.")
