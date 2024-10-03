import datetime
import pytz

#adicionar um limite de 10 transações diárias
LIMITE_SAQUES = 3
LIMITE_DIARIO = 10

def atualizar_transacoes(ultima_data, numero_transacoes): 
    data_atual = datetime.datetime.now().date()
    
    if data_atual > ultima_data:
        return data_atual, 0 #atualiza a data e o numero de transações
    else:
        return data_atual, numero_transacoes + 1
    
def atualizar_saques(ultima_data, numero_saques): 
    data_atual = datetime.datetime.now().date()
    
    if data_atual > ultima_data:
        return data_atual, 0 #atualiza a data e o numero de saques
    else:
        return data_atual, numero_saques + 1
    
    
    

def deposito(saldod, extratod, ultima_data, numero_transacoes):
    data, transacoes = atualizar_transacoes(ultima_data,numero_transacoes)
    if transacoes > LIMITE_DIARIO:
        print("Você excedeu o limite diário de transações") 
        return saldod, extratod, data, transacoes
    else: 
        while True:
            valor = float(input ("Quanto deseja depositar?\n"))
            if valor >= 0:
                break
            else:
                print("Digite valor um válido\n")
        
        saldod += valor
        d = datetime.datetime.now()
        d = d.strftime("%d/%m/%Y às %H:%M") 
        mensagem = f"Valor R${valor:.2f} foi depositado a sua conta no dia " + d + f"! Saldo após operação: R${saldod:.2f}\n"
        extratod = mensagem + extratod 
        print(mensagem)
        return saldod,extratod, data, transacoes 

def saque(saldo,extrato, numero_saques, ultima_data, numero_transacoes):
    while True:
        ultima_data, numero_saques = atualizar_saques(ultima_data, numero_saques)    
        if numero_saques >  LIMITE_SAQUES:
                print("Limite de saques diários atingido! Volte amanhã!\n")
                break
        
        ultima_data, numero_transacoes = atualizar_transacoes(ultima_data,numero_transacoes) #precisa ser embaixo do if dos saques se não vai contar um saque mal sucedido como operação
        if numero_transacoes > LIMITE_DIARIO:
            print("Você excedeu o limite diário de transações")
            break
            
        valor = float(input ("Quanto deseja sacar?\n"))
        if valor > 0 and valor <= 500:
            if valor > saldo:
                print("Saque maior do que saldo disponível! Digite um valor válido!\n")
            else:
                saldo -= valor
                d = datetime.datetime.now()
                d = d.strftime("%d/%m/%Y às %H:%M")
                mensagem = f"Valor R${valor:.2f} foi sacado da sua conta no dia " + d + f"! Saldo após operação: R${saldo:.2f}\n"
                extrato = mensagem + extrato 
                print(mensagem)
                break
        else:
            print("Digite valor um válido\n")
    
    return saldo,extrato, numero_saques, ultima_data, numero_transacoes 




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
numero_transacoes = 0
extrato = ""
ultima_data = datetime.datetime.now().date()


while True:
    opcao = input(menu)
    
    if opcao == "d":
        print("Déposito\n")
        saldo,extrato,ultima_data,numero_transacoes = deposito(saldo,extrato,ultima_data,numero_transacoes)
        
        
    elif opcao == "s":
        print("Saque\n")
        saldo, extrato, numero_saques, ultima_data, numero_transacoes = saque(saldo, extrato, numero_saques, ultima_data, numero_transacoes)
        
    elif opcao == "e":
        print("Extrato")
        print("Extrato da operação mais recente até a menos recente:\n")
        print(extrato)
        
    elif opcao == "q":
        break
    
    else: 
        print("Operação inválida, por favor selecione novamente a operação desejada.")
        
        

        
            