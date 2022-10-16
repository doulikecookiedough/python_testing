from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()))

# driver.get("https://www.nceas.ucsb.edu/publications-products")
# filter_category_value = driver.find_element(
#     By.CLASS_NAME, "page-title")
# print(filter_category_value.text)

category_ids = ('100', '101', '102', '103', '104', '105')
driver.get('https://www.nceas.ucsb.edu/publications-products')
category_list = []
for category in category_ids:
    filter_category_value = driver.find_element(
        By.NAME, f'category[{category}]')
    filter_category_value.find_elements(By.XPATH, ".//*")
    category_list.append(filter_category_value.text)
    print(f"List length: {len(category_list)}")
    empty_values_detected = False
    for item in category_list:
        if len(item) == 0:
            empty_values_detected = True
            break
