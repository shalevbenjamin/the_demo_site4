from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions

def driver_setup():
    options = ChromeOptions()
    service = ChromeService(ChromeDriverManager().install())
    options.add_experimental_option('detach', True)
    options.add_argument('--start-maximized')
    options.add_argument('--disable-extentions')
    driver = webdriver.Chrome(service=service, options=options)
    return driver

if _name_ == '_main_':
    my_driver = driver_setup()
    my_driver.get('https://thedemosite.co.uk/')