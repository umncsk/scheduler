from selenium import webdriver
from bs4 import BeautifulSoup
import datetime
import time
import re
import zenhan

def getTime():
    month = datetime.date.today().month
    if (3 <= month and month < 6) or (9 <= month and month < 12):
        return 0
    else:
        return 1

#receive id and pswd, then return html source
def getPageSource(id, pswd):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome("Drivers/chromedriver.exe", options=options)

    driver.get("https://g-sys.toyo.ac.jp/portal/")
    time.sleep(1)

    useridElement = driver.find_element_by_name("j_username")
    passwordElement = driver.find_element_by_name("j_password")
    loginElement = driver.find_element_by_name("login")
    useridElement.send_keys(id)
    passwordElement.send_keys(pswd)
    loginElement.click()
    time.sleep(1)

    processElement = driver.find_element_by_id("menu_3800")
    processElement.click()
    time.sleep(1)

    confTable = driver.find_element_by_link_text("履修登録確認表")
    confTable.click()
    time.sleep(1)

    driver.switch_to.window(driver.window_handles[1])

    source = driver.page_source

    return source

#receive html source, then fill in the template and return
def exportAsDict(html):
    exportData = {
        "Spring":{
        "Monday":[],
        "Tuesday":[],
        "Wednesday":[],
        "Thursday":[],
        "Friday":[],
        "Saturday":[],
        "Sunday":[],
    },
        "Autumn":{
        "Monday":[],
        "Tuesday":[],
        "Wednesday":[],
        "Thursday":[],
        "Friday":[],
        "Saturday":[],
        "Sunday":[],
    }
    }
    soup = BeautifulSoup(html, "html.parser")
    tables = soup.find_all("table",{"class":"list"})[0]
    rows = tables.find_all("tr")[0]
    contents = tables.find_all("td")

    weekTags = {
        "月": "Monday",
        "火": "Tuesday",
        "水": "Wednesday",
        "木": "Thursday",
        "金": "Friday",
        "土": "Saturday",
        "日": "Sunday",
        }

    objects = [content.text.strip() for content in contents if content != ""]

    if "春学期" in objects:
        semester = "Spring"
    elif "秋学期" in objects:
        semester = "Autumn"

    quarter = getTime()

    if (("１Ｑ" or "３Ｑ") in objects) and (quarter == 0):
        quarter = 0
    elif(("２Ｑ" or "４Ｑ") in objects) and (quarter == 1):
        quarter = 1
    else:
        quarter = 2

    objects = objects[1:]
    week_counter = 0
    for weekTag in weekTags:
        object_counter = 0
        for object in objects:
            if object == weekTag:
                set = weekTag
                if week_counter == 0:
                    week_counter = 1
                else:
                    objects = objects[object_counter:]
                    object_counter = 0
                break

            elif re.match(r"(?<![０-９])([０-９])(?![０-９])", object):
                classNum = int(zenhan.z2h(object))
                isClass = 0
                if classNum != 0:
                    isClass = 1
                exportData[semester][weekTags[set]].append((classNum, isClass, 2))
            object_counter += 1
    return exportData

    def makelist():
        testlist=[]
        for j in range(0,7):
            testlist.append(0)
        return testlist

    def changedata(dict_sample):
        
        return 0
