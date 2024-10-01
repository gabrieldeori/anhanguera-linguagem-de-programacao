print("Bem-Vindo a máquina de vendas automática de ingressos de cinema!")

idade = int(input("Por favor, digite sua idade: \n"))

if idade < 12:
    print("Recomendamos:")
    print("1. Filme A;")
    QUANTIDADE_INGRESSOS = 5
    if QUANTIDADE_INGRESSOS > 0:
        print("Ingressos disponíveis.")


elif idade < 18:
    print("Recomendamos:")
    print("2. Filme B;")
    QUANTIDADE_INGRESSOS = 9
    if QUANTIDADE_INGRESSOS > 0:
        print("Ingressos disponíveis.")

else:
    print("Recomendamos:")
    print("3. Filme C;")
    QUANTIDADE_INGRESSOS = 0
    if QUANTIDADE_INGRESSOS > 0:
        print("Ingressos disponíveis.")
