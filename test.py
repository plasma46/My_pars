from  import webdriver
import time

driver = webdriver.Chrome(executable_path = "D:\\My_pars\\chromedriver\\chromedriver")
url = "http://www.python.org"

try:
    driver.get(url = url)
    time.sleep(10)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()