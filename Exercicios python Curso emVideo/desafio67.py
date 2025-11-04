from time import sleep
Tabuada = 0
resultado = 0
while True:
    Tabuada = int(input("Digite a tabuada que voce quer ver:"))
    if Tabuada <= -1:
        sleep (1)
        print("Progama finalizado")
        break
    else:
        for c in range (1, 11):
            sleep(0.5)
            print(f"{Tabuada} x {c} = {resultado}")
            c += 1
            resultado = Tabuada * c
    
