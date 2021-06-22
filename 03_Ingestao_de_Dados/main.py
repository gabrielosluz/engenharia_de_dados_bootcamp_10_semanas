import requests
import json

url = 'https://economia.awesomeapi.com.br/last/USD-BRL/'
ret = requests.get(url)

if ret:
    print(ret)
else:
    print("Deu ruim malandro")

dolar = json.loads(ret.text)['USDBRL']

dolar['bid']

print( f" 20 Dólares hoje custam {float(dolar['bid']) * 20} reais")

def cotacao(valor, moeda):
    url = f'https://economia.awesomeapi.com.br/last/{moeda}/'
    ret = requests.get(url)
    dolar = json.loads(ret.text)[moeda.replace('-','')]
    print( f" {valor} {moeda[:3]} hoje custam {float(dolar['bid']) * valor} {moeda[-3:]}")

cotacao(20, 'USD-BRL')

try:
    cotacao(20, 'JPY-BRL')
except:
    pass

try:
    10/0
except Exception as e:
    print(e)

lst_money = [
        "USD-BRL",
        "EUR-BRL",
        "BTC-BRL",
        "RPL-BRL",
        "JPY-BRL",
        "RPL-BRL"
    ]

valor = 20

for moeda in lst_money:
    try:
        url = f'https://economia.awesomeapi.com.br/last/{moeda}/'
        ret = requests.get(url)
        dolar = json.loads(ret.text)[moeda.replace('-','')]
        print( f" {valor} {moeda[:3]} hoje custam {float(dolar['bid']) * valor} {moeda[-3:]}")
    except:
        print(f"Falha na moeda: {moeda}")

def multi_moeda(valor):
    lst_money = [
        "USD-BRL",
        "EUR-BRL",
        "BTC-BRL",
        "RPL-BRL",
        "JPY-BRL"
    ]

    for moeda in lst_money:
        url = f'https://economia.awesomeapi.com.br/last/{moeda}/'
        ret = requests.get(url)
        dolar = json.loads(ret.text)[moeda.replace('-','')]
        print( f" {valor} {moeda[:3]} hoje custam {float(dolar['bid']) * valor} {moeda[-3:]}")


multi_moeda(20)



