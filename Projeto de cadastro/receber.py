def receberInteiro():
    while True:
        try:
            valor = int(input("Digite um número inteiro: "))
            return valor
        except ValueError:
            print("Por favor, digite um número inteiro válido.")

def receberString():
    while True:
        try:
            valor = input("Digite um texto: ")
            return valor
        except ValueError:
            print("Por favor, digite um texto válido.")



            