srtIcon = '''
  _      _______      ________    _____         ______ ______   ____   ____ _______ 
 | |    |_   _\ \    / /  ____|  / ____|  /\   |  ____|  ____| |  _ \ / __ \__   __|
 | |      | |  \ \  / /| |__    | (___   /  \  | |__  | |__    | |_) | |  | | | |   
 | |      | |   \ \/ / |  __|    \___ \ / /\ \ |  __| |  __|   |  _ <| |  | | | |   
 | |____ _| |_   \  /  | |____   ____) / ____ \| |    | |____  | |_) | |__| | | |   
 |______|_____|   \/   |______| |_____/_/    \_\_|    |______| |____/ \____/  |_|                                                                                                                                                                       
'''
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

print(srtIcon + "\n\n By Jake R")

# Chrome Window Setup
driver = webdriver.Chrome('./chromedriver')
driver.get("https://livesafe.jotform.com/202527480965966")
driver.maximize_window()

start_time = time.time()

time.sleep(2)

# School Selector
dropDown = driver.find_element_by_xpath("/html/body/form/div/ul/li[2]/div/select")
dropDown.click()

schoolSelc = driver.find_element_by_xpath("/html/body/form/div/ul/li[2]/div/select/option[3]")
schoolSelc.click()

nextBtn = driver.find_element_by_xpath("/html/body/form/div/ul/li[3]/div/div/button")
nextBtn.click()

# ID Selector
engBtn = driver.find_element_by_xpath("/html/body/form/div/ul/li[3]/div/div/span[1]/input")
engBtn.click()

fstName = driver.find_element_by_xpath("/html/body/form/div/ul/li[7]/div/input")
fstName.send_keys("FIRST")  # ADD FIRST NAME HERE

lstName = driver.find_element_by_xpath("/html/body/form/div/ul/li[8]/div/input")
lstName.send_keys("LAST")  # ADD LAST NAME HERE

email = driver.find_element_by_xpath("/html/body/form/div/ul/li[10]/div/input")
email.send_keys("EMAIL@stu.smuhsd.org")  # ADD EMAIL HERE

areaCode = driver.find_element_by_xpath("/html/body/form/div/ul/li[11]/div/div[1]/span[1]/input")
areaCode.send_keys("111")  # ADD FIRST 3 DIGITS OF PHONE NUMBER HERE

phoneNum = driver.find_element_by_xpath("/html/body/form/div/ul/li[11]/div/div[1]/span[2]/input")
phoneNum.send_keys("1111111")  # ADD LAST 7 DIGITS OF PHONE NUMBER HERE

studentBtn = driver.find_element_by_xpath("/html/body/form/div/ul/li[12]/div/div/span[1]/input")
studentBtn.click()

studID = driver.find_element_by_xpath("/html/body/form/div/ul/li[14]/div/input")
studID.send_keys("1111111")  # ADD STUDENT ID HERE

# Covid Questions
q1 = driver.find_element_by_xpath("/html/body/form/div/ul/li[21]/div/div/span[2]/input")
q1.click()

q2 = driver.find_element_by_xpath("/html/body/form/div/ul/li[24]/div/div/span[2]/input")
q2.click()

q3 = driver.find_element_by_xpath("/html/body/form/div/ul/li[27]/div/div/span[3]/input")
q3.click()

q4 = driver.find_element_by_xpath("/html/body/form/div/ul/li[31]/div/div/span[2]/input")
q4.click()

# Submit
submit = driver.find_element_by_xpath("/html/body/form/div/ul/li[42]/div/div/button")
submit.click()

end_time = time.time()
elapsed = end_time - start_time

print("\nYour LIVESAFE application was succesfuly submited in " + str(elapsed) + " seconds\n")

print("Closing in 5 seconds")

time.sleep(1)

driver.close()

time.sleep(5)

driver.quit()
