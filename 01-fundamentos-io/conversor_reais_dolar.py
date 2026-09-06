valor_em_reais = float(input("Digite o valor em Reais: "))
cotacao_dolar = float(input("Digite a cotação atual do Dólar: "))

valor_em_dolar = valor_em_reais / cotacao_dolar
print(f"{valor_em_reais:.2f} Reais equivalem a {valor_em_dolar:.2f} Dólares.")
