import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

url = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_1.csv"
url2 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_2.csv"
url3 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_3.csv"
url4 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_4.csv"

loja1 = pd.read_csv(url)
loja2 = pd.read_csv(url2)
loja3 = pd.read_csv(url3)
loja4 = pd.read_csv(url4)

loja1['Loja'] = 'Loja 1'
loja2['Loja'] = 'Loja 2'
loja3['Loja'] = 'Loja 3'
loja4['Loja'] = 'Loja 4'

dados = pd.concat([loja1, loja2, loja3, loja4], ignore_index=True)

dados.head()

print(dados.info())
print(dados.head())

# Calcule o faturamento total e médio
print(f"Faturamento total: R${dados['Preço'].sum():,.2f}")
print(f"Faturamento médio: R${dados['Preço'].mean():,.2f}")

# Faturamento por loja
plt.figure(figsize=(10,5))
sns.barplot(x="Loja", y="Preço", data=dados, estimator=sum)
plt.title("Faturamento por Loja")
plt.ylabel("Faturamento Total (R$)")
plt.xlabel("Loja")
plt.xticks(rotation=45)
plt.show()

# Faturamento ao longo do tempo
dados['Data da Compra'] = pd.to_datetime(dados['Data da Compra'], dayfirst=True)

dados_por_data = dados.groupby(dados['Data da Compra'].dt.year)['Preço'].sum()

plt.figure(figsize=(10,5))
sns.lineplot(x=dados_por_data.index, y=dados_por_data.values, marker="o")
plt.title("Evolução do Faturamento ao Longo dos Anos")
plt.xlabel("Ano")
plt.ylabel("Faturamento Total (R$)")
plt.grid()
plt.show()

# Vendas por Categoria (gráfico de pizza)
vendas_categoria = dados.groupby("Categoria do Produto")["Preço"].sum()
plt.figure(figsize=(8,8))
plt.pie(vendas_categoria, labels=vendas_categoria.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette("pastel"))
plt.title("Distribuição das Vendas por Categoria")
plt.show()

# Média de Avaliação das Lojas (gráfico de barras)
avaliacao_lojas = dados.groupby("Loja")["Avaliação da compra"].mean().reset_index()
plt.figure(figsize=(8,5))
sns.barplot(x="Loja", y="Avaliação da compra", data=avaliacao_lojas, palette="Blues")
plt.title("Média de Avaliação das Lojas")
plt.ylabel("Avaliação Média")
plt.xlabel("Loja")
plt.ylim(0, 5)
plt.show()

# Frete Médio por Loja (gráfico de linha)
frete_medio_loja = dados.groupby("Loja")["Frete"].mean().reset_index()
plt.figure(figsize=(8,5))
sns.lineplot(x="Loja", y="Frete", data=frete_medio_loja, marker="o", color="red")
plt.title("Frete Médio por Loja")
plt.ylabel("Frete Médio (R$)")
plt.xlabel("Loja")
plt.grid()
plt.show()

# Produtos mais vendidos (gráfico de barras horizontal)
produtos_vendidos = dados.groupby("Produto")["Produto"].count().reset_index(name="Quantidade Vendida")
produtos_vendidos = produtos_vendidos.sort_values(by="Quantidade Vendida", ascending=False).head(10)

plt.figure(figsize=(10,6))
sns.barplot(y="Produto", x="Quantidade Vendida", data=produtos_vendidos, palette="Greens")
plt.title("Top 10 Produtos Mais Vendidos")
plt.ylabel("Produto")
plt.xlabel("Quantidade Vendida")
plt.show()

#Faturamento total por loja
faturamento_loja = dados.groupby("Loja")["Preço"].sum().reset_index()
print(faturamento_loja)