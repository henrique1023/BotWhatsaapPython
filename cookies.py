import selenium.webdriver

driver = selenium.webdriver.Chrome()
driver.get("https://web.whatsapp.com/")

driver.execute_script('console.log(Store.Conn.__x_ref);')
driver.execute_script('console.log(Store.Conn.__x_serverToken)')