import json
import os

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
        "empréstimo": 0
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
            saldo_disponivel()
        elif opcao == "2":
            area_pix()
        elif opcao == "3":
            historico_transferencia()
        elif opcao == "4":
            emprestimo()
        elif opcao == "5":
            print("\nSaindo da conta...")
            menu()
        else:
            print("\nEscolha uma operação de 1 a 5")

def saldo_disponivel():
    print("Saldo disponível: 0")

def area_pix():
    print("pix")

def historico_transferencia():
    print("Histórico de transferÊncia")

def emprestimo():
    print("Empréstimo")

if __name__ == '__main__':
    inicializar_arquivo()
    menu()