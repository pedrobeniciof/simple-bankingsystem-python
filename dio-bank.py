import sys
import time

nomeBanco = ("DioBank".center(63,"-"))
linhaBranca = ("".center(63,"-"))
menu = f"""
{nomeBanco}

Selecione a opção abaxio conforme sua operação.

[1] - Saque
[2] - Depósito
[3] - Extrato
[4] - Sair

{linhaBranca}
"""
menuProximo = f"""
Deseja realizar outra operação?

[1] - Saque
[2] - Depósito
[3] - Extrato
[4] - Sair

{linhaBranca}
"""
menuErro = f"""

A opção selecionada não existe, tente novamente.

[1] - Saque
[2] - Depósito
[3] - Extrato
[4] - Sair

{linhaBranca}
"""

saldo = 0
limite = 0
numero_depositos = 0
valorDepositado = 0
numero_saques = 0
valorSaque = 0
LIMITE_SAQUES = 3

def deposito():
    global saldo, numero_depositos, valorDepositado
    deposito = float(input("Ok, informe o valor que você deseja depósitar\n"))
    if deposito > 0:
        saldo += deposito
        print(f"Depósito concluido com sucesso! Seu saldo atual é de R${saldo:.2f}\n")
        numero_depositos += 1
        valorDepositado += deposito
        menuSelecionar(menuProximo)
    else:
        print("Não foi possível realizar a operação.. tente novamente")
        menuSelecionar(menu)

def saque():
    global saldo, valorSaque, numero_saques
    if numero_saques < LIMITE_SAQUES:
        saque = float(input("Digite o valor do saque\n"))
        if saque > 500:
            print("Seu limite de saque é de R$ 500,00.")
            menuSelecionar(menuProximo)
        elif saque <= saldo:
            saldo -= saque
            numero_saques += 1
            valorSaque += saque
            print(f"Saque no valor de R${saque:.2f} foi efetuado com sucesso.\nSeu novo saldo é de R${saldo:.2f}\n") 
            menuSelecionar(menuProximo)
        else:
            print("Saldo insufiente, tente novamente")
            menuSelecionar(menu)
    else:
        print("Seu limite de saque diário expirou.")
        menuSelecionar(menuProximo)

def extrato():
    print(f"""
{nomeBanco}
Seu extrato detalhado.

Total de operações {numero_depositos+numero_saques} 

Número  total de saques: {numero_saques}
Valor total sacado: {valorSaque}
Número total de depósitos: {numero_depositos}
Valor total depósitado: {valorDepositado}

Saldo atual: {saldo}
Limite de saque diário: {LIMITE_SAQUES} / {numero_saques}
""")

def sair():
    print("Finalizando, aguarde!")
    time.sleep(2)
    sys.exit()
def erro():
    menuSelecionar(menuErro)

#A escolha da opção com switch case

switch = {
    1: saque,
    2: deposito,
    3: extrato,
    4: sair
}
def menuSelecionar(palavra):
    print(palavra)
    opcao = int(input())
    operacao = switch.get(opcao, erro)
    operacao()

menuSelecionar(menu)
