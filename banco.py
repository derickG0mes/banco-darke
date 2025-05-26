import json
import os
from cryptography.fernet import Fernet

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
#----------------------------------------------------------------------------#
print("--BANCO DARKE--")
print("-BEM VINDO AO BANCO DARKE-")

def menu():
    print("1. CADASTRO")
    print("2. LOGIN")
    print("3. SAIR")

    opcao = int(input("Digite o número da operação: "))

    while True:
        if opcao == 1:
            cadastro()
        elif opcao == 2:
            login()
        elif opcao == 3:
            print("Saindo do banco...")
            print("Volte sempre.")
            break
        else:
            print("Escolha uma operação de 1 a 3")

def cadastro():
    print("--ÁREA DE CADASTRO")

    dados = carregar_usuarios()

    nome = input("Digite o seu nome: ")
    sobrenome = input("\nDigite o seu sobrenome: ")
    cpf = input("\nDigite o seu CPF ('Apenas números'): ")
    rg =input("Digite o número do seu RG: ")
    endereco = input("\nDigite o seu endereço: ")
    telefone = input("\nDigite o seu número de telefone: ")
    gmail = input("\nDigite o seu gmail: ")
    senha = input("\nDigite a sua senha: ")

    usuario = {
        "nome": (nome),
        "sobrenome": (sobrenome),
        "cpf": (cpf),
        "rg": (rg),
        "endereço": (endereco),
        "telefone": (telefone),
        "gmail": (gmail),
        "senha": (senha)
    }

    dados["usuarios"].append(usuario)
    salvar_usuarios(dados)

    print("Cadastro realizado com sucesso")

def login():
    print("--ÁREA DE LOGIN--")

    cpf = input("\nDigite o seu CPF ('Apenas números'): ")
    senha = input("\nDigite a sua senha: ")

    print("Login realizado com sucesso")
#----------------------------------------------------------------------------#
def usuario_logado():
    print("--MENU PRINCIPAL")
    print("Usuário: \n")

    print("1. VER SALDO DISPONÍVEL")
    print("2. PIX")
    print("3. HISTÓRICO DE TRANSFERÊNCIA")
    print("4. EMPRÉSTIMO")
    print("5. SAIR DA CONTA")

    opcao = int(input("Digite o número da operação: "))

    while True:
        if opcao == 1:
            saldo_disponivel()
        elif opcao == 2:
            area_pix()
        elif opcao == 3:
            historico_transferencia()
        elif opcao == 4:
            emprestimo()
        elif opcao == 5:
            print("Saindo da conta...")
            menu()
        else:
            print("Escolha uma operação de 1 a 5")

def saldo_disponivel():
    print("Saldo disponível: 0")

def area_pix():
    print("pix")

def historico_transferencia():
    print("Histórico de transferÊncia")

def emprestimo():
    print("Empréstimo")