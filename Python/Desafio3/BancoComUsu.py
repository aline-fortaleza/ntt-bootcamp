"""
No desafio de codigo ele implementa o criar conta e criar usuario, mas no fim das contas não faz as operações
com os usuarios e segue essa linha mais "geral" deixei assim por enquanto mas pretendo voltar para melhorar o código

Adicionar individualmente:
Saldo
Limite de Saque
Limite de deposito
Limite de Operação
Extrato
"""

import datetime
import pytz

#adicionar funções de criar usuário e criar conta corrente
LIMITE_SAQUES = 3
LIMITE_DIARIO = 10
MAX_SAQUE = 500

def validar_data(nascimento): #checa se ta no formato certo
    try:
        # Tenta converter a entrada para o formato dd/mm/aaaa
        data_valida = datetime.strptime(nascimento, "%d/%m/%Y")
        return True
    except ValueError:
        # Se ocorrer um erro de formato, retorna False
        return False
    
def validar_cpf(cpf): #checa se ta no formato certo
    # Verifica se o CPF tem 11 dígitos e se contém apenas números
    if len(cpf) == 11 and cpf.isdigit():
        return True
    else:
        return False    
    
def cpf_ja_cadastrado(usuarios,cpf): #checa se o cpf já foi cadastrado
    for usuario in usuarios:
        if usuario[2] == cpf:
            return True # se ja foi retorna True
    return False #se não foi retorna False    

def criar_usu_aux (usuarios,nome, nascimento, cpf, logra, nro, bairro,cidade,estado): #começar o codigo com usuarios vazio
    usu_atual = [nome, nascimento, cpf, logra + ", " + nro + " - " + bairro + " - " + cidade + "/" + estado] #colocando no formato que ele pediu
    usuarios.append(usu_atual)
    usuarios.sort(key=lambda x:x[2]) #deixando ordendo pelo cpf
    return usuarios
    
def criar_usu (usuarios): 
    nome = input("Qual seu nome?")
    while True:
        nascimento = input("Qual sua data de nascimento?(dd/mm/aaaa)")
        if validar_data(nascimento) == True: 
            break
        else:
            print("Por favor, digite a data em um formado válido")
    
    while True:
        cpf = input("Qual seu cpf? Digite apenas números!")
        if validar_cpf(cpf):
            if not cpf_ja_cadastrado(usuarios,cpf): #se não foi cadastrado(ou seja a função devolveu falso) segue
                break
            else:
                print("CPF já cadastrado! Digite outro CPF!")
        else:
            print("Por favor, digite o cpf em um formato válido")
            
    logra = "Em que rua você mora?"
    nro = "Em que número você mora?"
    bairro = "Em que bairro você mora?"
    cidade = "Em que cidade você mora?"
    estado = "Qual a sigla do estado que você mora?"
    
    usuarios = criar_usu_aux (usuarios,nome, nascimento, cpf, logra, nro, bairro,cidade,estado) 
    return usuarios
            
            

def criar_conta (usuarios,contas):
    agencia ="0001"
    if contas == []:
        num_conta = 1
    else:
        num_conta = contas[-1][1] +1
    
    while True:
        cpf_usuario = input("Qual o CPF do titular da conta? Digite somente numeros")
        if validar_cpf(cpf_usuario): #checa se ta no padrão do cpf
            if cpf_ja_cadastrado(usuarios,cpf_usuario): #checa se o usuario foi cadastrado
                break # caso ambos, quebra do true
            else:
                print("CPF não foi cadastrado, digite um CPF já cadastrado")
        else:
            print("CPF fora dos padrões! Digite somente números!") 
    
    conta_atual = [agencia, num_conta,cpf_usuario]        
    contas.append(conta_atual) 
    return contas     
        
         

def atualizar_transacoes(*,ultima_data, numero_transacoes): 
    data_atual = datetime.datetime.now().date()
    
    if data_atual > ultima_data:
        return data_atual, 0 #atualiza a data e o numero de transações
    else:
        return data_atual, numero_transacoes + 1
    
def atualizar_saques(*,ultima_data, numero_saques): 
    data_atual = datetime.datetime.now().date()
    
    if data_atual > ultima_data:
        return data_atual, 0 #atualiza a data e o numero de saques
    else:
        return data_atual, numero_saques + 1
    
def extrato(saldo,/,valor,tipo,*,extrato):
    d = datetime.datetime.now()
    d = d.strftime("%d/%m/%Y às %H:%M")
    if tipo == "deposito":
        mensagem = f"Valor R${valor:.2f} foi depositado a sua conta no dia " + d + f"! Saldo após operação: R${saldo:.2f}\n"
        extrato = mensagem + extrato
             
    

def deposito(saldod, extratod, ultima_data, numero_transacoes,/):
    data, transacoes = atualizar_transacoes(ultima_data = ultima_data ,numero_transacoes = numero_transacoes )
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

def saque(*,saldo,extrato, numero_saques, ultima_data, numero_transacoes):
    while True:
        ultima_data, numero_saques = atualizar_saques(ultima_data = ultima_data, numero_saques = ultima_data)    
        if numero_saques >  LIMITE_SAQUES:
                print("Limite de saques diários atingido! Volte amanhã!\n")
                break
        
        ultima_data, numero_transacoes = atualizar_transacoes(ultima_data = ultima_data ,numero_transacoes = numero_transacoes) #precisa ser embaixo do if dos saques se não vai contar um saque mal sucedido como operação
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
[u] Criar Usuario
[c] Criar Conta
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>
"""

usuarios = []
contas = []

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

