from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://demoqa.com/radio-button")

radioButtonEnabled=driver.find_element(by=By.ID, value="noRadio")

assert radioButtonEnabled.is_enabled()==False

print(radioButtonEnabled.is_enabled())



radioButtonImpressive=driver.find_element(by=By.XPATH, value="//label[@for='impressiveRadio']")
radioButtonImpressive.click()

rtaLabel=driver.find_element(by=By.XPATH, value="//p[@class='mt-3']//span[@class='text-success']")

print(radioButtonImpressive.text)
assert radioButtonImpressive.text==rtaLabel.text

radioButtonYes=driver.find_element(by=By.XPATH, value="//label[@for='yesRadio']")

radioButtonYes.click()

print(radioButtonYes.text)
assert radioButtonYes.text==rtaLabel.text





