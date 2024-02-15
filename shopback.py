import pandas as pd

from datetime import date
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

site_url = 'https://www.shopback.com.au/all--stores'

def scrape_url(url):
    driver.get(url)
    items = driver.find_elements(By.XPATH, "/html/body/div[2]/div[2]/div/div/div/div[2]/div")

    for i, item in enumerate(items):
        try:
            link = item.find_element(By.TAG_NAME,'a').get_attribute("href")
            df.loc[i, "link"] = link
        except:
            pass
        try:
            cname = item.find_element(By.TAG_NAME, 'picture').find_element(By.TAG_NAME, 'img').get_attribute("alt")
            df.loc[i, "Store_Name"] = cname
        except:
            pass
        try:
            cashback = item.find_element(By.CLASS_NAME, 'atom__typo--type-cashback').text
            df.loc[i, "Discount"] = cashback
        except:
            pass
        try:
            df.loc[i, "Scraped_Date"] = date.today().strftime('%Y/%m/%d')
            df.to_csv('scraped_details.csv', index=False)
        except:
            pass
    driver.close()


if __name__ == "__main__":
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    df = pd.DataFrame(columns=["Store_Name"])

    scrape_url(site_url)