import pandas 
import pandas as pd
                    ## FAZER DOWNLOAD DO XAMPP NA MAQUINA E ATIVAR ALGUMAS FUNÇÕES##
# try:
#     print("Tentando importar o pandas")
#     import pandas as pd
#     print("Pandas importado com sucesso")

#     ## É uma boa pratica verificar a versão do pandas instalada no sistema
#     ## sys.version.split()[0] - serve para verificar qual a versão instalda do pandas no sistema da máquina

#     print(f"Versão do Pandas instalada: {pd.__version__}")
#     print(f"Versão do python: {sys.version.split()[0]}")

# except ImportError:
#     print("\n --- ERRO ---")
#     print("A biblioteca Pandas não foi encontrada")
#     print("Por favor, instale-a usando o comando")
#     print("pip install pandas")

# except Exception as e:
#     print("Ocorreu um erro inesperado: {e}")

# finally:
#     print("Verificação de setup concluída.\n")


# ##################################

# dados_salarios={
#     "analista de dados" = 7000.50
#     "cientista de dados" = 12000.00
#     "engenheiro de dados" = 11000.00
#     "analista de BI" = 6500.00
# }



# --- 3. Criando um DataFrame (Estrutura 2D) ---

# try:
#     print("--- Criando um DataFrame (2D) de Filmes ---")
    
#     dados_filmes = {
#         'nome_do_filme': ['O Poderoso Chefão', 'Interestelar', 'Parasita', 'Matrix'],
#         'ano_de_lancamento': [1972, 2014, 2019, 1999],
#         'genero': ['Criminal', 'Ficção Científica', 'Suspense', 'Ficção Científica']
#     }
    
#     # Criamos o DataFrame a partir do dicionário
#     df_filmes = pd.DataFrame(dados_filmes)
    
#     print("\n--- DataFrame Criado ---")
#     print(df_filmes)
    
#     print("\n--- Informações do DataFrame (.info()) ---")
#     df_filmes.info()
    
# except NameError:
#     print("\nERRO: O pandas (pd) não foi importado corretamente.")
# except Exception as e:
#     print(f"Ocorreu um erro ao criar o DataFrame: {e}")
# finally:
#     print("Criação de DataFrame concluída.\n")


# --- 4. Lendo um Arquivo CSV ---

# Defina o nome do arquivo que você baixou
nome_do_arquivo_csv = 'ClassicDisco.csv'
df_disco = None # Inicializamos o DataFrame como None

try:
    print(f"--- Lendo o arquivo '{nome_do_arquivo_csv}' ---")
    
    # O comando mágico para ler CSV!
    df_disco = pd.read_csv(nome_do_arquivo_csv)
    
    print("Arquivo lido com sucesso!")
    
    # Vamos espiar os dados. .head() mostra as 5 primeiras linhas
    print("\n--- As 5 primeiras linhas do DataFrame (.head()) ---")
    print(df_disco.head())
    
    # .info() nos dá um resumo das colunas e tipos de dados
    print("\n--- Informações do DataFrame (.info()) ---")
    df_disco.info()

except FileNotFoundError:
    print(f"\n--- ERRO: Arquivo não encontrado ---")
    print(f"O arquivo '{nome_do_arquivo_csv}' não foi encontrado no diretório.")
    print("Por favor, baixe o CSV do Kaggle e coloque-o na mesma pasta do script.")
except NameError:
    print("\nERRO: O pandas (pd) não foi importado corretamente.")
except Exception as e:
    print(f"Ocorreu um erro ao ler o arquivo CSV: {e}")
finally:
    print("Leitura de CSV concluída.\n")
