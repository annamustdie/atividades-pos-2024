from xml.dom.minidom import parse

def mostrar_detalhes_imovel(imovel):
    descricao = imovel.getElementsByTagName('descricao')[0].firstChild.nodeValue
    proprietario_nome = imovel.getElementsByTagName('nome')[0].firstChild.nodeValue
    telefones = imovel.getElementsByTagName('telefone')
    email_element = imovel.getElementsByTagName('email')
    endereco_rua = imovel.getElementsByTagName('rua')[0].firstChild.nodeValue
    endereco_numero = imovel.getElementsByTagName('numero')[0].firstChild.nodeValue if imovel.getElementsByTagName('numero') else 'S/N'
    endereco_bairro = imovel.getElementsByTagName('bairro')[0].firstChild.nodeValue
    endereco_cidade = imovel.getElementsByTagName('cidade')[0].firstChild.nodeValue
    tamanho = imovel.getElementsByTagName('tamanho')[0].firstChild.nodeValue
    num_quartos = imovel.getElementsByTagName('numQuartos')[0].firstChild.nodeValue
    num_banheiros = imovel.getElementsByTagName('numBanheiros')[0].firstChild.nodeValue
    valor = imovel.getElementsByTagName('valor')[0].firstChild.nodeValue
    
    print(f"\nDescrição: {descricao}")
    print(f"Proprietário: {proprietario_nome}")
    if email_element:
        print(f"Email: {email_element[0].firstChild.nodeValue}")
    print("Telefones:")
    for telefone in telefones:
        print(f"  - {telefone.firstChild.nodeValue}")
    print(f"Endereço: {endereco_rua}, {endereco_numero}, {endereco_bairro}, {endereco_cidade}")
    print(f"Tamanho: {tamanho} m²")
    print(f"Quartos: {num_quartos}")
    print(f"Banheiros: {num_banheiros}")
    print(f"Valor: R$ {float(valor):,.2f}")

dom = parse("xml/imobiliaria.xml")

imobiliaria = dom.documentElement

imoveis = imobiliaria.getElementsByTagName('imovel')

for x, imovel in enumerate(imoveis, start=1):
    descricao_imovel = imovel.getElementsByTagName('descricao')[0].firstChild.nodeValue
    print(f"{x} - {descricao_imovel}")

id_escolhido = input("\nDigite o ID do imóvel para ver mais detalhes: ")

imovel_selecionado = None
if id_escolhido.isdigit():
    id_escolhido = int(id_escolhido)
    if 1 <= id_escolhido <= len(imoveis):
        imovel_selecionado = imoveis[id_escolhido - 1]

if imovel_selecionado:
    mostrar_detalhes_imovel(imovel_selecionado)
else:
    print("Imóvel não encontrado")
