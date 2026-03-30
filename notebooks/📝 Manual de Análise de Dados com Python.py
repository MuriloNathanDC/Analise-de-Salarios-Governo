📝 Manual de Análise de Dados com Python (Roteiro Prático)
1️⃣ Preparação do ambiente
# Importando bibliotecas essenciais
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Configurações opcionais
pd.set_option("display.max_columns", None)  # mostra todas as colunas
pd.set_option("display.max_rows", 100)      # mostra até 100 linhas
sns.set(style="whitegrid")                  # estilo dos gráficos
2️⃣ Carregar dados
# CSV
df = pd.read_csv("data/raw/TB_RH.csv", sep=';', encoding='latin1')

# Excel
# df = pd.read_excel("data/raw/arquivo.xlsx", sheet_name="Sheet1")

✅ Verificar primeiras linhas

df.head()       # primeiras 5 linhas
df.tail()       # últimas 5 linhas
df.sample(5)    # 5 linhas aleatórias
3️⃣ Estrutura do dataset
df.shape        # linhas e colunas
df.columns      # nomes das colunas
df.dtypes       # tipos de dados de cada coluna
df.info()       # resumo geral
4️⃣ Estatísticas básicas
df.describe()              # estatísticas de colunas numéricas
df.describe(include='all') # estatísticas de todas as colunas
5️⃣ Valores nulos e vazios
df.isnull().sum()            # quantidade de nulos por coluna
df.isna().sum()              # mesma coisa
df.dropna()                  # remove linhas com qualquer NA
df.dropna(how='all')         # remove linhas totalmente vazias
df.fillna("Não Informado")   # preenche nulos
6️⃣ Visualizar dados únicos
df['cargo'].unique()         # valores únicos
df['cargo'].value_counts()   # contagem de cada valor
7️⃣ Filtrar dados
df_ativos = df[df['ult_remu_bruta'] > 0]  # só quem tem salário
df_saude = df[df['instituicao'].str.contains("SAUDE")]  # só saúde
8️⃣ Selecionar colunas
df[['nome', 'cargo', 'ult_remu_bruta']]    # seleciona colunas específicas
9️⃣ Ordenar dados
df.sort_values(by='ult_remu_bruta', ascending=False)  # maior salário primeiro
10️⃣ Agrupar dados (Resumir)
# Média de salários por cargo
df.groupby('cargo')['ult_remu_bruta'].mean().sort_values(ascending=False)

# Contagem de cargos por instituição
df.groupby('instituicao')['cargo'].count()
11️⃣ Criar novas colunas
# Idade
df['idade'] = 2026 - df['ano_nasc']

# Faixa salarial
df['faixa_remu'] = pd.cut(df['ult_remu_bruta'], bins=[0, 2000, 5000, 10000, 20000, 70000], labels=['0-2k','2-5k','5-10k','10-20k','20k+'])
12️⃣ Visualização rápida
# Histograma
df['ult_remu_bruta'].hist(bins=30)

# Boxplot por cargo
plt.figure(figsize=(12,6))
sns.boxplot(x='cargo', y='ult_remu_bruta', data=df_ativos)
plt.xticks(rotation=90)

# Gráfico de barras por instituição
df.groupby('instituicao')['ult_remu_bruta'].mean().plot(kind='bar', figsize=(12,6))
13️⃣ Limpeza de dados grande (redução de tamanho)
# Remover colunas irrelevantes
colunas_para_remover = ['dt_inicio','dt_fim','atualizado','quadro_funcional_desc']
df.drop(columns=colunas_para_remover, inplace=True)

# Remover linhas sem salário
df = df[df['ult_remu_bruta'] > 0]

# Preencher lotacao nula
df['lotacao'] = df['lotacao'].fillna("Não Informado")

# Criar sample leve para GitHub
df_sample = df.sample(1000, random_state=42)
df_sample.to_csv("data/processed/sample_limpo.csv", index=False)
14️⃣ Exportar dados
# CSV
df.to_csv("data/processed/dados_limpos.csv", index=False)

# Excel
df.to_excel("data/processed/dados_limpos.xlsx", index=False)
15️⃣ Dicas extras
Sempre verifique nulos antes de agrupar ou analisar.
Sempre visualize a distribuição de colunas numéricas (histogramas, boxplots).
Use sample() quando o dataset for gigante para teste/portfólio.
Use pd.cut ou pd.qcut para criar categorias.
Evite subir arquivos maiores que 100 MB no GitHub.