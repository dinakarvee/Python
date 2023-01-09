import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import requests
service = Service(r"C:\Users\Sai Ram\Documents\Python\Driver\chromedriver.exe")

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(service = service, options = options)
    driver.get("https://stats.espncricinfo.com/ci/engine/records/team/match_results.html?class=3;id=2022;type=year")
    return driver

# def clean_text(text):
#     """Extract only the temperature from text"""
#     output = float(text.split(": ")[1])
#     return output


def main():
    get_driver()
    url = "https://stats.espncricinfo.com/ci/engine/records/team/match_results.html?class=3;id=2022;type=year"

    html = requests.get(url).content
    df = pd.read_html(html)[0]

    df.to_csv(r'C:\Users\Sai Ram\Documents\Power BI\End to End T-20 World Cup DashBoard\CSV Data\scappying.csv')


main()
