import pandas as pd
import matplotlib.pyplot as plt

from utils.general_functions import get_most_recent_file

def plot_mercadoria_vs_quantidade():
    directory = "../data/csv"
    file_prefix = "paranagua_ships"
    recent_file = get_most_recent_file(directory, file_prefix)
    df = pd.read_csv(recent_file, delimiter=",")

    df["SaldoTotal"] = df["SaldoTotal"].str.replace(".", "").str.replace(",", ".").str.extract("(\d+\.\d+)").astype(float)
    mercadoria_totais = df.groupby("Mercadoria")["SaldoTotal"].sum().sort_values(ascending=True)

    plt.figure(figsize=(12, 6))
    mercadoria_totais.plot(kind="barh", color="skyblue")
    plt.title("Distribuição de Quantidade por Tipo de Mercadoria")
    plt.xlabel("Quantidade Total (Tons)")
    plt.ylabel("Tipo de Mercadoria")
    plt.tight_layout()
    plt.show()

def plot_sentido_operacoes():
    directory = "../data/csv"
    file_prefix = "paranagua_ships"
    recent_file = get_most_recent_file(directory, file_prefix)
    df = pd.read_csv(recent_file, delimiter=",")
    
    sentido_counts = df["Sentido"].value_counts()
    for sentido in sentido_counts.index:
        if sentido not in ["Imp", "Exp", "Imp/Exp"]:
            sentido_counts.drop(sentido, inplace=True)

    plt.figure(figsize=(8, 8))
    plt.pie(sentido_counts, labels=sentido_counts.index, autopct="%1.1f%%", startangle=90, colors=["skyblue", "lightgreen", "lightcoral"])
    plt.title("Distribuição das Operações por Sentido (Importação/Exportação)")
    plt.tight_layout()
    plt.show()

def plot_top_operadores():
    directory = "../data/csv"
    file_prefix = "paranagua_ships"
    recent_file = get_most_recent_file(directory, file_prefix)
    df = pd.read_csv(recent_file, delimiter=",")
    
    df["SaldoTotal"] = df["SaldoTotal"].str.replace(".", "").str.replace(",", ".").str.extract("(\d+\.\d+)").astype(float)
    operadores_totais = df.groupby("Operador")["SaldoTotal"].sum().nlargest(5)

    plt.figure(figsize=(10, 6))
    operadores_totais.plot(kind="bar", color="orange")
    plt.title("Top 5 Operadores com Maior Movimentação")
    plt.ylabel("Saldo Total (Tons)")
    plt.xlabel("Operador")
    plt.tight_layout()
    plt.show()

def plot_prancha_por_embarcacao():
    directory = "../data/csv"
    file_prefix = "paranagua_ships"
    recent_file = get_most_recent_file(directory, file_prefix)
    df = pd.read_csv(recent_file, delimiter=",")
    
    df["Prancha(t/dia)"] = df["Prancha(t/dia)"].str.replace(",", ".").astype(float)
    prancha_totais = df.groupby("Embarcação")["Prancha(t/dia)"].mean().nlargest(10)

    plt.figure(figsize=(12, 6))
    prancha_totais.plot(kind="bar", color="purple")
    plt.title("Top 10 Embarcações com Maior Prancha (Toneladas/Dia)")
    plt.xlabel("Embarcação")
    plt.ylabel("Prancha (t/dia)")
    plt.tight_layout()
    plt.show()

def plot_loa_vs_saldo():
    directory = "../data/csv"
    file_prefix = "paranagua_ships"
    recent_file = get_most_recent_file(directory, file_prefix)
    df = pd.read_csv(recent_file, delimiter=",")
    
    df["LOA"] = df["LOA"].str.replace(",", ".").astype(float)
    df["SaldoTotal"] = df["SaldoTotal"].str.replace(".", "").str.replace(",", ".").str.extract("(\d+\.\d+)").astype(float)

    plt.figure(figsize=(10, 6))
    plt.scatter(df["LOA"], df["SaldoTotal"], color="green", alpha=0.6)
    plt.title("Relação entre LOA (Comprimento) e Saldo Total")
    plt.xlabel("LOA (m)")
    plt.ylabel("Saldo Total (Tons)")
    plt.tight_layout()
    plt.show()
