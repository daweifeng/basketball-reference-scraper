from bs4 import BeautifulSoup
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains


import re
import pandas as pd
import os

#DRIVER_PATH = "./geckodriver"
DRIVER_PATH = "./chromedriver"

def download_data(url):
    # page = urllib.request.urlopen(url)
    #cap = DesiredCapabilities().FIREFOX
    #cap["marionette"] = True
    #driver = webdriver.Firefox(capabilities=cap, executable_path=DRIVER_PATH)
    driver = webdriver.Chrome(executable_path=DRIVER_PATH)
    action = ActionChains(driver)
    #driver.implicitly_wait(30)
    driver.get(url)

    # hover
    hove_xpath = "//*[@id='all_tgl_basic']/div[1]/div/ul/li[2]"
    hover_button = driver.find_element_by_xpath(hove_xpath)
    action.move_to_element(hover_button).perform()

    # click button
    xpath = "//*[@id='all_tgl_basic']/div[1]/div/ul/li[2]/div/ul/li[4]/button"
    get_csv_button = driver.find_element_by_xpath(xpath)
    action.move_to_element(get_csv_button).click()
    #get_csv_button.click()
    soup = BeautifulSoup(driver.page_source)
    content = soup.find('pre', attrs={'id': 'csv_tgl_basic'})
    print(content)

def main():
    base_url = "https://www.basketball-reference.com/teams/"
    team_names = ["MEM", "PHO", "MIN"]
    
    # Loop years
    for year in range(2008, 2009):
        for team in team_names:
            url = base_url + team + "/" + str(year)+ "/" + "gamelog"
            download_data(url)


main()


