import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def getAthleteLink(name):
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chromeDriver = webdriver.Chrome(options=options)
    chromeDriver.get('https://olympics.com/en/athletes/')
    chromeDriver.implicitly_wait(20)
    inputBox = chromeDriver.find_element(by=By.ID, value="input-search-athletes")
    inputBox.send_keys(name)
    time.sleep(3)
    inputBox.send_keys(Keys.ARROW_DOWN)
    inputBox.send_keys(Keys.RETURN)
    time.sleep(3)
    ul_list = chromeDriver.find_element(by=By.CSS_SELECTOR, value=".search--list.row")
    li_item = ul_list.find_element(by=By.TAG_NAME, value="li")
    Link = ul_list.find_element(by=By.TAG_NAME, value="a").get_attribute("href")
    time.sleep(1)
    return Link


AthletesDF = pd.read_csv('./Athletes.csv')
AthleteLinks = []
for ind in AthletesDF.index[:100]:
    query = AthletesDF['Name'][ind].replace('-', '')
    q = query.split()
    query = '"' + query + '"' + ' OR "' + q[0] + '" * "' + q[-1] + '"'
    link = getAthleteLink(query)
    AthleteLinks.append(link)
    print(ind, AthletesDF['Name'][ind], link)
    time.sleep(1)


# AthletesDF['URL'] = AthleteLinks
# AthletesDF.to_csv('./Athletes_With_Links.csv')
