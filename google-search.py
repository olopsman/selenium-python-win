from selenium import webdriver

driver=webdriver.Chrome("chromedriver.exe")
driver.get("https://www.google.com")
driver.get_screenshot_as_file("test.png")
driver.find_element_by_id("lst-ib").send_keys("Automation")
driver.find_element_by_name("btnK").click()
