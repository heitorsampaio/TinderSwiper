from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from time import sleep
from secret import username, password
from random import random

class BadooBot():
    def __init__(self):
        self.profile = webdriver.FirefoxProfile('/Users/heitorsampaio/Desktop/Tools/SMMarketingTools/Profile')
        self.options = Options()
        self.driver = webdriver.Firefox(self.profile, options=self.options)

    def login(self):
        self.driver.get('https://badoo.com')

        sleep(3)

        fb_btn = self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[3]/div/div[3]/div/div[1]/div[2]/div/div/a')
        fb_btn.click()

        sleep(20)

    def like(self):
        like_btn = self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/main/div[1]/div/div[1]/section/div/div[2]/div/div[2]/div[1]/div[1]')
        like_btn.click()
        try:
            sleep(5)
            self.driver.find_element_by_xpath('/html/body/aside/section/div[1]/div/div[2]/div/div[1]').click()
        except Exception:
            pass

    def dislike(self):
        dislike_btn = self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/main/div[1]/div/div[1]/section/div/div[2]/div/div[2]/div[2]/div[1]')
        dislike_btn.click()

    def auto_swipe(self):
        like_count, dislike_count = 0, 0
        while True:
            sleep(0.5)
            try:
                rand = random()
                if rand < .73:
                    self.like()
                    like_count = like_count + 1
                    print('{}th like swipe'.format(like_count))
                else:
                    self.dislike()
                    dislike_count = dislike_count + 1
                    print('{}th like swipe'.format(dislike_count))
            except Exception:
                try:
                    self.close_popup()
                except Exception:
                    self.close_match()

    def close_popup(self):
        popup_3 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        popup_3.click()

    def close_match(self):
        match_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        match_popup.click()

bot = BadooBot()
bot.login()
bot.auto_swipe()
bot.close_popup()
bot.close_match()