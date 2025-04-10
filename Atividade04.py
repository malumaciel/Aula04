n = int(input("Digite o número"))
if n <= 0:
    print("invalido")
else:
    for x in range(1, n, 1):
        print(x, end= "  ")