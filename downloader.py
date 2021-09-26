import pyperclip
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

#pyperclip.copy('helo')
while True:
    s = pyperclip.waitForPaste()
    
#    v = s.find('instagram')
    
    link = s
    print (link)
    driver = webdriver.Chrome('chromedriver')
    driver.get(link)
    soup = BeautifulSoup(driver.page_source,'html')
    img = soup.find('img',class_='FFVAD')
    img_url = img['src']
    r = requests.get(img_url)

    with open("instabot"+str(time.time())+".png",'wb') as f:
        f.write(r.content)

    print ('success')
    time.sleep(20) 
