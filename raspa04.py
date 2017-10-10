from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen(
    "http://www.portaltransparencia.gov.br/copa2014/api/rest/empreendimento")
bsObj = BeautifulSoup(html, "xml")
valores = bsObj.findAll('valorTotalPrevisto')

soma = 0
for v in valores:
    soma += float(v.get_text())


print(soma)
