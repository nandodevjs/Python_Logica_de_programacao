# if / elif / else
# se / Se não se / se não

# If (condição: o retorno da codição é um bool)

entrada = input("Você deseja entrar ou sair? ")

entrada = entrada.lower()

if entrada == "entrar":
    print(f"Você escolheu {entrada} no sistema")

elif entrada == "sair":
    print(f"Você escolheu {entrada} do sistema ")

elif entrada == "pass":
    pass #Utilizado para passar/pular alguma etapa do código

else:
    print("Escolha entre entrar ou sair")