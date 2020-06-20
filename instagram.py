from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time
import schedule


global x
x = 0

print ("coming here")
usrnames = ['emperoreby']  # username whom you will send the message
browser = webdriver.Firefox(executable_path='/home/emperoreby/Downloads/geckodriver')
browser.get('https://www.instagram.com/accounts/login/')

time.sleep(2)

usrname_bar = browser.find_element_by_name('username')  # Find the username bar
passwrd_bar = browser.find_element_by_name('password')  # Find the password bar

username = ''  # Enter your username here
password = ''  # Enter your password here

usrname_bar.send_keys(username)
passwrd_bar.send_keys(password + Keys.ENTER)

time.sleep(11)

def send_msg(usrnames):
    browser.get('https://www.instagram.com/direct/inbox')

    time.sleep(5)
     
    nxt_btn = browser.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[1]/a')
    nxt_btn.click()

    #to_btn = browser.find_element_by_name('queryBox')
    #to_btn.send_keys(usrnames)

    #time.sleep(8)

    #chk_mrk = browser.find_element_by_class_name('dCJp8')
    #chk_mrk.click()

    time.sleep(3)

    nxt_btn = browser.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div/div[4]/div[2]/div/div/div/div/div/div/div')
    value =  nxt_btn.get_attribute('innerHTML')
    hov = ActionChains(browser).move_to_element(nxt_btn)
    hov.perform()
    ana_btn = browser.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div/div[3]/div[2]/div/div/div/div[1]/button')
    ana_btn.click()
    unsend_btn = browser.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div/div[3]/div[2]/div/div/div/div[2]/div/div[2]/div[3]/button/div')
    unsend_btn.click()

    time.sleep(6)

    #txt_box = browser.find_element_by_tag_name('textarea')
    #txt_box.send_keys("Hi @{usrnames} ! What's up ?")  # Customize your message

    time.sleep(2)

    #snd_btn = browser.find_elements_by_tag_name('button')
    #snd_btnn = snd_btn.__getitem__(3)
    #snd_btnn.click()

    time.sleep(4)

count = 0
try:
    for usrnamee in usrnames:
        send_msg(usrnamee)
        count += 1

except TypeError:
    print('Failed!')

#browser.quit()

print('''
Successfully Sent {count} Massages

Python Programme by
      ___   ___ _      _         
     | _ \ / __(_)_ _ | |_  __ _ 
     |  _/ \__ \ | ' \| ' \/ _` |
     |_|   |___/_|_||_|_||_\__,_|

    Follow me on Instagram @codeinpy 

    Github codein-py
''')

x += 1


