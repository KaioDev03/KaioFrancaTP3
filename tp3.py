import csv
import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime
import sqlite3
#Tratamento de erros ao carregar arquivo.
#Abra o arquivo "dados_usuarios.csv" usando o bloco try...except. Exiba uma mensagem de erro se o arquivo não for encontrado (erro específico) e informe ao usuário que o arquivo está em falta.
print("Exercicio 1")
'''
    1. Abra o arquivo "dados_usuarios.csv" usando o bloco try...except. Exiba uma mensagem de erro se o arquivo nao for encontrado (erro especifico) e informe ao usuario que o arquivo esta em falta.
'''
with open('dados_usuarios.csv', mode='r', encoding='utf-8') as file:
    try:
        reader = csv.reader(file)
        for row in reader:
            print(row)
    except FileNotFoundError:
        print("O arquivo 'dados_usuarios.csv' nao foi encontrado.")
        
#Explorando Dados do Excel
#Abra o arquivo "dados_usuarios.csv", que contém informações dos usuários. Exiba as 10 primeiras linhas do arquivo e liste todas as colunas presentes no arquivo.
print("Exercicio 2")
'''
    1. Abra o arquivo "dados_usuarios.csv", que contém informações dos usuários. Exiba as 10 primeiras linhas do arquivo e liste todas as colunas presentes no arquivo.
'''
with open('dados_usuarios.csv', mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    
    header = next(reader)
    print("Colunas presentes no arquivo:", header)
    
    print("\nAs 10 primeiras linhas são:")
    for idx, row in enumerate(reader, start=1):
        if idx <= 10:
            print(row)
        else:
            break
#Manipulação de Dados Básica
#Usando Pandas, selecione apenas os usuários com idade maior que 30 e salve esses dados em um novo arquivo chamado "INFwebNET_30mais.xlsx".
print("Exercicio 3")
''''
    1. Utilizando Pandas, selecione apenas os usuários com idade maior que 30 e salve esses dados em um novo arquivo chamado "INFwebNET_30mais.xlsx".
'''
df = pd.read_csv('dados_usuarios.csv', encoding='utf-8', delimiter=';')
df = df[df['idade'] > 30]
df.to_excel('INFwebNET_30mais.xlsx', index=False)
print("Arquivo INFwebNET_30mais.xlsx criado com sucesso.")
#Limpeza de Dados
#Para o DataFrame anterior proceda com as seguintes tarefas de limpeza de dados:
#Remova todos os usuários que não possuírem e-mail válido cadastrado.
#Preencha os valores ausente do campo “cidade” com o texto “Não Informada”.
#Preencha os dados ausentes na coluna “estado” com “ZZ”.
print("Exercicio 4")
'''
    1. Remova todos os usuários que não possuírem e-mail valido cadastrado
    2. Preencha os valores ausente do campo "cidade" com o texto "Nao Informada"
    3. Preencha os dados ausentes na coluna "estado" com "ZZ"
'''
df = pd.read_csv('dados_usuarios.csv', encoding='utf-8', delimiter=';')
df = df[df['email'].notna()]  # Remove e-mails que são NaN
df = df[df['email'].str.contains('@', na=False)]  # Remove os e-mails sem '@'
df['cidade'] = df['cidade'].fillna('Nao Informada')
df['estado'] = df['estado'].fillna('ZZ')

df.to_csv('dados_usuarios_limp.csv', index=False)
print("Arquivo dados_usuarios_limp.csv criado com sucesso.")
#Combinação de Arquivos Excel
#A INFwebNET possui dados históricos de usuários em arquivo Excel com o nome “INFwebNET_Historico.xlsx”, onde há duas tabelas, “INFwebNET2022” e “INFwebNET2023”, cada uma referente a um ano.
#Use um bloco try...except para carregar as planilhas do arquivo "INFwebNET_Historico.xlsx" e, se o arquivo for carregado com sucesso, exiba o número total de linhas de cada planilha. Caso ocorra uma exceção, mostre uma mensagem de erro apropriada.
print("Exercicio 5")
'''
    5. Use um bloco try...except para carregar as planilhas do arquivo "INFwebNET_Historico.xlsx" e, se o arquivo for carregado com sucesso, exiba o número total de linhas de cada planilha. Caso ocorra uma exceção, mostre uma mensagem de erro apropriada.
'''
try:
    df_2022 = pd.read_excel('INFwebNET_Historico.xlsx', sheet_name='INFwebNET2022')
    df_2023 = pd.read_excel('INFwebNET_Historico.xlsx', sheet_name='INFwebNET2023')
    
    print("Número de linhas da planilha 'INFwebNET2022':", len(df_2022))
    print("Número de linhas da planilha 'INFwebNET2023':", len(df_2023))
except FileNotFoundError:
    print("O arquivo 'INFwebNET_Historico.xlsx' nao foi encontrado.")
except Exception as e:
    print(f"Erro ao carregar o arquivo: {e}")
#Combinação de Arquivos Excel
#Carregue a informação das duas planilhas, combine as informações em um único DataFrame e remova duplicatas baseado na coluna "id".
print("Exercicio 6")
'''
    1. Carregue a informação das duas planilhas, combine as informações em um único DataFrame e remova duplicatas baseado na coluna "id".
'''
try:
    df_2022 = pd.read_excel('INFwebNET_Historico.xlsx', sheet_name='INFwebNET2022')
    df_2023 = pd.read_excel('INFwebNET_Historico.xlsx', sheet_name='INFwebNET2023')
    
    df_combinado = pd.concat([df_2022, df_2023], ignore_index=True)
    
    df_combinado = df_combinado.drop_duplicates(subset='id', keep='first')
    
    print(df_combinado)
except FileNotFoundError:
    print("O arquivo 'INFwebNET_Historico.xlsx' nao foi encontrado.")
except Exception as e:
    print(f"Erro ao carregar o arquivo: {e}")
#Carregando Dados em SQL
#Conecte-se a um banco de dados SQLite chamado "INFwebNET_DB.db" usando SQLAlchemy. Carregue os dados combinados do item anterior para uma tabela chamada "Usuarios_Historicos".
print("Exercicio 7")
'''
    1. Conecte-se a um banco de dados SQLite chamado "INFwebNET_DB.db" usando SQLAlchemy.
    2. Carregue os dados combinados do item anterior para uma tabela chamada "Usuarios_Historicos".
'''
try:
    engine = create_engine('sqlite:///INFwebNET_DB.db')
    df_combinado.to_sql('Usuarios_Historicos', con=engine, if_exists='replace', index=False)
    print("Dados carregados com sucesso para a tabela 'Usuarios_Historicos'.")
except Exception as e:
    print(f"Erro ao carregar os dados: {e}")
#Consultando o Banco de Dados SQL
#Escreva uma consulta usando Pandas que retorne apenas os usuários com idade entre 22 e 30 anos existentes na tabela “Usuarios_Historicos”. Exiba o resultado na tela.
print("Exercicio 8")
'''
    1. Escreva uma consulta usando Pandas que retorne apenas os usuários com idade entre 22 e 30 anos existentes na tabela “Usuarios_Historicos”.
    2. Exiba o resultado na tela.
'''
try:
    engine = create_engine('sqlite:///INFwebNET_DB.db')
    df = pd.read_sql_query('SELECT * FROM Usuarios_Historicos WHERE idade BETWEEN 22 AND 30', con=engine)
    print(df)
except Exception as e:
    print(f"Erro ao consultar os dados: {e}")
#Utilizando o Pandas e SQLAlchemy crie uma nova tabela no banco de dados chamada “Consolidado” e insira nesta tabela todos os dados obtidos nos itens anteriores.
print("Exercicio 9")
'''
    1. Utilizando o Pandas e SQLAlchemy crie uma nova tabela no banco de dados chamada “Consolidado” e insira nesta tabela todos os dados obtidos nos itens anteriores.
'''
try:
    engine = create_engine('sqlite:///INFwebNET_DB.db')
    df.to_sql('Consolidado', con=engine, if_exists='replace', index=False)
    print("Dados carregados com sucesso para a tabela 'Consolidado'.")
except Exception as e:
    print(f"Erro ao carregar os dados: {e}")
#Atualizando idade
#Consulte todos os dados da tabela “Consolidado” e recalcule a idade de todos os usuários considerando a data de 22 de julho de 2024. Exporte os dados atualizados para uma tabela SQL chamada “Consolidado_Atualizado”.
print("Exercicio 10")
'''
    1. Consulte todos os dados da tabela “Consolidado” e recalcule a idade de todos os usuários considerando a data de 22 de julho de 2024.
    2. Exporte os dados atualizados para uma tabela SQL chamada “Consolidado_Atualizado”.
'''
try:
    engine = create_engine('sqlite:///INFwebNET_DB.db')
    df = pd.read_sql_query('SELECT * FROM Consolidado', con=engine)
    df['idade'] = (pd.to_datetime('2024-07-22') - pd.to_datetime(df['data de nascimento'])).dt.days // 365
    df.to_sql('Consolidado_Atualizado', con=engine, if_exists='replace', index=False)
    print("Dados atualizados com sucesso para a tabela 'Consolidado_Atualizado'.")
except Exception as e:
    print(f"Erro ao atualizar os dados: {e}")
#Exceção Customizada para Dados Ausentes
#Implemente uma função que leia os dados da tabela “Consolidado” e lance uma exceção customizada chamada "DadosAusentesError" se alguma coluna apresentar um dado faltante. Utilize um bloco try...except para capturar essa exceção e listar o e-mail do INFNETiano em questão caso a exceção seja levantada, e salve o e-mail em um arquivo txt chamado, “dados_ausentes.txt”.
print("Exercicio 11")
'''
    1. Leia os dados da tabela “Consolidado” e levante uma exceção se alguma coluna apresentar um dado faltante.
    2. Liste os e-mails do INFNETiano em questão caso a exceção seja levantada.
    3. Salve os e-mails em um arquivo txt chamado “dados_ausentes.txt”.
'''
try:
    engine = create_engine('sqlite:///INFwebNET_DB.db')
    df = pd.read_sql_query('SELECT * FROM Consolidado', con=engine)
    if df.isnull().any().any():
        # Identificando os dados ausentes
        usuarios_ausentes = df[df.isnull().any(axis=1)]
        emails_ausentes = usuarios_ausentes['email'].tolist()
    print("Não há dados ausentes.")
    
except Exception as e:
    print(f"Exceção levantada: {e}")
    with open("dados_ausentes.txt", "w") as f:
        for email in e.args[0].split(': ')[1].split(', '):
            f.write(email + "\n")
            
    print("E-mails com dados ausentes foram salvos em 'dados_ausentes.txt'.")
#Try…Except Completo
#Escreva uma função que leia todos os arquivos: “dados_usuario.csv”, “INFwebNET_30mais.xlsx", “INFwebNET_Historico.xlsx”, "INFwebNET_DB.db" e “dados_ausentes.txt” utilizando uma estrutura try...except completa de forma que cada tentativa de leitura seja feita dentro de um try que capture e lide com os seguintes tipos de exceções: `FileNotFoundError`, `MemoryError`, `RuntimeError`, `EOFError`, `OSError`, `ConnectionError`, `TimeoutError` e `PermissionError`.
#Lide com cada tipo de exceção exibindo uma mensagem apropriada e siga para o próximo arquivo ou encerre o programa quando for apropriado.
#Utilize um bloco else para exibir a quantidade de linhas existentes no arquivo lido
#Utilize um bloco finally para garantir o fechamento do arquivo ou da conexão.
print("Exercicio 12")
'''
    1. Leia os arquivos: "dados_usuario.csv", "INFwebNET_30mais.xlsx", "INFwebNET_Historico.xlsx", "INFwebNET_DB.db" e "dados_ausentes.txt" utilizando uma estrutura try...except completa.
    2. Lide com cada tipo de exceção exibindo uma mensagem apropriada e siga para o próximo arquivo ou encerre o programa quando for apropriado.
    3. Utilize um bloco else para exibir a quantidade de linhas existentes no arquivo lido.
    4. Utilize um bloco finally para garantir o fechamento do arquivo ou da conexão.
'''
files = [
    "dados_usuario.csv",
    "INFwebNET_30mais.xlsx",
    "INFwebNET_Historico.xlsx",
    "INFwebNET_DB.db",
    "dados_ausentes.txt"
]

for file in files:
    try:
        print(f"Lendo o arquivo: {file}")
        
        if file.endswith(".csv"):
            df = pd.read_csv(file, encoding='utf-8', delimiter=';')
        elif file.endswith(".xlsx"):
            df = pd.read_excel(file, engine='openpyxl')
        elif file.endswith(".db"):
            conn = sqlite3.connect(file)
            df = pd.read_sql_query("SELECT * FROM Usuarios_Historicos", conn)
        elif file.endswith(".txt"):
            with open(file, 'r') as f:
                dados = f.readlines()
            df = pd.DataFrame(dados, columns=['email'])  # Criação de um DataFrame para manter a consistência
            
        else:
            raise ValueError("Tipo de arquivo desconhecido ou não suportado.")
        
    except FileNotFoundError:
        print(f"Erro: O arquivo '{file}' não foi encontrado.")
    except pd.errors.ParserError:
        print(f"Erro: Falha ao analisar o conteúdo do arquivo '{file}'.")
    except sqlite3.DatabaseError:
        print(f"Erro: Falha ao conectar ou ler o banco de arquivo '{file}'.")
    except ValueError as ve:
        print(f"Erro: {ve}")
    except Exception as e:
        print(f"Erro inesperado ao ler o arquivo '{file}': {e}")
    else:
        print(f"Quantidade de linhas no arquivo '{file}': {len(df)}")
    finally:
        # Garantindo o fechamento da conexão se o arquivo for um banco de dados
        if file.endswith(".db") and 'conn' in locals():
            conn.close()
            print(f"Conexão com o banco de dados '{file}' encerrada.")