intervalo=0
fora=0
for x in range(10):
    num=int(input("Digite um número:"))
    if num < 10 or num > 20:
        fora+=1
    else:
        intervalo+=1