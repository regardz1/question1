from selenium import webdriver
from webdriver
import time

driver1 = "D:\Python Selenium\chromedriver_win32\chromedriver.exe"
driver2 = webdriver.Chrome(driver1)
driver2.maximize_window()
driver2.get("https://www.cermati.com/app/gabung")

time.sleep(10)
driver2.find_elements_by_xpath('//*[(text() = "Daftar Akun" or . = "Daftar Akun")]')

driver2.find_element_by_id('email').send_keys("test@gmail.com")
time.sleep(2)
driver2.find_element_by_id('mobilePhone').send_keys("081234567890")
time.sleep(2)
driver2.find_element_by_id('password').send_keys("Testing123")
time.sleep(2)
driver2.find_element_by_id('confirmPassword').send_keys("Testing123")
time.sleep(2)
driver2.find_element_by_id('firstName').send_keys("Tester")
time.sleep(2)
driver2.find_element_by_id('lastName').send_keys("Manual")
time.sleep(2)
driver2.find_element_by_id('cityAndProvince').send_keys("Sumut")
time.sleep(2)
toba = driver2.find_elements_by_xpath('//*[(text() = "KABUPATEN TOBA SAMOSIR" or . = "KABUPATEN TOBA SAMOSIR")]')
driver2.find_element_by_xpath(toba).click()
driver2.find_element_by_id("//*[@type='button']").click()
time.sleep(10)
driver2.close()
