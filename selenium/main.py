import random
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome()
# driver.implicitly_wait(20)  # da una espera implícita de 20 segundos

driver.get("https://www.google.com")

# driver = webdriver.Chrome('chromedriver.exe')
# options = webdriver.ChromeOptions()
# options.add_argument('--headless')
# driver = webdriver.Chrome(executable_path=r'chromedriver.exe')


###    coneccion selenium 4    ###
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
###    coneccion selenium 4    ###


driver.get('http://www.pehuajo.gob.ar/')

# titulos = driver.find_elements(By.XPATH, '//h2[@class="post-title entry-title"]')
# for titulo in titulos:
#     titular = titulo.text
#     print(titular)  # imprime titular

# paginaActual = int(driver.find_element(By.XPATH, '//span[@class="showpagePoint"]').text)  # pagina actual en int
# paginaSiguiente = 2

for i in range(0, 5):

    # botones = driver.find_elements_by_xpath(' //span[@class="showpageNum"]')  ####

    #### imprimir titulares de la pagina #### inicio
    driver.get('http://www.pehuajo.gob.ar/')
    titulos = driver.find_elements(By.XPATH, '//h2[@class="post-title entry-title"]')
    for titulo in titulos:
        titular = titulo.text
        print(titular)  # imprime titular
    #### imprimir titulares de la pagina #### FIN

    paginaActual = int(driver.find_element(By.XPATH, '//span[@class="showpagePoint"]').text)  # pagina actual en int
    paginaSiguiente = paginaActual + 1
    print("""
        pagina actual: %d
        pagina siguiente:%d
        """ % (paginaActual, paginaSiguiente))

    botones = driver.find_elements(By.XPATH, '//span[@class="showpageNum"]')  # saco los botones
    for j in botones:
        # val = int(j.text)
        val = 0
        val = int(j.text)
        print("el valor de val es %d" % val)
        print("el valor de paginaSiguiente es %d" % paginaSiguiente)
        if int(j.text) == paginaSiguiente:
            direccion = '//a[@onclick="redirectpage(%s)"]' % paginaSiguiente
            # paginaSiguiente += 1
            try:
                boton = driver.find_element(By.XPATH, direccion)
                boton.click()
                sleep(random.uniform(125.0, 158.0))
            except:
                break
        else:
            pass
