from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

def login_to_website(email, password, url):
    path = "C:\\Users\\ABC\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"
    service = Service(path)
    driver = webdriver.Chrome(service=service)

    driver.get(url)

    # Adjust these according to the actual page structure
    driver.find_element(By.NAME, "username").send_keys(email)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# credentials
email = "25f1002558@ds.study.iitm.ac.in"
password = "your_password_here"  # Replace with your actual password

url = "https://code.iitm.ac.in/code-programs/VIDYA/"

# function call
login_to_website(email, password, url)
