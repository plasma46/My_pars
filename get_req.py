from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path = "D:\\My_pars\\chromedriver\\chromedriver")
url = "http://stackoverflow.com/questions/7794087/running-javascript-in-selenium-using-python"

try:
    driver.get(url = url)
    driver.execute_script("document.getElementsByClassName('comment-user')[0].click()")
    time.sleep(10)
    content = driver.page_source

    content = content.encode('utf-8')
    time.sleep(10)
    print(content)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()

# from selenium import webdriver
# driver = webdriver.Firefox()
# driver.get("http://stackoverflow.com/questions/7794087/running-javascript-in-selenium-using-python")
# driver.execute_script("document.getElementsByClassName('comment-user')[0].click()")