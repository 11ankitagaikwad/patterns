import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(2)
driver.get("https://www.amazon.in/")

def selClick(strXpath,inte):
    element = WebDriverWait(driver, inte).until(EC.presence_of_element_located((By.XPATH,strXpath)))
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    element.click()

driver.find_element(By.XPATH,"//input[@id='twotabsearchtextbox']").send_keys("shirt")
selClick("//input[@id='nav-search-submit-button']",1)
selClick("//div[@role='listitem'][8]",5)
selClick("//span[@id='size_name_2']",10)
selClick("//input[@title='Add to Shopping Cart']",10)
selClick("//a[@data-csa-c-content-id='sw-gtc_CONTENT']",10)
selClick("//input[@value='Delete']",10)


element=WebDriverWait(driver,inte).until(Ec.presence_of_element_located(By.XPATH,))
















"""
driver.find_element(By.XPATH,"//input[@id='twotabsearchtextbox']").send_keys("shirt")
driver.find_element(By.XPATH,"//input[@id='nav-search-submit-button']").click()
#scroll=driver.find_element(By.XPATH,"//div[@role='listitem'][8]")
#driver.execute_script("arguments[0].scrollIntoView(true);",scroll)
driver.find_element(By.XPATH,"//div[@role='listitem'][8]").click()
driver.find_element(By.XPATH,"//span[@id='size_name_2']").click()
#addCart=driver.find_element(By.CSS_SELECTOR,"input[title='Add to Shopping Cart']")
#driver.execute_script("arguments[0].scrollIntoVeiw(true);",addCart)
#time.sleep(2)
driver.find_element(By.CSS_SELECTOR,"input[title='Add to Shopping Cart']").click()

driver.find_element(By.XPATH,"//a[@data-csa-c-content-id='sw-gtc_CONTENT']").click()

#//div[@aria-labelledby="dim-values-aria-label-size_name"]//span[contains(text(),'M')]
driver.find_element(By.XPATH,"//input[@value='Delete']").click()
"""

