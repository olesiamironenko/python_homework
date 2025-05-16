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

#  Task 3.2: Add code to load the web page given in task 2
url = 'https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart'

driver.get(url)

# Task 3.4: Within your program, create an empty list called results
results = []

# Set page numbers for pagination handling
# page_number = 1
# last_scraped_page = 0
total_pages_scraped = 0
total_items_scraped = 0

while True:
    # Wait for search results to load
    WebDriverWait(driver, 30).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.results_container'))
    )

    # Getting current page number
    current_page_list_item = driver.find_element(By.CSS_SELECTOR, 'li.pagination-item--current')
    if current_page_list_item:
        current_page_text = current_page_list_item.find_element(By.CSS_SELECTOR, 'span.cp-screen-reader-message').text
        print(current_page_text)
        current_page_match = re.match(r'^\w*\s*(\d*)\,', current_page_text)
        if current_page_match:
            print("True")
            current_page = current_page_match.group(1)
        else:
            print("False")
    print(f"Current page: {current_page}")

    # Task 3.3: Find all the li elements in the current page of the search results
    list_items = driver.find_elements(By.CSS_SELECTOR,'li.cp-search-result-item') # Find all the list items on the page.
    print(f"Found {len(list_items)} items on page {current_page}")

    # Task 3.5: Main loop: iterate through the list of li entries
    for item in list_items:
        try:
            # Task 2.4 / 3.5: find the element that stores the title
            title = item.find_element(By.CSS_SELECTOR,'span.title-content')
            if title:
                title = title.text.strip()
            else:
                title = "No title"
            print(title)
        except StaleElementReferenceException:
            print("❗ STALE ELEMENT ERROR on: span.title-content")

        try:
            # Task 2.5 / 3.5: find the element that stores the author
            authors = item.find_elements(By.CSS_SELECTOR,'a.author-link')
            print(f'{len(authors)} authors found')
            authors_names = [] 
            if authors:
                for author in authors:
                    author_name = author.text.strip()
                    print(f'Author: {author_name}')
                    authors_names.append(author_name)
            else:
                authors_names.append("No Author")
            authors_names_joined = '; '.join(authors_names)
            print(f'Authors: {authors_names_joined}')
        except StaleElementReferenceException:
                print("❗ STALE ELEMENT ERROR on: a.author-link")

        try:
            # Task 2.6 / 3.5: find the element that stores the format of the book and the year it was published
            format_year_raw = item.find_element(By.CSS_SELECTOR,'span.display-info-primary').text.strip()
            print(format_year_raw)
            if format_year_raw:
                match_format_year = re.match(r'^(.*?\s*-\s*\d{4})', format_year_raw)
                if match_format_year:
                    format_year = match_format_year.group(1)
                else:
                    format_year = "No format"
                print(format_year)
        except StaleElementReferenceException:
            print("❗ STALE ELEMENT ERROR on: span.display-info-primary")

        # Task 3.5: Create a dict that stores these values, with the keys being Title, Author, and Format-Year
        dict = {
            "Title": title, 
            "Author": authors_names_joined,
            "Format-Year": format_year,
        }

        # Increment total items scraped
        total_items_scraped +=1

        # Task 3.5: Append the dictionary to the results list
        try:
            results.append(dict)
            # print(results)
        except StaleElementReferenceException:
            print(f"Appending scraping results error: {e}")
        
    # Check page number
    print(f"current_page: {current_page}")

    # Increment total pages scraped
    total_pages_scraped +=1

    # Check if the next page exists
    try:
        next_page_chevron = driver.find_element(By.CSS_SELECTOR, 'li.pagination__next-chevron')
        if 'disabled' in next_page_chevron.get_attribute('class'):
            print("Next chevron disabled.")
            print("No more pages available.")
            break # No more pages
        else:
            next_page_link = next_page_chevron.find_element(By.CSS_SELECTOR, 'a.pagination-item__link')
            # print(next_page_link.get_attribute('href'))
            next_page_link.click()
            time.sleep(4)
    except Exception as e:
        print(f"Clicking next page link error: {e}") 

# Check totals
print(f"{total_pages_scraped} pages scraped")
print(f"{total_items_scraped} items scraped")

# Task 3.6: Save results to a DataFrame and print that DataFrame
df_results = pd.DataFrame(results)
print(df_results)

driver.quit()

# Task 4.1: Write the DataFrame to a file called get_books.csv, within the assignment9 folder
df_results.to_csv('./get_books.csv', sep=',', index=True, header=True, encoding=None)

# TAsk 4.2: Write the results list to a file called get_books.json, within the assignment9 folder
data = {"results": results}
with open('get_books.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)

# DOM elements from search for scraper
    # li: li.cp-search-result-item
    # title: span.title-content 
    # authors: span.cp-author-link
    # author: a.author-link (account for multiple authors)
    # format, year: div.manifestation-item-format-info-wrap
    # format, year: span.display-info-primary (beginning: format, end: year) div .cp-format-info
    # cp-pagination-item pagination__next-chevron
    # cp-pagination-item pagination__next-chevron pagination-item--disabled
