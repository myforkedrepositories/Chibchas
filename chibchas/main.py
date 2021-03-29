import time
import pandas as pd

import helium as h
from selenium.common.exceptions import NoSuchElementException

# login
browser = h.start_firefox('https://scienti.minciencias.gov.co/institulac2-war/')
sleep=0.8
    #browser = h.start_firefox('https://scienti.minciencias.gov.co/institulac2-war/')
time.sleep(sleep)
h.click('Consulte Aquí')

time.sleep(sleep)
h.write('UNIVERSIDAD DE ANTIOQUIA',into='Digite el nombre de la Institución')

time.sleep(sleep)
h.click('Buscar')

time.sleep(sleep)
h.click(browser.find_element_by_id('list_instituciones'))

time.sleep(sleep)

time.sleep(sleep)
h.select('seleccione una','UNIVERSIDAD DE ANTIOQUIA')

time.sleep(sleep)
h.write('annyarango',into='Usuario')

time.sleep(sleep)
h.write('1@Silver',into='Contraseña')

time.sleep(sleep)
h.click(h.Button('Ingresar'))

# navigation 1
time.sleep(sleep)
h.click('Aval')

time.sleep(sleep)
h.click('Avalar grupos')

time.sleep(sleep)
h.click('Grupos Avalados')

# -- end login --

# catch 1 schema
# empty df
# select max items per page
# while until end
# try:
    # catch table
    # preproces table
    # catch urls
    # add url colums
    # add df
    # click next page -> raise error
# except Nosuchelement:
    # break

    
# catch 1 implementation

dfg=pd.DataFrame()

time.sleep(sleep)
h.click(browser.find_element_by_xpath('//table[@id="grupos_avalados"]//select[@name="maxRows"]'))

time.sleep(sleep)
h.select(browser.find_element_by_xpath('//table[@id="grupos_avalados"]//select[@name="maxRows"]'),'100')

cont=True
while cont:
    
    try:
        # catch source
        time.sleep(sleep)
        source_g=browser.page_source
        
        # catch table
        time.sleep(sleep)
        df=pd.read_html(source_g, attrs={"id":"grupos_avalados"}, header=2)[0]
        
        # and preprocces it
        c=[x for x in df.columns if x.find('Unnamed:') == -1]
        dfgp=df[c][1:-1]
        print(dfgp.columns,dfgp.shape)
        
        # catch urls
        url=[a.get_attribute('href') for a in browser.find_elements_by_xpath('//table[@id="grupos_avalados"]//td[5]/a')]
        dfgp['Revisar'] = url
        dfg=dfg.append(dfgp)
        
        # click next page. this instruction rise error of the end. 
        h.click(browser.find_element_by_xpath('//table[@id="grupos_avalados"]//tr/td[3]/a'))
        
    except NoSuchElementException as e:
        print(e)
        print('out of cicle')
        break
        
    time.sleep(sleep)
    time.sleep(sleep)
    
assert dfg.shape[0] == 324
# -- end catch one --
