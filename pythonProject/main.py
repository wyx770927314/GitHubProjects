import time

from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Base import global_params as gp


# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


start_params = {
    "platformName": gp.platformName,
    "deviceName": gp.deviceName,
    "appPackage": gp.appPackage,
    "appActivity": gp.appActivity
}
print(start_params)
driver = webdriver.Remote(gp.appium_server_ip, start_params)


def isElementExist_BY_ID(elementid):
    element = driver.find_element_by_id(elementid)
    if element is not None:
        return True
    else:
        return False


def two_click_agreebtn():
    if isElementExist_BY_ID('com.jike.cleaner.qingli.jkql:id/welcome_btn_approve'):
        print('隐私弹框存在')
        # 定位同意按钮，点击
        agree_btn = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
            [By.ID, "com.jike.cleaner.qingli.jkql:id/welcome_btn_approve"]))
        agree_btn.click()
        # 定位两次授权按钮
        agree_sq_btn = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "com.lbe.security.miui:id"
                                                                         "/permission_allow_foreground_only_button")))
        agree_sq_btn.click()
        time.sleep(3)
        agree_sq_btn.click()
    else:
        print('隐私弹框不存在')
        if not isElementExist_BY_ID('com.lbe.security.miui:id/permission_allow_foreground_only_button'):
            print('授权弹窗存在')
            # 定位两次授权按钮
            agree_sq_btn = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "com.lbe.security.miui:id"
                                                                             "/permission_allow_foreground_only_button")))
            agree_sq_btn.click()

            time.sleep(3)
            agree_sq_btn.click()
        else:
            print('授权弹窗不存在')







# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    two_click_agreebtn()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
