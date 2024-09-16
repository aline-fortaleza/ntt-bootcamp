LIMITE_SAQUES = 3

def deposito(saldod, extratod):
    while True:
        valor = float(input ("Quanto deseja depositar?\n"))
        if valor >= 0:
            break
        else:
            print("Digite valor um válido\n")
    
    saldod += valor
    mensagem = f"Valor R${valor:.2f} foi depositado a sua conta! Saldo após operação: R${saldod:.2f}\n"
    extratod = mensagem + extratod 
    print(mensagem)
    return saldod,extratod 

def saque(saldo,extrato, numero_saques):
    while True:
        if numero_saques >=  LIMITE_SAQUES:
                print("Limite de saques diários atingido! Volte amanhã!\n")
                break
            
        valor = float(input ("Quanto deseja sacar?\n"))
        if valor > 0 and valor <= 500:
            if valor > saldo:
                print("Saque maior do que saldo disponível! Digite um valor válido!\n")
            else:
                saldo -= valor
                mensagem = f"Valor R${valor:.2f} foi sacado da sua conta! Saldo após operação: R${saldo:.2f}\n"
                extrato = mensagem + extrato 
                numero_saques += 1
                print(mensagem)
                break
        else:
            print("Digite valor um válido\n")
    
    return saldo,extrato, numero_saques 




menu = """

MENU:
[d] Depositar 
[s] Sacar
[e] Extrato
[q] Sair

=>
"""

saldo = 0
max_saque = 500
numero_saques = 0
extrato = ""

while True:
    opcao = input(menu)
    
    if opcao == "d":
        print("Déposito\n")
        saldo,extrato = deposito(saldo,extrato)
        
        
    elif opcao == "s":
        print("Saque\n")
        saldo, extrato, numero_saques = saque(saldo, extrato, numero_saques)
        
    elif opcao == "e":
        print("Extrato")
        print("Extrato da operação mais recente até a menos recente:\n")
        print(extrato)
        
    elif opcao == "q":
        break
    
    else: 
        print("Operação inválida, por favor selecione novamente a operação desejada.")
        
        

        
            