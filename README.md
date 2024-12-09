Review Assignment Due Date Open in Codespaces Contexto: Você continua como cientista de dados na INFwebNET, agora com novas responsabilidades relacionadas ao gerenciamento e análise de dados armazenados em arquivos Excel e um banco de dados SQL. Os exercícios a seguir irão guiá-lo por situações práticas que abrangem a manipulação de dados, tratamento de exceções e o uso do SQL para nossa rede social fictícia.
Prepare-se para consolidar e expandir suas habilidades!
Leia todo o enunciado.
Você pode decidir atender a mais de um item com uma única função se achar conveniente, indique quais itens estão sendo atendidos em cada trecho ou bloco de código.

Sinal vermelho.
Questões:
Tratamento de Erros ao Carregar Arquivo
Abra o arquivo "dados_usuarios.csv" usando o bloco try...except. Exiba uma mensagem de erro se o arquivo não for encontrado (erro específico) e informe ao usuário que o arquivo está em falta.

Explorando Dados do Excel
Abra o arquivo "dados_usuarios.csv", que contém informações dos usuários. Exiba as 10 primeiras linhas do arquivo e liste todas as colunas presentes no arquivo.

Manipulação de Dados Básica
Usando Pandas, selecione apenas os usuários com idade maior que 30 e salve esses dados em um novo arquivo chamado "INFwebNET_30mais.xlsx".

Limpeza de Dados
Para o DataFrame anterior proceda com as seguintes tarefas de limpeza de dados:

Remova todos os usuários que não possuírem e-mail válido cadastrado.

Preencha os valores ausente do campo “cidade” com o texto “Não Informada”.

Preencha os dados ausentes na coluna “estado” com “ZZ”.

Combinação de Arquivos Excel
A INFwebNET possui dados históricos de usuários em arquivo Excel com o nome “INFwebNET_Historico.xlsx”, onde há duas tabelas, “INFwebNET2022” e “INFwebNET2023”, cada uma referente a um ano.
Use um bloco try...except para carregar as planilhas do arquivo "INFwebNET_Historico.xlsx" e, se o arquivo for carregado com sucesso, exiba o número total de linhas de cada planilha. Caso ocorra uma exceção, mostre uma mensagem de erro apropriada.

Combinação de Arquivos Excel
Carregue a informação das duas planilhas, combine as informações em um único DataFrame e remova duplicatas baseado na coluna "id".

Carregando Dados em SQL
Conecte-se a um banco de dados SQLite chamado "INFwebNET_DB.db" usando SQLAlchemy. Carregue os dados combinados do item anterior para uma tabela chamada "Usuarios_Historicos".

Consultando o Banco de Dados SQL
Escreva uma consulta usando Pandas que retorne apenas os usuários com idade entre 22 e 30 anos existentes na tabela “Usuarios_Historicos”. Exiba o resultado na tela.

Consolidando Dados
Utilizando o Pandas e SQLAlchemy crie uma nova tabela no banco de dados chamada “Consolidado” e insira nesta tabela todos os dados obtidos nos itens anteriores.

Atualizando idade
Consulte todos os dados da tabela “Consolidado” e recalcule a idade de todos os usuários considerando a data de 22 de julho de 2024. Exporte os dados atualizados para uma tabela SQL chamada “Consolidado_Atualizado”.

Exceção Customizada para Dados Ausentes
Implemente uma função que leia os dados da tabela “Consolidado” e lance uma exceção customizada chamada "DadosAusentesError" se alguma coluna apresentar um dado faltante. Utilize um bloco try...except para capturar essa exceção e listar o e-mail do INFNETiano em questão caso a exceção seja levantada, e salve o e-mail em um arquivo txt chamado, “dados_ausentes.txt”.

Try…Except Completo
Escreva uma função que leia todos os arquivos: “dados_usuario.csv”, “INFwebNET_30mais.xlsx", “INFwebNET_Historico.xlsx”, "INFwebNET_DB.db" e “dados_ausentes.txt” utilizando uma estrutura try...except completa de forma que cada tentativa de leitura seja feita dentro de um try que capture e lide com os seguintes tipos de exceções: `FileNotFoundError`, `MemoryError`, `RuntimeError`, `EOFError`, `OSError`, `ConnectionError`, `TimeoutError` e `PermissionError`.

Lide com cada tipo de exceção exibindo uma mensagem apropriada e segua para o próximo arquivo ou encerre o programa quando for apropriado.
Utilize um bloco else para exibir a quantidade de linhas existentes no arquivo lido
Utilize um bloco finally para garantir o fechamento do arquivo ou da conexão.
Entrega:
Para a entrega, certifique-se de incluir o banco de dados SQLite e arquivos resultantes de todas as manipulações e códigos em .py ou .ipynb.
A entrega deverá ser feita pelo repositório desta atividade e em um arquivo zip através da plataforma.
