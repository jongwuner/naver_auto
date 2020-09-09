from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from random import random
from selenium import webdriver
import time
from  selenium.webdriver.common.keys import Keys
import pyperclip

def login(driver) :
    id_form = driver.find_element_by_id('id')
    pw_form = driver.find_element_by_id('pw')
    id_form.click()
    pyperclip.copy('jklh0202')
    id_form.send_keys(Keys.CONTROL, 'v')
    time.sleep(1)
    pw_form.click()
    pyperclip.copy('1j2k3l20^^')
    pw_form.send_keys(Keys.CONTROL, 'v')
    time.sleep(1)
    login_btn = driver.find_element_by_id('log.login')
    login_btn.click()

def work(driver) :
    i = 1
    while True :
        try :
            while True :
                print("여까진 오는데요")
                driver.get('https://m.blog.naver.com/Recommendation.nhn')
                time.sleep(5)
                post = driver.find_elements_by_class_name('title__2VIQG')[2]
                post.click()
                time.sleep(10)
                print("여까지도 오시나요?")


                try :
                    likeP = driver.find_element_by_xpath('//*[@id="ct"]/div[4]/div[3]/div/div[1]/div/div/a')
                    like = likeP.find_element_by_xpath('//*[@id="ct"]/div[4]/div[3]/div/div[1]/div/div/a')

                    actions = ActionChains(driver)
                    time.sleep(5)
                    actions.move_to_element(like).click().perform()
                    time.sleep(5)
                except :
                    time.sleep(10)
        except NoSuchElementException as e:
            print("[Error] ", e)
            pass
        except Exception as e:
            print("[Error] 주기값을 조정해야 합니다.", e.args)


def main() :
    driver = webdriver.Chrome(r'chromedriver.exe')
    driver.get('https://nid.naver.com/nidlogin.login?url=https%3A%2F%2Fsection.blog.naver.com%2FBlogHome.nhn')
    time.sleep(5)
    login(driver)
    work(driver)
    time.sleep(100)

main()