from selenium import webdriver
import datetime
import time
import pandas

# return binary schedule data
def get_user_schedule(id, pswd):
    # initialize selenium
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome("Drivers/chromedriver.exe", options=options)

    # page access
    driver.get("https://www.ace.toyo.ac.jp/ct/home")
    time.sleep(1)

    # login process
    useridElement = driver.find_element_by_name("userid")
    passwordElement = driver.find_element_by_name("password")
    loginElement = driver.find_element_by_name("login")
    useridElement.send_keys(id)
    passwordElement.send_keys(pswd)
    loginElement.click()
    time.sleep(1)

    # get page source as html
    html = driver.page_source

    data = pandas.io.html.read_html(html)[1].isnull()

    data = data.iloc[:, 1:]
    schedule_binary = ""
    for _, j in data.iteritems():
        for k in j:
            if k != True:
                schedule_binary += "1"
            else:
                schedule_binary += "0"
    # 8 binary per 1 day
    return schedule_binary
