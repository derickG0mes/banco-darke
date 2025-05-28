import json
import os
from datetime import datetime

ARQUIVO_USUARIO = "usuario.json"

def inicializar_arquivo():
    if not os.path.exists(ARQUIVO_USUARIO):
        with open(ARQUIVO_USUARIO, "w", encoding='utf-8') as file:
            json.dump({"usuarios": []}, file, ensure_ascii=False, indent=4)

def carregar_usuarios():
    inicializar_arquivo()
    try:
        with open(ARQUIVO_USUARIO, "r", encoding='utf-8') as file:
            dados = json.load(file)
        if "usuarios" not in dados:
            dados["usuarios"] = []
        return dados
    except (json.JSONDecodeError, FileExistsError):
        return {"usuarios": []}
    
def salvar_usuarios(dados):
    with open(ARQUIVO_USUARIO, "w", encoding='utf-8') as file:
        json.dump(dados, file, ensure_ascii=False, indent=4)

def limpa_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def verificar_usuario_existente(campo, valor):
    dados = carregar_usuarios()
    for usuario in dados["usuarios"]:
        try:
            if campo == "nome_usuario":
                if usuario["nome_usuario"] == valor:
                    return True
            else:
                if usuario[campo] == valor:
                    return True
        except Exception:
            continue
    return False
#----------------------------------------------------------------------------#
print("-------BANCO DARKE-------")
print("--BEM VINDO AO BANCO DARKE--\n")

def menu():
    while True:
        print("1. CADASTRO")
        print("2. LOGIN")
        print("3. SAIR")

        opcao = input("\nDigite o número da operação: ")

        if opcao == "1":
            cadastro()
        elif opcao == "2":
            login()
        elif opcao == "3":
            print("Saindo do banco...")
            print("Volte sempre.")
            break
        else:
            print("\nEscolha uma operação de 1 a 3")

def cadastro():
    print("\n--ÁREA DE CADASTRO--")

    dados = carregar_usuarios()

    nome_usuario = input("\nDigite o nome de usuário (ex: nome.sobrenome): ").strip()
    while verificar_usuario_existente("nome_usuario", nome_usuario):
        print("Nome de usuário já existe. Tente outro.")
        nome_usuario = input("\nDigite o nome de usuário: ").strip()

    nome = input("\nDigite o seu nome: ").strip()
    sobrenome = input("\nDigite o seu sobrenome: ").strip()

    idade = int(input("\nDigite a sua idade: "))
    while idade <= 17:
        print("Você ainda é menor de idade para criar uma conta neste banco")
        idade = int(input("\nDigite a sua idade: "))

    data_nascimento = input("\nDigite a sua data de nascimento: ").strip()

    cpf = input("\nDigite o CPF: ").strip()
    while len(cpf) != 11 or not cpf.isdigit() or verificar_usuario_existente("cpf", cpf):
        if verificar_usuario_existente("cpf", cpf):
            print("CPF já existe. Tente outro.")
        else:
            print("CPF inválido. Deve ter 11 dígitos.")
        cpf = input("\nDigite o CPF: ").strip()

    rg = input("\nDigite o seu RG: ").strip()
    while len(rg) < 7 or not rg.isdigit() or verificar_usuario_existente("rg", rg):
        if verificar_usuario_existente("rg", rg):
            print("RG já existe. Tente outro.")
        else:
            print("RG inválido. Deve ter pelo menos 7 dígitos.")
        rg = input("\nDigite o seu RG: ").strip()

    endereco = input("\nDigite o seu endereço: ").strip()
    while len(endereco) < 5:
        print("Endereço inválido. Deve ter pelo menos 5 caracteres.")
        endereco = input("\nDigite o seu endereço: ").strip()

    telefone = input("\nDigite o seu telefone: ").strip()
    while len(telefone) != 11 or not telefone.isdigit() or verificar_usuario_existente("telefone", telefone):
        if verificar_usuario_existente("telefone", telefone):
            print("Telefone já esxite. Tente outro.")
        else:
            print("Telefone inválido. Deve ter 11 dígitos")
        telefone = input("\nDigite o seu número de telefone: ").strip()

    gmail = input("\nDigite o seu gmail: ").strip()
    while "@" not in gmail or ".com" not in gmail or verificar_usuario_existente("gmail", gmail):
        if verificar_usuario_existente("gmail", gmail):
            print("Email já cadastrado. Tente outro.")
        else:
            print("Email inválido. Deve conter @ e .com")
        gmail = input("\nDigite o seu gmail: ").strip()

    senha = input("\nDigite a sua senha: ").strip()
    while len(senha) < 6:
        print("A senha deve ter pelo menos 6 caracteres.")
        senha = input("\nDigite a sua senha: ").strip()

    usuario = {
        "nome_usuario": (nome_usuario),
        "nome": (nome),
        "sobrenome": (sobrenome),
        "idade": (idade),
        "data de nascimento": (data_nascimento),
        "cpf": (cpf),
        "rg": (rg),
        "endereço": (endereco),
        "telefone": (telefone),
        "gmail": (gmail),
        "senha": (senha),
        "saldo da conta": 0,
        "empréstimo": 0,
        "historico_transferencias": []
    }

    dados["usuarios"].append(usuario)
    salvar_usuarios(dados)
    limpa_tela()
    print("Cadastro realizado com sucesso\n")

def login():
    print("--ÁREA DE LOGIN--")

    nome_usuario = input("\nDigite seu usuário: ")
    cpf = input("\nDigite o seu CPF ('Apenas números'): ")
    senha = input("\nDigite a sua senha: ")

    dados = carregar_usuarios()
    for usuario in dados["usuarios"]:
        if usuario["nome_usuario"] == nome_usuario and usuario["cpf"] == cpf and usuario["senha"] == senha:
            limpa_tela()
            print("Login realizado com sucesso")
            usuario_logado(usuario)
            return

    print("\nUsuário, CPF ou senha incorretos")
