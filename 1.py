# implementar:
# verificar elementos carregarem em vez de time.sleep
# verificar o tipo de página na antaq(inexistente, alterável e protocolado)
# for para fazer múltiplos valores, esperar depois que o protocolo for enviado
# bypass captcha

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import Select

import time

imolist = [
    "9725471",
    "9651101",
    "9442469",
    "9311177",
    "9460760",
    "9573634",
    "9576961",
    "9285146",
    "9935466",
    "9900095",
    "9705354",
    "9289025",
    "9713935",
    "9193317",
    "9374351",
    "9457878",
    "9569243",
    "9675274",
    "9467249",
    "9425186",
    "9494486",
    "9491587",
    "9442392",
    "9649299",
    "9642215",
    "9679799",
    "9600607",
    "9604847",
    "9887619",
    "9734185",
    "9298533",
    "9717060",
    "9646663",
    "9300556",
    "9705299",
    "9139268"
]

email = 'dcampos@brssz.com'

keyword3 = input("enter a character or press enter to continue")

for imo in imolist:
    servico = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=servico)

    # entra no site e aguarda carregar
    driver.get("https://www.marinetraffic.com/en/global-search/")

    # espera até aviso aparecer para continuar e aceita os cookies
    element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="qc-cmp2-ui"]/div[2]/div/button[2]')))
    driver.find_element('xpath', '//*[@id="qc-cmp2-ui"]/div[2]/div/button[2]').click()

    # digita IMO e pesquisa
    driver.find_element('xpath', "//div[@id='app']/div/div[3]/div[2]/header/div/div/div/div[2]/div/div/input").send_keys(imo)
    driver.find_element('xpath', "//div[@id='app']/div/div[3]/div[2]/header/div/div/div/div[2]/div/div/input").send_keys(Keys.RETURN)

    # clica no primeiro resultado
    element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//div[@id='app']/div/div[3]/div[2]/div/div/a/div/div[3]/div/h5/span/span")))
    driver.find_element('xpath',"//div[@id='app']/div/div[3]/div[2]/div/div/a/div/div[3]/div/h5/span/span").click()
    time.sleep(2)

    # scroll até a área onde os dados estão localizados
    driver.execute_script("scroll(0, 1600)")
    element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="General-content"]/div')))

    time.sleep(4)
    # coleta dos dados
    #element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="shipName"]/b')))
    nome = driver.find_element('xpath', '//*[@id="shipName"]/b').text

    callSign = driver.find_element('xpath', '//*[@id="callSign"]/b').text
    bandeira = driver.find_element('xpath', '//*[@id="flag"]/b').text
    tipo = driver.find_element('xpath', '//*[@id="shipTypeSpecific"]/b').text
    ano = driver.find_element('xpath', '//*[@id="yearBuilt"]/b').text
    arqueacao = driver.find_element('xpath', '//*[@id="grossTonnage"]/b').text
    dwt = driver.find_element('xpath', '//*[@id="summerDwt"]/b').text

    # tratamento dos dados
    bandeira = bandeira[-3] + bandeira[-2] # pegando apenas a sigla da bandeira
    arqueacao += '00'
    dwt = dwt.replace(' t', '')
    dwt += '00'

    # separando cada caractere das strings arqueacao e dwt devido a um bug no formulário da ANTAQ
    arqueacao = (" ".join(arqueacao))
    dwt = (" ".join(dwt))

    print(nome, callSign, bandeira, tipo, ano, arqueacao, dwt)



    # SITE ANTAQ

    # entra no site da antaq e preenche imo
    driver.get("https://web3.antaq.gov.br/SAMA/Embarcacao/Consultar.aspx")
    driver.find_element('xpath', '//*[@id="txtIMO"]').send_keys(imo)
    driver.find_element('xpath', '//*[@id="txtIMO"]').send_keys(Keys.RETURN)

    # verifica se o popup de navio já cadastrado aparece
    if (len(driver.find_elements('xpath', '//*[@id="msgCadastrar"]'))):
        driver.find_element('xpath', '//*[@id="btnCadastrarSim"]').click()

    time.sleep(1)
        
    # preenchimento de dados
    driver.find_element('xpath', '//*[@id="txtNome"]').send_keys(nome)
    driver.find_element('xpath', '//*[@id="txtIRIN"]').send_keys(callSign)
    driver.find_element('xpath', '//*[@id="ddlBandeira"]').click()
    select = Select(driver.find_element('xpath','//*[@id="ddlBandeira"]')).select_by_value(bandeira)

    # verifica o tipo de navio e carga
    driver.find_element('xpath', '//*[@id="ddlTipoEmbarcacao"]').click()
    if (tipo == 'Bulk Carrier'):
        driver.find_element('xpath', '//*[@id="ddlTipoEmbarcacao"]/option[19]').click()
        driver.find_element('xpath', '//*[@id="vncTipoCarga"]/select[1]/option[9]').click()
        driver.find_element('xpath', '//*[@id="vncTipoCarga"]/div/input[3]').click()
    elif (tipo == 'General Cargo'):
        driver.find_element('xpath', '//*[@id="ddlTipoEmbarcacao"]/option[10]').click()
        driver.find_element('xpath', '//*[@id="vncTipoCarga"]/select[1]/option[4]').click()
        driver.find_element('xpath', '//*[@id="vncTipoCarga"]/div/input[3]').click()
    elif (tipo == 'Tanker'):
        driver.find_element('xpath', '//*[@id="ddlTipoEmbarcacao"]/option[19]').click()
        time.sleep(1)
        driver.find_element('xpath', '//*[@id="ddlClasse"]/option[2]').click()
        driver.find_element('xpath', '//*[@id="vncTipoCarga"]/select[1]/option[11]').click()
        driver.find_element('xpath', '//*[@id="vncTipoCarga"]/div/input[3]').click()
    elif (tipo == 'Oil Tanker' or tipo == 'Crude Oil Tanker'):
        driver.find_element('xpath', '//*[@id="ddlTipoEmbarcacao"]/option[31]').click()
        # opção de petróleo não aparecendo
        driver.find_element('xpath', '//*[@id="vncTipoCarga"]/div/input[3]').click()
    elif (tipo == 'Passenger Ship'):
        driver.find_element('xpath', '//*[@id="ddlTipoEmbarcacao"]/option[28]').click() # marcado como opção passageiros, confirmar depois
        driver.find_element('xpath', '//*[@id="vncTipoCarga"]/select[1]/option[15]').click()
        driver.find_element('xpath', '//*[@id="vncTipoCarga"]/div/input[3]').click()


    # preenchendo dados de ano, arqueação e dwt
    driver.find_element('xpath', '//*[@id="txtAno"]').send_keys(ano)
    driver.find_element('xpath', '//*[@id="txtArqueacao"]').send_keys(arqueacao)
    driver.find_element('xpath', '//*[@id="txtTPB"]').send_keys(dwt)

    # selecionando checkbox de cabotagem e longo curso
    driver.find_element('xpath', '//*[@id="chkCabotagem"]').click()
    time.sleep(2)
    driver.find_element('xpath', '//*[@id="chkLongoCurso"]').click()

    # inserindo email
    driver.find_element('xpath', '//*[@id="txtEmail"]').send_keys(email)
    driver.find_element('xpath', '//*[@id="txtConfirmarEmail"]').send_keys(email)

    driver.find_element('xpath', '//*[@id="rdbSDP"]').click()



    keyword = input("enter a character or press enter to continue")

