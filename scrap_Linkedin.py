from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()

driver.implicitly_wait(10)

driver.get('https://br.linkedin.com/jobs/cientista-de-dados-vagas?position=1&pageNum=0')

resultados = driver.find_elements_by_class_name('result-card')

lista_descricao=[]
while True:
    for r in resultados[len(lista_descricao):]:
        r.click()
        sleep(1)
        try:
            descricao = driver.find_element_by_class_name('description')
            lista_descricao.append(descricao.text)
        except:
            pass
    resultados = driver.find_elements_by_class_name('result-card')         

    if len(lista_descricao) == len(resultados):
        break

descricao_salvar = '\n'.join(lista_descricao)
with open('descricoes_vagas.txt', 'w',encoding='utf-8') as f:
    f.write(descricao_salvar)

driver.quit()