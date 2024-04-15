cod_mestre="34470274"         #cód. criação cadastro inicial

import sys

i=5
lapso2=0
acao_user=0
acao_user2=0
usuarios = []
estoque=[]

def cad_estoque():
    prod = input("Produto:")
    lote_produto = input ("Lote:")
    peso_unitario = input ("Peso médio unitário:")
    data_fab = input ("Data de fabricação:")
    validade_prod = input ("Validade do Produto:")
    quantidade = input("Quantidade:")
    novoProduto = {
    "Produto":prod,
    "Lote": lote_produto,
    "Peso Unitário": peso_unitario,
    "Data de Fabricação": data_fab,
    "Validade do Lote" : validade_prod,
    "Quantidade": quantidade
    }
    print("\nO seguinte produto foi cadastrado:\n")
    estoque.append(novoProduto)
    for dados,produto in novoProduto.items():
        print(f"{dados}:{produto}")

def getUser():
    nome = input ("Nome:")
    senha = input("Senha:")
    novoUsuario = {
    "Nome":nome,
    "Senha":senha
    }
    return novoUsuario

def login():
    print('\nlogin\n')
    inputUser = getUser()
    for usuario in usuarios:
        if (usuario["Nome"]== inputUser["Nome"] and usuario["Senha"]):
            return True;
    return False

def cadastro():
    cod_digitado=input("Digite o código de acesso:(é 34470274)")
    if cod_digitado==cod_mestre:
        print('\nCadastro\n')
        novoUsuario = getUser()
        usuarios.append(novoUsuario)
    if cod_digitado!=cod_mestre:
        print("\nCódigo Invalido\n")

while acao_user!=3:
    acao_user=int(input("Selecione uma das opções abaixo:\nLogin/cadastro\n1--->cadastro\n2--->login\n3--->Sair\n-->"))
    if acao_user==1:
         cadastro()
         print("\n")
    if acao_user==2:
        lapso2=0
        if login():
            i=5
            while lapso2!=1:
                acao_user2=int(input("Seja bem vindo, selecione uma das opções abaixo:\n1-->Consulta de estoque\n2-->Cadastro de Mercadorias\n3-->Retirada de Mercadorias\n4-->Sair para o menu\n-->"))
                if acao_user2==1:
                    for item in estoque:
                        print("Produto:",item.get("Produto"),"\nLote:",item.get("Lote"), "\nPeso médio unitário:",item.get("Peso Unitário"),"\nData de fabricação:",item.get("Data de Fabricação"),"\na validade do lote expira em:",item.get("Validade do Lote"),"\nQuantidade:",item.get("Quantidade"),"\n\n")
                if acao_user2==2:
                    cad_estoque()
                    print("\n")
                if acao_user2==3:
                    z=-1
                    p=input("qual o lote do produto que você deseja remover?")
                    for item in estoque:
                        z=z+1
                        if (item["Lote"]==p):
                            del estoque[z]
                if acao_user2==4:
                    lapso2=1    
        else:
            i=i-1
            print("Senha Invalida, você ainda tem %s chances"%(i))
            if i==0:
                print("Sessão encerrada")
                sys.exit()
    if acao_user==3:
        print("Sessão encerrada")
        sys.exit()
print("Sessão encerrada")