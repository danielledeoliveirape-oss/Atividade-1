maior_altura = 0
menor_altura = None

soma_masculino = 0
quantidade_masculino = 0

quantidade_feminino = 0

for i in range(15):
    print(f"\n--- Pessoa {i + 1} ---")

    altura = float(input("Digite a altura (ex: 1.75): ").replace(",", "."))
    genero = input("Digite o gênero (M para Masculino / F para Feminino): ").upper()

    # Verifica a maior altura do grupo
    if altura > maior_altura:
        maior_altura = altura

    # Verifica a menor altura do grupo
    if menor_altura is None or altura < menor_altura:
        menor_altura = altura

    # Dados do gênero masculino
    if genero == "M":
        soma_masculino += altura
        quantidade_masculino += 1

    # Conta pessoas do gênero feminino
    elif genero == "F":
        quantidade_feminino += 1


# Calcula a média das alturas masculinas
if quantidade_masculino > 0:
    media_masculino = soma_masculino / quantidade_masculino
else:
    media_masculino = 0


print("\n===== RESULTADOS =====")

print(f"Maior altura do grupo: {maior_altura:.2f} m")
print(f"Menor altura do grupo: {menor_altura:.2f} m")

if quantidade_masculino > 0:
    print(f"Média das alturas masculinas: {media_masculino:.2f} m")
else:
    print("Não foram informadas pessoas do gênero masculino.")

print(f"Número de pessoas do gênero feminino: {quantidade_feminino}")