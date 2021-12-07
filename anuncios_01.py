import json
from colorama import Fore, Style, init

with open("anuncios.json", "rb") as f:
    anuncios = json.load(f)

pos = 0
keys = []
lista_terreno = []
lista_industrial = []
lista_galpao = []

global valorBaixo
valorBaixo = 10000000

global valorAlto
valorAlto = 0

umBanheiro = 0
doisBanheiros = 0
tresBanheiros = 0

umQuarto = 0
doisQuartos = 0
tresQuartos = 0

area120m = 0

casa = 0
apartamento = 0
kitnet = 0
terreno = 0
galpao = 0
industrial = 0

umaGaragem = 0
duasGaragem = 0

vigia = 0
arcondicionado = 0
esquina = 0
escritório = 0
circuito_de_segurança = 0
cameras_de_segurança = 0
seguranca_24h = 0
sistema_de_alarme = 0
vigilancia = 0
gerador = 0
cerca = 0
deposito = 0
gas_encanado = 0

imoveis_com_seguranca = 0
lista_imoveis_com_seguranca = []

#Pegando as chaves existentes dos dados para saber com que dados estou trabalhando
for key in anuncios[0].keys(): 
    keys.append(key)

#Pegando um modelo de dado
for x in anuncios:
    check_seguranca = 0
    
    #Dados variaveis globais para os valores 
    if x['valor'] < valorBaixo and x['valor'] > 300:
        valorBaixo = x['valor']
    
    if x['valor'] > valorAlto:
        valorAlto = x['valor']
    
    #Dados quartos
    try:
        if x['quarto'] == 1:
            umQuarto += 1
        
        if x['quarto'] == 2:
            doisQuartos += 1
            
        if x['quarto'] >= 3:
            tresQuartos += 1
    except:
        pass  
     
    #Dados banheiros
    try:
        if x['banheiro'] == 1:
            umBanheiro += 1
        
        if x['banheiro'] == 2:
            doisBanheiros += 1
            
        if x['banheiro'] >= 3:
            tresBanheiros += 1
    except:
        pass  
     
    #Area total
    try:
        if x['area_total'] >= 120:
            area120m += 1
    except:
        pass
       
    #Tipo imovel
    try:
        if x['tipo_imovel'][0] == "Casa":
            casa += 1
        elif x['tipo_imovel'][0] == "Apartamento":
            apartamento += 1
        elif x['tipo_imovel'][0] == "Kitnet":
            kitnet += 1
        elif x['tipo_imovel'][0] == "Terreno":
            terreno += 1
            lista_terreno.append(pos)
        elif x['tipo_imovel'][0] == "Galpão":
            galpao += 1
            lista_galpao.append(pos)
        elif x['tipo_imovel'][0] == "Industrial":
            industrial += 1
            lista_industrial.append(pos)
        #else:
        #    print(x['tipo_imovel'])
    except:
        pass  
     
    #Dados garagem
    try:
        if x['garagem'] == 1:
            umaGaragem += 1
            
        if x['garagem'] >= 2:
            duasGaragem += 1    
    except:
        pass
        
    #Opcionais
    try:
        for y in x['opcionais']:            
            if y['name'] == 'Vigia':
                vigia += 1
            if y['name'] == 'Ar condicionado':
                arcondicionado += 1
            if y['name'] == 'Esquina':
                esquina += 1
            if y['name'] == 'Escritório':
                escritório += 1
            if y['name'] == 'Circuito de segurança':
                circuito_de_segurança += 1
                check_seguranca += 1
            if y['name'] == 'Câmeras de segurança':
                cameras_de_segurança += 1
                check_seguranca += 1
            if y['name'] == 'Segurança 24h':
                seguranca_24h += 1
            if y['name'] == 'Sistema de alarme':
                sistema_de_alarme += 1
            if y['name'] == 'Vigilancia':
                vigilancia += 1
            if y['name'] == 'Cerca':
                cerca += 1
            if y['name'] == 'Gerador':
                gerador += 1
            if y['name'] == 'Depósito':
                deposito += 1
            if y['name'] == 'Gas encanado':
                gas_encanado += 1
    except:
        pass

    #Verificando o imovel se encaixa com os 2 padroes estabelecidos 
    if check_seguranca == 2:
        lista_imoveis_com_seguranca.append(pos)
        imoveis_com_seguranca += 1
    
    pos = pos + 1
        
"""    for y in x:
        if y == "opcionais":
            print("Opcionais:")
            for z in x[y]:
                print(z)
            input()
        else:
            print(f"{y}: {x[y]}")"""


print(f"""
INFORMAÇÕES GERAIS
------------------------------------------------------------------------------
Menor preço de imóvel: {valorBaixo}
Maior preço de imóvel: {valorAlto}

Imoveis com um banheiro: {umBanheiro}
Imoveis com dois banheiros: {doisBanheiros}
Imoveis com três banheiros ou mais: {tresBanheiros}

Imoveis com um quarto: {umQuarto}
Imoveis com dois quartos: {doisQuartos}
Imoveis com três quartos ou mais: {tresQuartos}

Imoveis com uma garagem: {umaGaragem}
Imoveis com duas garagens ou mais: {duasGaragem}

Imoveis com área total maior que 120m2: {area120m}

Casa: {casa}
Apartamento: {apartamento}
Kitnet: {kitnet}
Terreno: {terreno}
Galpão: {galpao}
Industrial: {industrial}

OPCIONAIS:
Esquina: {esquina}
Ar condicionado: {arcondicionado}
Deposito: {deposito}
Escritório: {escritório}
Vigia: {vigia}
Cerca: {cerca}
Circuito de segurança: {circuito_de_segurança}
Câmeras de segurança: {cameras_de_segurança}
Segurança 24h: {seguranca_24h}
Sistema de alarme: {sistema_de_alarme}
Vigilância: {vigilancia}
Gerador: {gerador}
Gas encanado: {gas_encanado}

Imoveis com segurança: {imoveis_com_seguranca}

Qtd de dados: {len(anuncios)}
------------------------------------------------------------------------------
""")