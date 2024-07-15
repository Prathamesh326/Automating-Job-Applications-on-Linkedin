from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)
driver.get(
    "https://www.linkedin.com/jobs/search/?currentJobId=3963431831&f_LF=f_AL&geoId=106164952&keywords=python%20developer&location=Mumbai%2C%20Maharashtra%2C%20India&origin=JOB_SEARCH_PAGE_LOCATION_AUTOCOMPLETE&refresh=true")

#  Automatically Login
driver.find_element(By.CSS_SELECTOR, ".nav__button-secondary.btn-md.btn-secondary-emphasis").click()
# time.sleep(2)
username = driver.find_element(By.ID, "username")
username.send_keys("")       #----------------------------------------enter your own email-----------------------------------------------

password = driver.find_element(By.ID, "password")
password.send_keys("")         #----------------------------------------enter your own password-----------------------------------------------

driver.find_element(By.CSS_SELECTOR, ".btn__primary--large.from__button--floating").click()

# save jobs
driver.find_element(By.XPATH,
                    '//*[@id="main"]/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div[1]/div[5]/div/button').click()
