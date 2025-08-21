saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
lista_cliente = {}
lista_contas = {}
cc = 1
AGENCIA = "0001"

def menu_principal():
   
    menu = """

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Novo Cliente
    [5] Nova Conta
    [6] Listar contas
    [7] Listar clientes
    [0] Sair

    => """

    print (menu)

def depositar(saldo, valor,extrato, /):

   
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"

        print(f"O valo de R$:{valor:.2f} foi depositado")

    else:
         print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def sacar(*, saldo, valor, extrato,limite, numero_saques, limite_saques):

    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Você não tem saldo suficiente.")

    elif excedeu_limite:
        print(" O valor do saque excede o limite de R$ 500,00.")

    elif excedeu_saques:
        print("Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1

        print(f"O Valor de R${valor:.2f} foi retirado")
    else:
        print("O valor informado é inválido.")


    return saldo, extrato, numero_saques

def imprimir_extrato(saldo, /, *, extrato):

    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def criar_usuario():

    print(f"Seja bem- vindo, vamos criar um novo cadastro")
    print("==============================================")

    try: 
        
        cpf =str(input("Digite o numero do CPF(somente os numeros)"))

        if len(cpf) !=11 or not cpf.isdigit():

             print ("Esse CPF é invalido")

        
        elif cpf in lista_cliente:
             
             print ("Esse CPF ja tem cadastro no banco")
             return
                    
             

        nome = input("Informe o seu nome completo")
        data_nascimento = input("Informe sua data de nascimento (dd-mm-aaaa)")
        logradouro = input("Informe o nome da sua rua")
        bairro = input("Informe o bairro")
        cidade = input("Informe a cidade")
        estado = input("Informe o estado (sigla)")

        cliente = {
                   "nome": nome,
                   "data_nascimento": data_nascimento,
                   "logradouro": logradouro,
                   "bairro": bairro,
                   "cidade": cidade, 
                   "estado": estado
        }


        lista_cliente[cpf] = cliente

        print("Usuario cadastrado com sucesso")

    except ValueError:
    
     print("Você não digitou um CPF válido")
     menu_principal()
        
def criar_conta(cont_conta):

    cont_conta = cc+1

    cpf= input("Digite o CPF do usuario(somente numeros)")

    if len(cpf) !=11 or not cpf.isdigit():

             print ("Esse CPF é invalido")
             menu_principal()

        
    elif cpf in lista_cliente:

            conta = {
                "agencia": AGENCIA,
                "conta corrente": cont_conta
            }
             
            
            cliente = lista_cliente[cpf]

            if "contas" not in cliente:
                cliente["contas"] = []

            cliente["contas"].append(conta)

            lista_contas[cont_conta] = conta

            
            return cont_conta
    else:
            print ("Não tem usuario cadastrado nesse CPF")

            
    menu_principal()
             

        

while True:

    menu_principal()

    opcao = input()

    if opcao == "1":

        valor = float(input("Informe o valor do deposito:"))

        saldo, extrato = depositar(saldo,valor, extrato)

    elif opcao == "2":

        valor = float(input("Informe o valor do saque: "))

        saldo, extrato, numero_saques = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)
        

    elif opcao == "3":
       imprimir_extrato(saldo, extrato=extrato)   

    elif opcao == "4":
        
        criar_usuario()

    elif opcao == "5":

        cc = criar_conta(cc)

    elif opcao == "6":

        for chave, valor in lista_contas.items():
            print(chave, valor)
            

    elif opcao == "7":
            
        for chave, valor in lista_cliente.items():
            print(chave, valor)
            
    elif opcao == "0":
        break

    else:
        print("Opção inválida, por favor selecione novamente a operação desejada.")