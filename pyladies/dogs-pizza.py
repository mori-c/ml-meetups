# cat_ipsum origin


import pause
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support

browser = webdriver.Chrome
(executable_path = r'https://github.com/mori-c/meetups/blob/master/pyladies/helper/workshop/chromedriver'
 
browser.get('https://giphy.com/search/dogs-pizza')
pause.seconds(1)
 
paraNum = browser.find_element_by_name('par_count')
paraNum.clear()
paraNum.send_keys('1')
browser.find_element_by_id('add_title').click()
browser.find_element_by_name('Generate').click()
 
wait = WebDriverWait(browser, 10)
title = wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="selectable"]/div')))
print(title.text)

browser.find_element_by_xpath('//select/option[@value="phrase"]').click()
browser.find_element_by_name('Generate').click()

ipsum = wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="selectable"]/div')))
for x in range (1, 4):
 print(browser.find_element_by_xpath('//*[@id="selectable"]/span[' + str(x) + ']').text)
 
browser.close()
browser.quit()
 
 
 