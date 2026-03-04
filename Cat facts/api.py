import requests
from googletrans import Translator

# pegar fato sobre gatos
API = "https://catfact.ninja/fact"
data = requests.get(API, timeout=10).json()
fato = data["fact"]

print("Fato sobre gato (original):")
print(fato)

# traduzir fato
translator = Translator()
traducao = translator.translate(fato, dest="pt")

print("Fato sobre gato (em português):")
print(traducao.text)