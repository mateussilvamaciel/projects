number = int(input("Digite o numero secreto: "))

number_secret = 777
counter = 1

while number != number_secret :
    counter += 1
    number = int(input("Numero incorreto digite outro numero: "))
    print("tentativa: ", counter)

print("Numero secreto é: ", number , "Você usou ", counter," tentativas")