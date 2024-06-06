import requests
from bs4 import BeautifulSoup
from time import sleep

print("BUSCADOR DE LINKS 8000")
url = str(input("Digite o dominio da pagina: "))
print("Validando link...")
sleep(0.5)
try:
  requests.get(url)
except:
  raise TypeError("Link response != 200, tente escrever novamente...")

print("Link Validado")
print("Buscando links na pagina...")
sleep(1)

# cabeçalho padrao
headers = {"User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1"}
# url = "https://www.google.com.br/search?q=cotacao+dolar"

req = requests.get(url, headers=headers)

site = BeautifulSoup(req.text, "html.parser")
cotacao_dolar = site.findAll("a")

for element in range(0, len(cotacao_dolar)):
  try:
    print(f"{element} = {cotacao_dolar[element]["href"]}")
    print()
    sleep(0.1)
  except:
    print(f"{element} = Elemento não tem link")
    print()
    sleep(0.1)
