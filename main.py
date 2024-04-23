from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException

URL = "https://www.linkedin.com/jobs/search/?currentJobId=3904508013&f_AL=true&keywords=junior%20software%20developer&origin=JOB_SEARCH_PAGE_JOB_FILTER"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)


def load_url():
    driver.get(URL)
    try:
        sign_in_button = driver.find_element(by=By.LINK_TEXT, value="Sign in")
        sign_in_button.click()
        time.sleep(2)
        email = driver.find_element(by=By.CSS_SELECTOR, value="#username")
        email.send_keys(USERNAME)
        password = driver.find_element(by=By.CSS_SELECTOR, value="#password")
        password.send_keys(PASSWORD)
        enter_button = driver.find_element(By.CLASS_NAME, "btn__primary--large")
        enter_button.click()
        time.sleep(2)
    except NoSuchElementException:
        load_url()


load_url()

all_jobs = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")

for job in all_jobs:
    job.click()
    time.sleep(3)
    apply_button = driver.find_element(by=By.CLASS_NAME, value="jobs-apply-button")
    apply_button.click()
    try:
        submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button[aria-label='Submit Application']")
        submit_button.click()
        close_button_success = driver.find_element(by=By.CSS_SELECTOR, value="button[aria-label='Dismiss']")
        close_button_success.click()
    except NoSuchElementException:
        exit_button = driver.find_element(by=By.CSS_SELECTOR, value="button[aria-label='Dismiss']")
        exit_button.click()
        time.sleep(1)
        discard_button = driver.find_element(By.CSS_SELECTOR, value=".artdeco-modal__confirm-dialog-btn")
        discard_button.click()





