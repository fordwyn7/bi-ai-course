from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import json
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.demoblaze.com/")

# Click on "Laptops"
time.sleep(2)
driver.find_element(By.XPATH, "//a[text()='Laptops']").click()
time.sleep(3)

laptops = []

# You can add pagination here if needed
cards = driver.find_elements(By.CLASS_NAME, "col-lg-4")

for card in cards:
    try:
        name = card.find_element(By.CLASS_NAME, "hrefch").text
        price = card.find_element(By.TAG_NAME, "h5").text
        description = card.find_element(By.CLASS_NAME, "card-text").text
        laptops.append({
            "name": name,
            "price": price,
            "description": description
        })
    except Exception as e:
        pass

# Save to JSON
with open("laptops.json", "w", encoding="utf-8") as f:
    json.dump(laptops, f, indent=2, ensure_ascii=False)
