from xml.dom.minidom import parse

def mostrar_detalhes_prato(prato):
    nome = prato.getElementsByTagName('nome')[0].firstChild.nodeValue
    descricao = prato.getElementsByTagName('descricao')[0].firstChild.nodeValue
    ingredientes = prato.getElementsByTagName('ingrediente')
    preco = prato.getElementsByTagName('preco')[0].firstChild.nodeValue
    calorias = prato.getElementsByTagName('calorias')[0].firstChild.nodeValue
    tempo_preparo = prato.getElementsByTagName('tempoPreparo')[0].firstChild.nodeValue
    
    print(f"\nNome: {nome}")
    print(f"Descrição: {descricao}")
    print("Ingredientes:")
    for ingrediente in ingredientes:
        print(f"  - {ingrediente.firstChild.nodeValue}")
    print(f"Preço: R$ {preco}")
    print(f"Calorias: {calorias} kcal")
    print(f"Tempo de preparo: {tempo_preparo}")

dom = parse("cardapio.xml")

cardapio = dom.documentElement

pratos = cardapio.getElementsByTagName('prato')

for prato in pratos:
    id_prato = prato.getElementsByTagName('id')[0].firstChild.nodeValue
    nome_prato = prato.getElementsByTagName('nome')[0].firstChild.nodeValue
    print(f"{id_prato} - {nome_prato}")

id_escolhido = input("\nDigite o ID do prato para ver mais detalhes: ")

prato_selecionado = None
for prato in pratos:
    if prato.getElementsByTagName('id')[0].firstChild.nodeValue == id_escolhido:
        prato_selecionado = prato
        break

if prato_selecionado:
    mostrar_detalhes_prato(prato_selecionado)
else:
    print("Prato não encontrado.")
