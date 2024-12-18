from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import Select
import time

# 替换为你下载的EdgeDriver的完整路径
driver_path = r"xxxxxx/xxxxxxx/xxxx/xxx"

# 登录信息
username = 'xxxxxxxxxx'
password = 'xxxxxxxxxx'
domain = 'xxxx'  # 根据实际情况选择校园网，中国电信，中国联通，中国移动
login_url = 'http://202.114.177.246/'


def login_to_campus_net():
    # 创建Edge选项以忽略SSL错误
    edge_options = Options()
    edge_options.add_argument('--ignore-certificate-errors')
    edge_options.add_argument('--ignore-ssl-errors')

    # 使用Service来指定EdgeDriver的位置
    service = Service(driver_path)
    driver = webdriver.Edge(service=service, options=edge_options)

    # 打开校园网登录页面
    driver.get(login_url)

    # 等待页面加载
    time.sleep(0.5)

    try:
        # 找到用户名输入框并输入用户名
        username_input = driver.find_element(By.ID, 'username')
        username_input.send_keys(username)

        # 找到密码输入框并输入密码
        password_input = driver.find_element(By.ID, 'password')
        password_input.send_keys(password)

        # 选择下拉菜单中的一个选项
        domain_select = Select(driver.find_element(By.ID, 'domain'))
        domain_select.select_by_visible_text(f'{domain}')

        # 提交登录表单
        password_input.send_keys(Keys.RETURN)

        # 等待几秒钟确保登录成功
        time.sleep(0.5)

    finally:
        driver.quit()


if __name__ == "__main__":
    login_to_campus_net()
