from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.btbtdy.net')
driver.find_element_by_link_text('电影').click()