from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

service = Service(executable_path=ChromeDriverManager().install())

driver = webdriver.Chrome(service=service)
title = driver.title
driver.implicitly_wait(0.5)