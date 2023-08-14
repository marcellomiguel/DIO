class Banco:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial
        self.extrato = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: +{valor}")
            print(f"Depósito de R${valor} realizado com sucesso.")
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            self.extrato.append(f"Saque: -{valor}")
            print(f"Saque de R${valor} realizado com sucesso.")
        else:
            print("Saldo insuficiente ou valor inválido para saque.")

    def visualizar_extrato(self):
        print("Extrato:")
        for item in self.extrato:
            print(item)
        print(f"Saldo atual: R${self.saldo}")


def main():
    banco = Banco()

    while True:
        print("\nOpções:")
        print("1 - Depositar")
        print("2 - Sacar")
        print("3 - Visualizar Extrato")
        print("4 - Sair")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            valor = float(input("Digite o valor a ser depositado: "))
            banco.depositar(valor)
        elif opcao == 2:
            valor = float(input("Digite o valor a ser sacado: "))
            banco.sacar(valor)
        elif opcao == 3:
            banco.visualizar_extrato()
        elif opcao == 4:
            print("Saindo...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")


if __name__ == "__main__":
    main()
