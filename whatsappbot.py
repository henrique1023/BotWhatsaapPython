from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import random
import time

chrome_options = Options()
chrome_options.add_argument("user-data-dir=C:/Users/Henrique A/AppData/Local/Google/Chrome/User Data")
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
driver.get("https://web.whatsapp.com/")

time.sleep(60)  
result = 0

contatos = [
]

mensagem = ['''Olá, tudo bem?Sou a *Raquel* da *Cond Climatização*, uma empresa que é referência na climatização de ambientes. Com tecnicos especializados na area. Esse mes estamos com super ofertas em alguns de nossos serviços para ares condicionados:
    • *Higienização de aparelhos SPLIT, K7, PISO TETO, JANELAS, entre outros.*
    • *Instalação de todos os tipos de aparelhos.*
    • *Manutenção geral com diagnósticos.*
    Ao final do serviço, a *Cond Climatização* pode oferecer Nota Fiscal e Laudo para *ANVISA*, a pedido do cliente.
    *Trabalhamos também com reforma elétrica e manutenção da rede residencial.*
    *FAÇA JÁ SEU ORÇAMENTO! NÃO PERCA ESSA OPORTUNIDADE*
    *Email: condrefrigeracao@gmail.com*
    *CASO NÃO QUEIRA MAIS RECEBER ESSA MENSAGEM, POR FAVOR ENVIE NÃO*''']

def anti_block():
    ref = random.randrange(1,20)
    if ref%3 == 0:
        r = random.randrange(1,15)
        f = round(r,0)
        time.sleep(f)
    else:
        time.sleep(5)
    
def enviar_mensagem(mensagem):
    campo_mensagem = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    campo_mensagem.click()
    time.sleep(2)
    campo_mensagem.send_keys(mensagem)
    campo_mensagem.send_keys(Keys.ENTER)  
    time.sleep(2)

def abrir_web(con):
    result = 0
    try:
        driver.get(con)
        time.sleep(15)
        enviar_mensagem(mensagem[0])
        time.sleep(4)
    except:
        result += 1
        return result 

for contato in contatos:
    cont = "https://web.whatsapp.com/send?phone=+55"+ str(contato)
    abrir_web(cont)
    result = result + 1
    anti_block()

print(result)

driver.close()
driver.quit()

