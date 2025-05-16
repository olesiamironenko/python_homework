from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
import re
import csv
import json

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Task 6.2: Read this page: [https://owasp.org/www-project-top-ten/]
url = 'https://owasp.org/www-project-top-ten/'
driver.get(url)

WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.TAG_NAME, 'body'))
)

list = []
dict = {}

# Task 6.3: Find each of the top 10 vulnerabilities
def scraping():
    h2 = driver.find_element(By.CSS_SELECTOR,'#top-10-web-application-security-risks') # Find all the links on the page.
    # print(h2.text)
    if h2:
        ul = h2.find_element(By.XPATH,'following-sibling::ul' )
        if ul:
            # print(f'A list is found bellow "Top 10 Web Application Security Risks" title')
            lis = ul.find_elements(By.XPATH, 'li')
            # print(f'{len(lis)} list items found')
            for li in lis:
                title = li.find_element(By.TAG_NAME, 'strong').text
                # print(title)
                link = li.find_element(By.TAG_NAME, 'a').get_attribute('href')
                # print(link)

                # Tassk 6.3: Keep the vulnerability title and the href link in a dict
                dict["Title"] = title
                dict["Link"] = link

                # Task 6.4: Print out the list to make sure you have the right data
                list.append(dict)
            
scraping()
print(list)

# Task 6.4: Write the list to a file called owasp_top_10.csv.
with open('owasp_top_10.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = list[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(list)

# title 
# href link