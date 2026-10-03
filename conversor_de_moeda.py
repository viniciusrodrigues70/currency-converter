import requests

IOF_TAX = 3.5

def buscar_cotacao():
    url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"

    try:
        response = requests.get(url, timeout= 5)
        response.raise_for_status()
        data = response.json()
        return float(data["USDBRL"]["bid"])

    except requests.RequestException:
        return None

try:
   valor_usd = float(input("Quantos dólares você quer? "))
   
except ValueError:
    print("Número Inválido!")
    exit()

valor_dolar = buscar_cotacao()

if valor_dolar is None:
    print("Não consegui buscar a cotação, me perdoeeeee! :(")
    exit()

valor_base = valor_dolar*valor_usd
valor_imposto = valor_base*(IOF_TAX/100)
valor_total = valor_base+valor_imposto

print(f"Cotação atual: R$ {valor_dolar:.2f}")
print(f"Valor base: R$ {valor_base:.2f}")
print(f"Valor do imposto: R$ {valor_imposto:.2f}")
print(f"Valor total com IOF: R$ {valor_total:.2f}") 