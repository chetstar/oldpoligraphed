"""Selenium Test 
Tests input field and submits to list.
"""

from selenium import webdriver
import selenium.webdriver.support.ui as ui
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()

driver.get("http://127.0.0.1:5000/")

#title = driver.find_element_by_xpath("html/body/div[2]/div/div[1]/h1") == "Noiselist"):
input_element = driver.find_element_by_xpath(".//*[@id='add_to_todo_list']/input[1]")
input_element.send_keys("cheese!")
WebDriverWait(driver, 10)

# submit the form (although google automatically searches now without submitting)
input_element.submit()

#try:
#    WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element("html/body/div[2]/div/div[2]/div[1]/ul", "cheese!"))
#    print driver.title

#finally:
#   driver.quit()