import csv
import json
import os
import pandas as pd
from datetime import datetime
import ast #Conversão de string do dicionário de amigos em um set
#Escreva um programa que leia o arquivo ""rede_INFNET_atualizado.txt" que foi elaborado no seu TP1, que contém dados básicos dos usuários (nome, idade, cidade, estado) - INFNETianos;
print("Exercicio 1")
'''Tratando os dados do arquivo txt'''
with open("rede_INFNET_atualizado.txt", mode='r', encoding='utf-8') as file:
    content = file.readlines()
    
    for linha in content:
        linha = linha.strip()
        if not linha:
            continue
        
    for linha in content:
        linha = linha.split('?')
        if not linha:
            continue
    
print(content)

print("Exercicio 1 - B")
'''Criação de 1 arquivo CSV usando os dados do arquivo TXT. Criado os "Headers" da tabela, feito a tratativa da linha "amigos" por conta que ele era considerado um SET.'''
#Utilizando a biblioteca csv, exporte um arquivo “INFwebNet.csv” contendo os mesmos dados.
with open("rede_INFNET_atualizado.txt", mode='r') as file:
    linhas = file.readlines()
    
with open("INFwebNet.csv", mode='w', newline='') as file.csv:
    writer = csv.writer(file.csv)
    
    writer.writerow(['Nome', 'Idade', 'Cidade', 'Estado', 'Amigos'])
    
    for linha in linhas:
        row = linha.strip().split('?')
        
        amigos_str = row[-1] #Ultimo elemento da lista ou poderia ser row[4] que seria o conjunto de amigos.
        amigos_set = ast.literal_eval(amigos_str)
        
        amigos_formatados = ', '.join(amigos_set)
        
        row[-1] = amigos_formatados
        
        writer.writerow(row)
        
print("Arquivo CSV criado com sucesso.")
#Utilizando apenas as bibliotecas csv e json, leia os dados do arquivo csv criado no item anterior, parseie as informações para uma estrutura json e exporte o arquivo “INFwebNET.json” devidamente estruturado.
print("Exercicio 2")
'''Abertura do arquivo .CSV, criado uma variável para armazenar todos os dados como dicionários para transformar-los em um arquivo .json'''
dados = []

with open('INFwebNet.csv', mode='r', encoding='utf-8') as file.csv:
    content = csv.DictReader(file.csv)
    
    for row in content:
        #Adicionando cada linha do dicionário dentro da lista(dados)
        dados.append(row)
        
with open('INFwebNET.json', mode='w', encoding='utf-8') as file.json:
#json.dump usado para converter a lista de dicionários em JSON
    json.dump(dados, file.json, indent=4, ensure_ascii=False)#Identação de 4 espaços para uma melhor organização dos dados. Ensure ... usado para caracteres especiais apareçam da forma correta.
    
print("Arquivo JSON criado com sucesso.")
#Crie um programa que permita ao usuário inserir novos INFNETianos (nome, idade, cidade, estado) e salve essas informações no arquivo "“INFwebNET.json", utilizando o módulo json.
print("Exercicio 3")
'''Inserindo novos usuários na rede INFNET. No caso é criado um novo usuário e adicionado em arquivo JSON para atualização dos dados'''
print("Exercicio 3: Carregando dados existentes do arquivo JSON")

# Verifica se o arquivo INFwebNET.json existe
if os.path.exists('INFwebNET.json'):
    with open('INFwebNET.json', 'r', encoding='utf-8') as file:
        try:
            dados_existentes = json.load(file)
        except json.JSONDecodeError:
            dados_existentes = []
else:
    dados_existentes = []

print(f"Dados carregados: {dados_existentes}")

print("\nExercicio 2: Adicionando novos INFNETianos")

while True:
    nome = input("Digite o nome: ")
    idade = input("Digite a idade: ")
    cidade = input("Digite a cidade: ")
    estado = input("Digite o estado: ")

    # Cria um dicionário com os dados do INFNETiano
    novo_infnetiano = {
        "Nome": nome,
        "Idade": idade,
        "Cidade": cidade,
        "Estado": estado
    }

    # Adiciona o novo INFNETiano à lista existente
    dados_existentes.append(novo_infnetiano)

    # Pergunta ao usuário se deseja adicionar outro
    continuar = input("Deseja adicionar outro INFNETiano? (s/n): ").lower()
    if continuar != 's':
        break

print(f"\nNovos dados inseridos: {dados_existentes}")

print("\nExercicio 3: Salvando dados no arquivo JSON")

with open('INFwebNET.json', 'w', encoding='utf-8') as file:
    json.dump(dados_existentes, file, indent=4, ensure_ascii=False)

print("Dados salvos com sucesso no arquivo INFwebNET.json.")
#Utilize o Pandas para ler o arquivo "“INFwebNET.json". Calcule a média de idade dos INFNETianos e exiba o resultado.
print("Exercicio 4")
'''Usando o pandas consigo manipular o arquivo json e conseguir a média das idades.'''
df = pd.read_json('INFwebNET.json', encoding='utf-8')

print("Dados carregados do arquivo JSON: ")
print(df)

idade_media = df['Idade'].mean()

