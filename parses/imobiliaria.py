import xml.etree.ElementTree as ET
import json

arquivo_caminho = r'C:\Users\20211181110030\Downloads\atividades-pos-2024\xml\imobiliaria.xml'

def xml_para_dicionario(elemento):
    dict_dados = {}
    if len(elemento):
        for filho in elemento:
            if len(filho) > 0:  
                if filho.tag not in dict_dados:
                    dict_dados[filho.tag] = []
                dict_dados[filho.tag].append(xml_para_dicionario(filho))
            else:
                dict_dados[filho.tag] = filho.text
    return dict_dados


with open(arquivo_caminho, 'r', encoding='utf-8') as arquivo:
    dados_xml = arquivo.read()
raiz = ET.fromstring(dados_xml)

lista_imoveis = [xml_para_dicionario(imovel) for imovel in raiz.findall('imovel')]

estrutura_imobiliaria = {"imobiliaria": lista_imoveis}
dados_json = json.dumps(estrutura_imobiliaria, indent=4, ensure_ascii=False)

print(dados_json)
