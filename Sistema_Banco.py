import os
from datetime import date


class ContaBancaria:
    LIMITE_SAQUES_DIARIOS = 3
    LIMITE_VALOR_SAQUE = 500.00

    def __init__(self, titular, agencia, numero_conta, banco, saldo_inicial=0):
        self.titular = titular
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.banco = banco
        self.saldo = saldo_inicial
        self.extrato = []
        self.extrato.append(f"Saldo inicial: R${self.saldo:.2f} ({date.today()})")
        self.saques_hoje = 0
        self.data_ultimo_saque = None

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: +R${valor:.2f} ({date.today()})")
            print("Depósito realizado com sucesso.")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        hoje = date.today()

        if self.data_ultimo_saque != hoje:
            self.saques_hoje = 0
            self.data_ultimo_saque = hoje

        if valor <= 0:
            print("Valor de saque inválido.")
        elif valor > ContaBancaria.LIMITE_VALOR_SAQUE:
            print(f"Limite de saque por operação é de R${ContaBancaria.LIMITE_VALOR_SAQUE:.2f}.")
        elif self.saques_hoje >= ContaBancaria.LIMITE_SAQUES_DIARIOS:
            print(f"Limite de {ContaBancaria.LIMITE_SAQUES_DIARIOS} saques diários atingido.")
        elif self.saldo >= valor:
            self.saldo -= valor
            self.extrato.append(f"Saque: -R${valor:.2f} ({date.today()})")
            self.saques_hoje += 1
            print("Saque realizado com sucesso.")
            print(f"Saldo atual: R${self.saldo:.2f}\n")
        else:
            print("Saldo insuficiente.")

    def visualizar_extrato(self):
        print(f"\nExtrato da conta de {self.titular} - Agência: {self.agencia} - Conta: {self.numero_conta} - Banco: {self.banco}:")
       
        if len(self.extrato) == 1:
            print("Não foram realizadas movimentações.")
        else:
            for operacao in self.extrato:
                print(operacao)
        print(f"Saldo atual: R${self.saldo:.2f}\n")


def limpar_tela():
    os.system('cls')

def menu():
    print("\nBem-vindo ao Sistema Bancário do Banco do Brasil!")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Visualizar Extrato")
    print("4 - Sair")
    return input("\nEscolha uma opção: ")

if __name__ == "__main__":
    conta_atual = ContaBancaria(
        titular="Thiago Bernado",
        agencia="0001",
        numero_conta="12345-6",
        banco="Banco do Brasil",
        saldo_inicial=500.00
    )
    print(f"Bem-vindo, {conta_atual.titular}! Sua conta foi carregada.")

    while True:
        opcao = menu()
        if opcao == '1':
            limpar_tela()
            valor_deposito = float(input("Digite o valor para depositar: "))
            conta_atual.depositar(valor_deposito)
            input("\nPressione Enter para voltar ao menu")
            limpar_tela()
        elif opcao == '2':
            limpar_tela()
            valor_saque = float(input("Digite o valor para sacar: "))
            conta_atual.sacar(valor_saque)
            input("\nPressione Enter para voltar ao menu")
            limpar_tela()
        elif opcao == '3':
            limpar_tela()
            conta_atual.visualizar_extrato()
            input("\nPressione Enter para voltar ao menu")
            limpar_tela()
        elif opcao == '4':
            limpar_tela()
            print("Obrigado por usar o Banco do Brasil!")
            break
        else:
            limpar_tela()
            print("Opção inválida. Por favor, tente novamente.")
            input("\nPressione Enter para voltar ao menu")
            limpar_tela()