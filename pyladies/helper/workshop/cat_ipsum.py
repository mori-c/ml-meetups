#! /usr/bin/env python3
# selenium module will launch browser that will interact with site to get cat ipsum

# add delay with pause
import pause
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support 
# user who click based on ID, name, class, tag
# selenium is sensitive to timing

import expected_conditions as ec
from selenium.webdriver.common.by import By


# create browser object
browser = webdriver.Chrome(executable_path=r'/Users/lindqui5/Desktop/chromedriver')
# pass object with url
browser.get('http://www.catipsum.com/')
pause.seconds(1)
# find element by name or any other name to get item you want to identity and get
# only want 1 paragraph with a title
paraNum = browser.find_element_by_name('par_count')
paraNum.clear()
paraNum.send_keys('1')
browser.find_element_by_id('add_title').click()
# get a random cat breed value with select list option
browser.find_element_by_xpath("//select/option[@value='breeds']").click()
browser.find_element_by_name('Generate').click()

# wait for element to appear
wait = WebDriverWait(browser, 10) # wait up to 10 seconds before throwing a TimeoutException
# for title, copy selector from inspector: #selectable > div
# if site has dropdown menu to do a filter search, use XPATH to grab item path
# to get XPATH, go to browser, find item, right click, copy to XPATH (absolute path: /user/user/to/some/path/where/file/is)
title = wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="selectable"]/div')))
print(title.text)

# get 3 cat ipsum phrases
browser.find_element_by_xpath("//select/option[@value='phrase']").click()
# create submit button again - stale element reference
browser.find_element_by_name('Generate').click()
ipsum = wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="selectable"]/div')))
for x in range (1,4):
    print(browser.find_element_by_xpath('//*[@id="selectable"]/span[' + str(x) + ']').text)
    
browser.close()
browser.quit()