#----------------------------------------------------------------------------#
def usuario_logado(usuario):
    while True:
        print("\n--MENU PRINCIPAL--")
        print(f"Usuário: {usuario['nome_usuario']}\n")

        print("1. VER SALDO DISPONÍVEL")
        print("2. PIX")
        print("3. HISTÓRICO DE TRANSFERÊNCIA")
        print("4. EMPRÉSTIMO")
        print("5. SAIR DA CONTA")

        opcao = input("Digite o número da operação: ")

        if opcao == "1":
            saldo_disponivel(usuario)
        elif opcao == "2":
            area_pix(usuario)
        elif opcao == "3":
            historico_transferencia(usuario)
        elif opcao == "4":
            emprestimo(usuario)
        elif opcao == "5":
            print("\nSaindo da conta...")
            menu()
        else:
            print("\nEscolha uma operação de 1 a 5")

def saldo_disponivel(usuario):
    print("\n--SALDO DA CONTA--")
    print(f"\nSaldo disponível: {usuario['saldo da conta']}")
    input("\nPressione 'Enter' tecla para continuar...")

def area_pix(usuario):
    while True:
        print("\n--ÁREA PIX--")
        print("1. Fazer pix")
        print("2. Registrar chave pix")
        print("3. Voltar")
    
        opcao = input("\nDigite o número da operação: ")
        if opcao == "1":
            fazer_pix(usuario)
        elif opcao == "2":
            registrar_chave(usuario)
        elif opcao == "3":
            break

def fazer_pix(usuario):
    print("\n--FAZER PIX--")
    buscar_usuario = input("Digite a chave pix do destinatário: ").strip()
    dados = carregar_usuarios()
    
    # Encontrar o usuário remetente nos dados
    for indice, usuario_atual in enumerate(dados["usuarios"]):
        if usuario_atual["nome_usuario"] == usuario["nome_usuario"]:
            indice_remetente = indice
            break
    
    destinatario = None
    for usuario_destinatario in dados["usuarios"]:
        if usuario_destinatario.get("chave_pix") == buscar_usuario:
            destinatario = usuario_destinatario
            break

    if not destinatario:
        print("Usuário não encontrado ou não possui chave pix registrada.")
        return

    confirmacao_pagamento = input(f"Você tem certeza que deseja enviar um pix para {destinatario['nome_usuario']}? (s/n): ").strip().lower()
    if confirmacao_pagamento != 's':
        print("Pix cancelado.")
        return
    
    confirmacao_senha = input("Digite sua senha para confirmar o pix: ").strip()
    if confirmacao_senha != usuario["senha"]:
        print("Senha incorreta. Pix não realizado.")
        return

    valor = float(input("Digite o valor do pix: "))
    if valor <= 0:
        print("Valor inválido. Deve ser maior que zero.")
        return

    if valor > usuario["saldo da conta"]:
        print("Saldo insuficiente.")
        return

    # Atualizar saldo do remetente
    usuario["saldo da conta"] -= valor
    dados["usuarios"][indice_remetente]["saldo da conta"] -= valor
    
    # Atualizar saldo do destinatário
    indice_destinatario = dados["usuarios"].index(destinatario)
    dados["usuarios"][indice_destinatario]["saldo da conta"] += valor

    # Registrar transferência no histórico
    transferencia = {
        "destinatario": destinatario['nome_usuario'],
        "valor": valor,
        "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    }
    
    dados["usuarios"][indice_remetente]["historico_transferencias"].append(transferencia)
    
    salvar_usuarios(dados)
    print(f"Pix de R${valor} enviado para {destinatario['nome_usuario']} com sucesso!")

def registrar_chave(usuario):
    print("\n--REGISTRAR CHAVE PIX--")
    print("1. Gmail")
    print("2. Telefone")
    print("3. CPF")

    opcao = input("\nEscolha chave pix que você deseja registrar: ")

    dados = carregar_usuarios()
    for usuario in dados["usuarios"]:
        if usuario["nome_usuario"] == usuario["nome_usuario"]:
            if opcao == "1":
                chave_pix = input("Digite seu gmail: ")
                if chave_pix == usuario["gmail"]:
                    usuario["chave_pix"] = chave_pix

                    salvar_usuarios(dados)
                    return True
                
            elif opcao == "2":
                chave_pix = input("Digite seu telefone: ")
                if chave_pix == usuario["telefone"]:
                    usuario["chave_pix"] = chave_pix

                    salvar_usuarios(dados)
                    return True
                
            elif opcao == "3":
                chave_pix = input("Digite seu CPF: ")
                if chave_pix == usuario["cpf"]:
                    usuario["chave_pix"] = chave_pix

                    salvar_usuarios(dados)
                    return True
    return False

def historico_transferencia(usuario):
    print("Extrato de transferências")
    for transferencia in usuario["historico_transferencias"]:
        print(f"Para: {transferencia['destinatario']}, Valor: R${transferencia['valor']}, Data: {transferencia['data']}")
    input("\nPressione 'Enter' tecla para continuar...")

def emprestimo(usuario):
    print("Empréstimo")
    valor = float(input("Digite o valor do empréstimo: "))
    if valor <= 0:
        print("Valor inválido. Deve ser maior que zero.")
        return

    usuario["saldo da conta"] += valor
    print(f"Empréstimo de R${valor} concedido com sucesso!")

if __name__ == '__main__':
    inicializar_arquivo()
    menu()