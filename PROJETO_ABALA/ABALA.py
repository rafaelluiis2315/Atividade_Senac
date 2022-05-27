import mysql.connector

conexao = mysql.connector.connect(
    host= '209.209.40.87',
    port=19505,
    user='admin',
    password='dVSsK94z',
    database='Projeto'
)

cursor = conexao.cursor()


def funcoes_sist():
    print(' 1 - Checar registros em uma tabela.')
    print(' 2 - Inserir um registro em tabelas.')
    print(' 3 - Atualizar uma informação em uma tabela.')
    print(' 4 - Deletar um registro de uma tabela.')
    print(' 5 - Finalizar Consultas')


while True:
    print('\n','='*129,'\n')
    funcoes_sist()
    info = input(' Digite o número da função que você deseja executar: ')

    def funcao_ler(tabela_consult):
        comando = f'SELECT * FROM {tabela_consult}'
        cursor.execute(comando)
        resultado = cursor.fetchall()  # ler o banco de dados

        for registro in resultado:
            posicao_registro = resultado.index(registro)

            resultado2 = resultado[posicao_registro]

            print(f" Esse é o {posicao_registro + 1} registo: {resultado2}")

    # CREATE
    if info == "1":

        # READ
        print('\n','='*129,'\n')
        print(" TABELAS: CLIENTES, PRODUTOS, FORNECEDORES e ESTOQUE")
        tabela_consult = str(input(' Digite o nome da tabela que deseja consultar: ')).lower()

        print('\n', ('='*55), "[RESULTADO]", ('='*55), '\n')

        funcao_ler(tabela_consult)
        
    elif info == "2":

        #CREADE

        print('\n', '='*129, '\n')
        print(" TABELAS: CLIENTES, PRODUTOS, FORNECEDORES e ESTOQUES")
        tabela_insercao = str(input(' Digite o nome da tabela que deseja cadastra: ')).lower()

        if tabela_insercao == "clientes":

            print('\n', ('='*55), "[DADOS NECESSÁRIOS]", ('='*55), '\n')
            # Armazena nome do cliente
            nome_clie = str(input(" Qual o seu nome? "))
            # Armazena CPF do cliente
            cpf_clie = str(input(" Qual a sua CPF ? (NÃO incluir pontos ( . ) e traços ( - )): "))
            # Armazena email do cliente
            email_clie = str(input(" Qual o seu E-mail? "))
            # Armazena telefone do cliente
            telefo_clie = str(input(" Qual o seu Telefone? "))
            # Armazena senha do cliente
            senha_clie = str(input(" Crie uma senha: "))

            # insere cadostro no BD
            comando = f'INSERT INTO clientes (cpf_cliente, nome_cliente, telefone, email, senha) VALUES ("{cpf_clie}", "{nome_clie}", "{telefo_clie}", "{email_clie}", "{senha_clie}")'
            cursor.execute(comando)
            conexao.commit()  # edita o banco de dados
        elif tabela_insercao == "produtos":
            
            print('\n', ('='*55), "[DADOS NECESSÁRIOS]", ('='*55), '\n')
            # Armazena descrição do porduto
            discricao_produto = str(input(" Qual a descrição do produto? "))
            # Armazena preço unitario do porduto
            preco_unitario = float(input(" Qual o preço unitario do produto (use ponto no lugar de virgulas): "))
            # Armazena codigo de barras do porduto
            codigo_barras = int(input(" Qual o codigo de barras do produto: "))
            # Armazena numero fornecedor do porduto
            numero_fornecedor = int(input(" Qual o numero do fornecedor: "))
            # Armazena data de fabricação do porduto
            data_fabricacao = str(input(" Qual o data de fabrição do produto: "))
            # Armazena data de vencimento do porduto
            data_vencimento = str(input(" Qual a data de vencimento do produto: "))

            # insere cadostro no BD
            comando = f'INSERT INTO produtos (DESCRiÇAO_PRODUTO, PREÇO_UNITARIO, CODIGO_BARRAS, NUMERO_FORNECEDOR, DATA_FABRICAÇAO, DATA_VENCIMENTO) VALUES ("{discricao_produto}", {preco_unitario}, {codigo_barras}, {numero_fornecedor}, {data_fabricacao}, {data_vencimento})'
            cursor.execute(comando)
            conexao.commit()  # edita o banco de dados

        elif tabela_insercao == "fornecedores":

            print('\n', ('='*55), "[DADOS NECESSÁRIOS]", ('='*55), '\n')
            # nome do Armazena
            nome_fornecedor = str(input(" Qual o nome do fornecedor? "))
            # Armazena CPF
            numero_fornecedor = int(input(" Qual o numero do fornecedor: "))
            # Armazena email
            tipo_fornecedor = str(input(" Qual o tipo do fornecedor? "))
            # Armazena email
            email_fornecedor = str(input(" Qual o E-mail do fornecedor? "))
            # Armazena telefone
            telefo_fornecedor = str(input(" Qual o Telefone do fornecedor? "))

            # insere cadostro no BD
            comando = f'INSERT INTO fornecedores (NOME, CNPJ, EMAIL, TELEFONE) VALUES ("{nome_fornecedor}", "{numero_fornecedor}", "{email_fornecedor}", "{telefo_fornecedor}")'
            cursor.execute(comando)
            conexao.commit()  # edita o banco de dados

        elif tabela_insercao == "estoques":
            
            print('\n', ('='*55), "[DADOS NECESSÁRIOS]", ('='*55), '\n')
            # Armazena nome do lote
            nome_lote = str(input(" Qual o nome do lote? "))
            # Armazena quantidade
            quantidade = int(input(" Quantidade do lote : "))
            # Armazena data de entrada
            data_entrada = str(input(" Data de entrada (COLOCAR TUDO JUNTO, EX:(20220101) : "))
            # Armazena codigo do lote
            codigo_lote = int(input(" Codigo do lote: "))

            comando = f'INSERT INTO estoque (NOME_LOTE, QUANTIDADE, DATA_ENTRADA, CODIGO_LOTE) VALUES ("{nome_lote}", "{quantidade}", "{data_entrada}", "{codigo_lote}")'
            cursor.execute(comando)
            conexao.commit()

        print('\n', ('='*55), "[CADASTRO CONCLUIDO]", ('='*55), '\n')
        funcao_ler(tabela_insercao)


    elif info == "3":
        # UPDATE
        print('\n','='*129,'\n')
        print(" TABELAS: CLIENTES, PRODUTOS, FORNECEDORES e ESTOQUES")
        tabela_atualizacao = str(input('Digite o nome da tabela que deseja atualizar: ')).lower()

        print('\n', ('='*55), "[DADOS NECESSÁRIOS]", ('='*55), '\n')
        campo_alteração = input(' O campo que você deseja alterar: ')
        valor_alteração = input(' Digite o valor da alteração: ')
        campo_alteração_condição = input(' Digite o campo condicional: ')
        dado_campo_alteração_condição = input(' Digite o valor condicional do campo definido acima: ')

        comando = f'UPDATE {tabela_atualizacao} SET {campo_alteração} = {valor_alteração} WHERE {campo_alteração_condição} = "{dado_campo_alteração_condição}" ;'
        cursor.execute(comando)
        conexao.commit()  # edita o banco de dados

        print('\n', ('='*55), "[ATUALIZAÇÃO CONCLUIDO]", ('='*55), '\n')
        funcao_ler(tabela_atualizacao)

    elif info == "4":

        # DELETE
        print('\n','='*129,'\n')
        print(" TABELAS: CLIENTES, PRODUTOS, FORNECEDORES e ESTOQUES")
        tabela_delete = str(input(' Digite o nome da tabela que deseja deletar o dado: ')).lower()

        print('\n', ('='*55), "[DADOS NECESSÁRIOS]", ('='*55), '\n')
        campo_condição_delete = input(' O campo do dado que deseja deletar: ').lower()
        dado_delete = input(' Digite o dado que vai ser deletado: ')
        print('\n','='*129,'\n')

        print ("\n Tem certeza que você quer deletar um dado?")
        print (" Esse dado não podera ser recuperado depois dessa operação! \n")
        decicao = input(" SIM ou NÃO: ").lower()

        if decicao == "sim":

            comando = f'DELETE FROM {tabela_delete} WHERE {campo_condição_delete} = "{dado_delete}" ;'
            cursor.execute(comando)
            conexao.commit() # edita o banco de dados
            print('\n', ('='*27), "[DELETE CONCLUIDO]", ('='*27), '\n')
            funcao_ler(tabela_delete)

        elif decicao == "não":
            print(" OK DELETE CANCELADO")

           
    elif info == "5":
        break

    else:
        print("Digite uma opção valida")

cursor.close()
conexao.close()
