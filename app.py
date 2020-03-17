from selenium import webdriver
import time

browser = webdriver.Firefox()
browser.get("https://web.whatsapp.com/")
time.sleep(60) #time provided to sign you in on the wb app.

#only DMs and no group messages by checking mute icon.
unreadMsgs = browser.find_elements_by_xpath(".//span[contains(@class,'P6z4j')]")

if not unreadMsgs:
    print ("Total unread messages: 0")
else:
    print ("Total unread messages: "+ str(len(unreadMsgs)))
    text = "Hi, I'm busy right now and will reply ASAP. BTW this is an automated message!"
    for msg in unreadMsgs:
        msg.click()
        time.sleep(5)
        browser.find_element_by_xpath(".//*[@id='main']/footer/div[1]/div[2]/div/div[2]").send_keys(text)
        time.sleep(2)
        browser.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]/button")[0].click()
        time.sleep(2)


'''
browser.find_element_by_xpath(".//*[@id='side']/div[2]/div/label/input").send_keys("Elon Musk") #search friend
time.sleep(5)
browser.find_element_by_xpath(".//*[@title='Elon Musk']").click()
time.sleep(5)
for i in range(1, 50):
    browser.find_element_by_xpath(".//*[@id='main']/footer/div[1]/div[2]/div/div[2]").send_keys("Spam Content!") #your message here.
    time.sleep(1)
    browser.find_element_by_xpath(".//*[@id='main']/footer/div[1]/button").click()
    time.sleep(1)
'''
