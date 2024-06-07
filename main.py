import requests
from time import sleep

print("BUSCADOR DE LINKS 8000")
from bs4 import BeautifulSoup

# solicitando url para o usuario
url = str(input("Digite o dominio da pagina: "))
print("Validando link...")
sleep(0.5)

# fazendo teste de response do link - programa para caso o link não estiver certo
try:
  requests.get(url)
except:
  raise TypeError("Link response != 200, tente escrever novamente...")
print("Link Validado")

# apartir daqui se inicia a pesquisa de links
print("Buscando links na pagina...")
sleep(1)

# cabeçalho padrao para o navegador
headers = {"User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1"}

# requisicao da pagina
req = requests.get(url, headers=headers)

# convertendo requisicao para o soup
site = BeautifulSoup(req.text, "html.parser")

# procurando tags <a> onde se encontra o link
site_text = site.findAll("a")

# para cada elemento que contenha <a> print o numero do elemento e o atributo href onde se encontra o link
for element in range(0, len(site_text)):
  # tente printar o href
  try:
    print(f"{element} = {site_text[element]['href']}")
    print()
    sleep(0.1)
  # caso nao tenha o elemento <a> nao tenha href
  except:
    print(f"{element} = Elemento não tem link")
    print()
    sleep(0.1)
