import json

def faturamento_diario(faturamento_json):
    with open(faturamento_json, 'r') as file:
        dados = json.load(file)
    
    valores = [dia['valor'] for dia in dados if dia['valor'] > 0]
    menor_valor = min(valores)
    maior_valor = max(valores)
    media = sum(valores) / len(valores)
    dias_acima_media = sum(1 for valor in valores if valor > media)

    print(f"Menor valor de faturamento: {menor_valor}")
    print(f"Maior valor de faturamento: {maior_valor}")
    print(f"Número de dias com faturamento acima da média: {dias_acima_media}")

arquivo_json = "dados.json"
faturamento_diario(arquivo_json)
