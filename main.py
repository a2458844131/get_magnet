from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import os

DRIVER_PATH = Service("/usr/bin/chromedriver")
result = []


def get_real_magnet(page_url):
    print("jump to " + page_url)
    driver.get(page_url)
    magent_url = driver.find_element(by=By.CLASS_NAME, value="panel-body").text
    return magent_url


if __name__ == "__main__":
    # 设置浏览器
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--headless')  # 无头参数
    options.add_argument('--disable-gpu')
    options.add_argument('proxy-server=socks5://127.0.0.1:10808')
    # 启动浏览器
    driver = Chrome(service=DRIVER_PATH, options=options)
    # 访问目标URL
    URL = 'https://868888.net'
    driver.get(URL)
    elem = driver.find_element(by=By.ID, value="search")
    elem.send_keys("数据结构")
    submit = driver.find_element(by=By.ID, value="btnSearch").click()
    html_serch = driver.page_source
    html_serch = BeautifulSoup(html_serch, "html.parser")
    html_items = html_serch.findAll('div', class_="item-title")
    for html_item in html_items:
        item_dict = {}
        real_url = ''.join(URL + html_item.a.get('href'))
        name = html_item.text
        item_dict["name"] = name
        item_dict['magent_url'] = get_real_magnet(real_url)
        result.append(item_dict)
    print(result)
    driver.close()
