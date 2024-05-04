from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
url = 'http://localhost:3000'
driver.get(url)
time.sleep(2)

def test_register():
    btn_login = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div[3]/a/button')
    btn_login.click()
    time.sleep(2)
    btn_view_user = driver.find_element(By.XPATH, '//*[@id="root"]/div/nav/div/div/ul/li[1]/a/a')
    btn_view_user.click()
    btn_new_user = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/div[2]/div[1]/a')
    btn_new_user.click()
    nombre1 = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/div[2]/div[2]/div/div/div[2]/div/form/div[1]/div[1]/div/input')
    nombre1.send_keys('Juan')
    nombre2 = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/div[2]/div[2]/div/div/div[2]/div/form/div[1]/div[2]/div/input')
    nombre2.send_keys('Perez')
    apellido1 = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/div[2]/div[2]/div/div/div[2]/div/form/div[2]/div[1]/div/input')
    apellido1.send_keys('Gomez')
    apellido2 = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/div[2]/div[2]/div/div/div[2]/div/form/div[2]/div[2]/div/input')
    apellido2.send_keys('Lopez')
    usuario = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/div[2]/div[2]/div/div/div[2]/div/form/div[3]/div[1]/div/input')
    usuario.send_keys('juanperez')
    password = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/div[2]/div[2]/div/div/div[2]/div/form/div[3]/div[2]/div/input')
    password.send_keys('123456')
    time.sleep(2)
    btn_guardar = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/div[2]/div[2]/div/div/div[2]/div/form/div[4]/button')
    btn_guardar.click()
    time.sleep(2)
    assert driver.current_url == url + '/usuarios'
    
    