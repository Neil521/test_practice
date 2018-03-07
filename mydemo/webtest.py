from selenium import webdriver
from time import sleep
import unittest2 as unittest


class Test(unittest.TestCase):
    '''打开火狐浏览器'''
    @classmethod
    def setUpClass(cls):
        '''打开浏览器'''
        cls.driver = webdriver.Firefox()
        # 设置大小
        # cls.driver.set_window_rect(200,200)
        # cls.driver.set_window_size(800,400)
        # 最大化
        cls.driver.maximize_window()

    def test_1(self):
        '''打开主页'''
        driver = self.driver
        driver.get("http://home.firefoxchina.cn/")

    def test_2(self):
        '''登录'''
        driver = self.driver
        driver.find_element_by_css_selector('.btn-pop-win').click()
        email=driver.find_element_by_class_name('email')
        email.clear()
        email.send_keys('136097832@qq.com')
        password=driver.find_element_by_id('password')
        password.clear()
        password.send_keys('xl12321xl')
        sleep(2)

    # 关闭浏览器
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()