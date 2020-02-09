from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from time import sleep
from secret import username, password
from random import random

class TinderBot():
    def __init__(self):
        self.profile = webdriver.FirefoxProfile('')
        self.driver = webdriver.Firefox(self.profile)

    def login(self):
        self.driver.get('https://tinder.com')

        sleep(3)

        fb_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/div[2]/button')
        fb_btn.click()

        # switch to login popup
        sleep(10)

        popup_1 = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/button[1]')
        popup_1.click()

        sleep(10)

        popup_2 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup_2.click()

    def like(self):
        like_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[3]')
        like_btn.click()

    def dislike(self):
        dislike_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[1]')
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

bot = TinderBot()
bot.login()
bot.auto_swipe()
bot.close_popup()
bot.close_match()