print(f"\nA média das idades é: {idade_media:.2f}")
#Elabore uma função que permita inserir novos INFNETianos na rede INFwebNet incluindo novos campos de dados. Além dos dados já existentes poderão serem incluídos os campos “hobbys” que conterá uma lista de atividades de interesse do INFNETiano, um campo “coding” que deverá conter uma lista de linguagens de programação que INFNETiano utiliza e uma lista de dicionários contendo os campos “jogos” e “plataforma”, onde o usuário poderá informar os jogos favoritos e a respectiva plataforma na qual o INFNETiano jogou aquele jogo.
print("Exercicio 5")
'''Adicionando um novo INFNETIANO e adicionado os novos dados no arquivo JSON'''
with open('INFwebNET.json', mode='r', encoding='utf-8') as file:
    dados_existentes = json.load(file)
    
    nome = input("Digite o nome: ")
    idade = input("Digite o idade: ")
    cidade = input("Digite o cidade: ")
    estado = input("Digite o estado: ")
    
    hobbys = []
    while True:
        hobby = input("Digite um hobby ou pressione enter para continuar: ")
        if hobby == "":
            break  # Sai do loop de hobbies
        hobbys.append(hobby)
    
    # Lista para linguagens de programação
    coding = []
    while True:
        linguagem = input("Digite uma linguagem de programação ou pressione enter para continuar: ")
        if linguagem == "":
            break  # Sai do loop de linguagens
        coding.append(linguagem)
    
    # Lista de jogos
    jogos = []
    while True:
        jogo = input("Digite o nome de um jogo favorito ou pressione enter para continuar: ")
        if jogo == "":
            break  # Sai do loop de jogos
        plataforma = input(f"Digite a plataforma em que jogou {jogo}: ")
        jogos.append({"jogo": jogo, "plataforma": plataforma})
        
        novo_infnetiano = {
            "Nome" : nome,
            "Idade" : idade,
            "Cidade" : cidade,
            "Estado" : estado,
            "Hobbys" : hobbys,
            "Coding" : coding,
            "Jogos" : jogos
                }
                
        dados_existentes.append(novo_infnetiano)
        with open('INFwebNET.json', mode='w', encoding='utf-8') as file:
            json.dump(dados_existentes, file, indent=4, ensure_ascii=False)
                
        print("\nNovo IFNETiano adicionado com sucesso!")
            
with open('INFwebNET.json', 'r', encoding='utf-8') as file:
    dados_existentes = json.load(file)  # Carrega diretamente os dados existentes
    print("\nINFNETianos registrados:")
    for idx, infnetiano in enumerate(dados_existentes, start=1):
        print(f"{idx}. Nome: {infnetiano['Nome']}, Idade: {infnetiano['Idade']}, Cidade: {infnetiano['Cidade']}, Estado: {infnetiano['Estado']}")
        print = print(f"   Hobbys: {', '.join(infnetiano['hobbys'])}")
        print(f"   Coding: {', '.join(infnetiano['Coding'])}")
        print("   Jogos e Plataformas:")
        for jogo in infnetiano['Jogos']:
            print(f"     - Jogo: {jogo['jogo']}, Plataforma: {jogo['plataforma']}")
#A INFwebNET recebeu um arquivo "dados_usuarios_novos.txt" com dados dos novos INFNETianos separados por ponto e vírgula (;). Utilize o módulo csv para ler esse arquivo, especificando o delimitador correto. (O arquivo está disponível no repositório específico do TP2).
print("Exercicio 6")
with open('dados_usuarios_novos.txt', mode='r', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter=';')
    for row in reader:
        print(row)
#Após ter obtido dados de diferentes bases de dados você precisa avançar um passo e reunir todas as informações do INFwebNet em um único DataFrame Pandas. (Lembre-se de estruturar as Séries adequadamente).
print("Exercicio 7")
df_json = pd.read_json('INFwebNET.json', encoding='utf-8')

df_csv = pd.read_csv('INFwebNET.csv',delimiter=';', encoding='utf-8')

df_text1 = pd.read_csv('dados_usuarios_novos.txt', delimiter=';', encoding='utf-8', header=None)
df_text2 = pd.read_csv('rede_INFNET_atualizado.txt', delimiter=';', encoding='utf-8', header=None)

df_text1.columns = ['Nome', 'Idade', 'Cidade', 'Amigos']
df_text2.columns = ['Nome', 'Idade', 'Cidade', 'Amigos']

dfs = [df_json, df_csv, df_text1, df_text2]

colunas_padrao = ['Nome', 'Idade', 'Cidade', 'Amigos']
for df in dfs:
    for col in colunas_padrao:
        if col not in df.columns:
            df[col] = None #Adiciona uma coluna vazia se não existir.
            
df_consolidado = pd.concat(dfs, ignore_index=True) #Ignorando os indices originais, assim o DF pode criar uma sequencia do zero.

print("\nDados Consolidados: ")
print(df_consolidado)

df_consolidado.to_csv('dados_consolidados.csv', index=False, encoding='utf-8')
df_consolidado.to_json('dados_consolidados.json', orient='records', force_ascii=False)
#orient='records' Cada linha é representada como um objeto JSON ou dicionário no python.
print("\nDados consolidados salvos com sucesso!")
#Crie uma nova coluna no dataset chamada “ano_nascimento” considerando a data atual e informação presente na coluna idade.
print("Exercicio 8")
df = pd.DataFrame({
    "Nome": ["João", "Ana", "Carlos"],
    "Idade": [25, 22, 30],
    "Cidade": ["São Paulo", "Rio de Janeiro", "Belo Horizonte"]
})