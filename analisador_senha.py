senha = input("Digite sua senha: ")

print("Quantidade de caracteres:", len(senha))

for letra in senha:
    print(letra)
    
tem_maiuscula = False
tem_minuscula = False
tem_numero = False
tem_especial = False

for letra in senha:
    if letra.isupper():
        tem_maiuscula = True

    if letra.islower():
        tem_minuscula = True

    if letra.isdigit():
        tem_numero = True

    if not letra.isalnum():
        tem_especial = True


pontos = 0

pontos = 0

if tem_maiuscula:
    pontos += 1

if tem_minuscula:
    pontos += 1

if tem_numero:
    pontos += 1

if tem_especial:
    pontos += 1

if len(senha) >= 12:
    pontos += 1

if pontos <= 2:
    forca = "Fraca"

elif pontos == 3:
    forca = "Média"

else:
    forca = "Forte"



print("\n========== RESULTADO ==========")

print(f"Força da senha: {forca}")

print(f"✔ Quantidade de caracteres: {len(senha)}")

print(f"Maiúscula: {'✔ Sim' if tem_maiuscula else '❌ Não'}")
print(f"Minúscula: {'✔ Sim' if tem_minuscula else '❌ Não'}")
print(f"Número: {'✔ Sim' if tem_numero else '❌ Não'}")
print(f"Especial: {'✔ Sim' if tem_especial else '❌ Não'}")

print(f"\nPontuação: {pontos}/5")

print("\nSugestões para melhorar:")

if len(senha) < 12:
    print("- Utilize pelo menos 12 caracteres.")

if not tem_maiuscula:
    print("- Adicione pelo menos uma letra maiúscula.")

if not tem_minuscula:
    print("- Adicione pelo menos uma letra minúscula.")

if not tem_numero:
    print("- Adicione pelo menos um número.")

if not tem_especial:
    print("- Adicione pelo menos um caractere especial (@, #, $, %, &, !...).")

# Caso a senha atenda a todos os requisitos
if (
    len(senha) >= 12
    and tem_maiuscula
    and tem_minuscula
    and tem_numero
    and tem_especial
):
    print("Parabéns! Sua senha atende todos os requisitos.")