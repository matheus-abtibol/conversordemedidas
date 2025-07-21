def conversor_c_f (valor):

    return(valor * 9/5) + 32

def conversor_f_c (valor):

    return(valor - 32) * 5/9
def conversor_k_c (valor):
    return valor - 273.15

def conversor_c_k (valor):
    return valor + 273.15
def conversor_f_k(valor):
    return ((valor - 32) * 5/9) + 273.15
def conversor_k_f(valor):
    return ((valor - 273.15) * 9/5) + 32
# Conversor de Tempo
def conversor_h_m(valor):
    return valor * 60

def conversor_h_s(valor):
    return valor * 3600

def conversor_m_h(valor):
    return valor / 60

def conversor_m_s(valor):
    return valor * 60

def conversor_s_h(valor):
    return valor / 3600

def conversor_s_m(valor):
    return valor / 60
# Conversor de Distância
def conversor_mi_m(valor):
    return valor * 1609.34

def conversor_mi_yd(valor):
    return valor * 1760

def conversor_m_mi(valor):
    return valor / 1609.34

def conversor_m_yd(valor):
    return valor * 1.09361

def conversor_yd_mi(valor):
    return valor / 1760

def conversor_yd_m(valor):
    return valor / 1.09361
def conversor_in_m(valor):
    return valor * 0.0254

def conversor_m_in(valor):
    return valor / 0.0254

def conversor_in_yd(valor):
    return valor / 36

def conversor_yd_in(valor):
    return valor * 36

def conversor_in_mi(valor):
    return valor / 63360

def conversor_mi_in(valor):
    return valor * 63360


# Conversor de Peso
def conversor_kg_lb(valor):
    return valor * 2.20462

def conversor_lb_kg(valor):
    return valor * 0.453592



grandeza=str(input('Qual a grandeza a ser medida? (peso, temperatura, tempo, distância) ')) 
unidade=str
if grandeza=="temperatura"or grandeza=="temperature":
##tempeatura


    unidade=input('Qual unidade unidade de medida?(celsius,kelvin,farenheint)')
    valor=float(input('Qual a temperatura?'))
    farenheint=float
    celsius=float
    kelvin=float
    if unidade=="celsius"or unidade=="c":
        farenheint=conversor_c_f(valor)
        kelvin=conversor_c_k(valor)
        print(f"{farenheint}º F e " f"{kelvin}ºK.")
    if unidade=="f"or unidade=="farenheint":
        celsius=conversor_f_c (valor)
        kelvin=conversor_f_k(valor)
        print(f"{celsius}º C e " f"{kelvin}ºK.")
    if unidade=="k" or unidade=="kelvin":
        celsius=conversor_k_c(valor)
        farenheint=conversor_k_f(valor)
        print(f"{celsius}ºC e " f"{farenheint}ºF.")


#tempo
elif grandeza=="tempo"or grandeza=="time":
    unidade= input('Escolha a unidade de tempo: (horas, minutos, segundos) ')  
    valor = float(input(f'Qual o valor em {unidade}? ')) 
    if unidade == "horas" or unidade == "h":
        minutos = conversor_h_m(valor)
        segundos = conversor_h_s(valor)
        print(f"{valor} horas é igual a {minutos:.2f} minutos e {segundos:.2f} segundos.")
    elif unidade == "minutos" or unidade == "m":
        horas = conversor_m_h(valor)
        segundos = conversor_m_s(valor)
        print(f"{valor} minutos é igual a {horas:.2f} horas e {segundos:.2f} segundos.")
    elif unidade == "segundos" or unidade == "s":
        horas = conversor_s_h(valor)
        minutos = conversor_s_m(valor)
        print(f"{valor} segundos é igual a {horas:.2f} horas e {minutos:.2f} minutos.")
    else:
        print("Unidade de tempo não reconhecida.")
##distancia
        '''elif grandeza== "distancia":
    unidade = input('Escolha a unidade de distância: (milhas, metros, jardas) ')
    valor = float(input(f'Qual o valor em {unidade}? '))

    if unidade == "milhas" or unidade == "mi":
        metros = conversor_mi_m(valor)
        jardas = conversor_mi_yd(valor)
        print(f"{valor} milhas é igual a {metros:.2f} metros e {jardas:.2f} jardas.")
    elif unidade == "metros" or unidade == "m":
        milhas = conversor_m_mi(valor)
        jardas = conversor_m_yd(valor)
        print(f"{valor} metros é igual a {milhas:.2f} milhas e {jardas:.2f} jardas.")
    elif unidade == "jardas" or unidade == "yd":
        milhas = conversor_yd_mi(valor)
        metros = conversor_yd_m(valor)
        print(f"{valor} jardas é igual a {milhas:.2f} milhas e {metros:.2f} metros.")'''
elif grandeza == "distancia":
    unidade = input('Escolha a unidade de distância: (milhas, metros, jardas, polegadas) ').lower()
    valor = float(input(f'Qual o valor em {unidade}? '))
    if unidade == "milhas" or unidade == "mi":
        metros = conversor_mi_m(valor)
        jardas = conversor_mi_yd(valor)
        polegadas = conversor_mi_in(valor)
        print(f"{valor} milhas é igual a {metros:.2f} metros, {jardas:.2f} jardas e {polegadas:.2f} polegadas.")
    elif unidade == "metros" or unidade == "m":
        milhas = conversor_m_mi(valor)
        jardas = conversor_m_yd(valor)
        polegadas = conversor_m_in(valor)
        print(f"{valor} metros é igual a {milhas:.2f} milhas, {jardas:.2f} jardas e {polegadas:.2f} polegadas.")
    elif unidade == "jardas" or unidade == "yd":
        milhas = conversor_yd_mi(valor)
        metros = conversor_yd_m(valor)
        polegadas = conversor_yd_in(valor)
        print(f"{valor} jardas é igual a {milhas:.2f} milhas, {metros:.2f} metros e {polegadas:.2f} polegadas.")
    elif unidade == "polegadas" or unidade == "inches" or unidade == "in":
        metros = conversor_in_m(valor)
        jardas = conversor_in_yd(valor)
        milhas = conversor_in_mi(valor)
        print(f"{valor} polegadas é igual a {metros:.2f} metros, {jardas:.2f} jardas e {milhas:.2f} milhas.")
    else:
        print("Unidade de distância não reconhecida.")
    
        
#peso
elif grandeza == "peso":
    unidade = input('Escolha a unidade de peso: (quilogramas, libras) ')
    valor = float(input(f'Qual o valor em {unidade}? '))

    if unidade == "quilogramas" or unidade == "kg":
        libras = conversor_kg_lb(valor)
        print(f"{valor} kg é igual a {libras:.2f} libras.")
    elif unidade == "libras" or unidade == "lb":
        quilogramas = conversor_lb_kg(valor)
        print(f"{valor} libras é igual a {quilogramas:.2f} kg.")
    else:
        print("Unidade de peso não reconhecida.")
else:
    print("grandeza não conhecida")