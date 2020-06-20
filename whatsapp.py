from selenium import webdriver
import time

browser = webdriver.Firefox(executable_path='/home/emperoreby/Downloads/geckodriver')
browser.get("https://web.whatsapp.com/")
time.sleep(15) #time provided to sign you in on the wb app.
group_array = ["Indus IND","Calvary fellowship groups","Orangearmy official","It's valparai man","Dayspring","OnePlus 7 India","CCT youths"]
sent_contact = []
#only DMs and no group messages by checking mute icon.

while(1):
    unreadMsgs = browser.find_elements_by_xpath(".//span[contains(@class,'P6z4j')]")
    if not unreadMsgs:
        print ("Total unread messages: 0")
    else:
        print ("Total unread messages: "+ str(len(unreadMsgs)))
        text = "Hi I am Eby's personal assistant. Eby is sleeping right now. He will reply you tmrw morning"
        for msg in unreadMsgs:
            msg.click()
            value = browser.find_element_by_xpath("./html/body/div[1]/div/div/div[4]/div/header/div[2]/div/div/span")
            Name = value.text
            if not Name in group_array:
              sent_contact.append(Name);
              time.sleep(1)
              browser.find_element_by_xpath(".//*[@id='main']/footer/div[1]/div[2]/div/div[2]").send_keys(text)
              time.sleep(1)
              browser.find_elements_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]/button')[0].click()
              time.sleep(1)
    time.sleep(10)  


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
