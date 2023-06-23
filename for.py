# Loop For
for i in range(5):# Argumento tamanho do array
    print("O valo de i é atualmente", i)

for i in range(2, 8):# primeiro argumento- Valor inicial é o inicio, segundo é o tamanho
    print("O valor de i é atualmente", i)

for i in range(2, 10, 3):# primeiro argumento- Valor inicial é o inicio, segundo é o tamanho e terceiro é um incremento
    print("O valor de i é atualmente", i)

# break - exemplo

print("The break instrução:")
for i in range(1, 6):
    if i == 3:
        break
    print("Dentro do laço.", i)
print("Fora do loop.")


# continue - exemplo

print("The continue instrução:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Dentro do laço.", i)
print("Fora do loop.")