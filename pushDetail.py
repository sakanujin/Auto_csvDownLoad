from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



import time

# set information
your_username = "p0007@kannetsu.co.jp"
your_password = "vI7QOM7c"
target_url = "https://pushlog.jp/"

# chrome start runnning 

driver = webdriver.Chrome()
driver.get(target_url)

try:
    wait = WebDriverWait(driver, 10)
    username_field = wait.until(EC.presence_of_element_located((By.ID, "signInName")))
    #print("find signInName")
    username_field.send_keys(your_username)
    time.sleep(2)

    password_field = wait.until(EC.presence_of_element_located((By.ID, "password")))
    password_field.send_keys(your_password)
    time.sleep(4)

    enter_field = wait.until(EC.presence_of_element_located((By.ID, "next")))
    enter_field.click()

    wait = WebDriverWait(driver, 10)
    agree_button = wait.until(EC.element_to_be_clickable((By.XPATH,'//span[@class="v-btn__content" and text()="同意して利用を開始する"]')))
    agree_button.click()
    time.sleep(8)
###################################################  sofar ok  ##########################

    link_elements = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "詳細へ")]')))
    link_url = link_elements.get_attribute("href")
    #print ("link url : ", link_url)
    driver.get(link_url)


    #driver.execute_script("arguments[0].click();", link_elements)
    print("link_elements is clicked", link_elements)
    wait = WebDriverWait(driver, 10)
    agree_button = wait.until(EC.element_to_be_clickable((By.XPATH,'//span[@class="v-btn__content" and text()="同意して利用を開始する"]')))
    agree_button.click()
    time.sleep(18)

###################################################  sofar ok  ##########################

    download_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(., 'CSVダウンロード')]")))
    download_button.click()
    time.sleep(18)




except Exception as e:
    print("cannot find")
    print("Error Occur :", e)

finally:
    driver.quit()
