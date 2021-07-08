from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.youtube.com/')

searchbox = driver.find_element_by_xpath('//*[@id="search"]')
searchbox.send_keys('euro 2020')

searchButton = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
searchButton.click()

videoplay = driver.find_element_by_id('img')
videoplay.click() 

fullscreen = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[3]/div/ytd-player/div/div/div[27]/div[2]/div[2]/button[10]')
fullscreen.click()