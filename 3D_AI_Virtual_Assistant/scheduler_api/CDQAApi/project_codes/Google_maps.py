'''https://www.google.com/maps/dir/Ichalkaranji+Maharashtra/Kavathe+Mahankal+Maharashtra+416405'''


from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import time
import webbrowser



#data = "play new video by mr beast"
# data = play new video by shreeman legend

def google_maps_func(data):
    from CDQAApi.driver_module import driver
    driver.get('chrome://settings/clearBrowserData')
    #data = "what is the distance of pune, maharashtra from sangli, maharashtra"

    if data.find("to") != -1:
        source = data[data.find("from")+5:data.find("to")-1]
        destination = data[data.find("to")+3:]
        link = "https://www.google.com/maps/dir/"+str(source.replace(" ","+"))+"/"+str(destination.replace(" ","+"))
        driver.get(link)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        soup = soup.find('div', class_="ivN21e tUEI8e fontBodyMedium").find('div').get_text()
        return soup
    source = data[data.find("from")+5:]
    destination = data[data.find("of")+3:data.find("from")-1]
    link = "https://www.google.com/maps/dir/"+str(source.replace(" ","+"))+"/"+str(destination.replace(" ","+"))
    driver.get(link)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    soup = soup.find('div', class_="ivN21e tUEI8e fontBodyMedium").find('div').get_text()
    return soup   
#google_maps_func()