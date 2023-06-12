from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import time
import webbrowser




#data = "play new video by mr beast"
# data = play new video by shreeman legend

def youtube_latest(original_data):
    from CDQAApi.driver_module import driver
    driver.get('chrome://settings/clearBrowserData')
    flag = True
    index=original_data.find("by")
    
    data = original_data[index+3:]
    data=data.replace(" ","")
    #print(data)
    url = "https://www.youtube.com/@"+str(data)+"/videos"
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    #print(soup.prettify())
    latest_video = soup.find('a', class_="yt-simple-endpoint inline-block style-scope ytd-thumbnail", href=True)
    #print(latest_video)
    if latest_video == None:
        youtube_else(original_data)
    else:
        video_link = "https://www.youtube.com"+str(latest_video['href'])
        webbrowser.open(video_link)
    return

def youtube_shorts(original_data):
    from CDQAApi.driver_module import driver
    driver.get('chrome://settings/clearBrowserData')
    flag = True
    index=original_data.find("by")
    
    data = original_data[index+3:]
    data=data.replace(" ","")
    #print(data)
    url = "https://www.youtube.com/@"+str(data)+"/shorts"
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    #print(soup.prettify())
    latest_video = soup.find('a', class_="yt-simple-endpoint inline-block style-scope ytd-thumbnail", href=True)
    #print(latest_video)
    if latest_video == None:
        youtube_else(original_data)
    else:
        video_link = "https://www.youtube.com"+str(latest_video['href'])
        webbrowser.open(video_link)
    return flag

def youtube_else(original_data):
    from CDQAApi.driver_module import driver
    driver.get('chrome://settings/clearBrowserData')
    data = original_data
    data = data.replace(" ","+")

    driver.get("https://www.youtube.com/results?search_query="+str(data))
    #print(data)
    #youtube_search = driver.find_element(By.CLASS_NAME,"ytd-searchbox").send_keys(data)
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    webbrowser.open("https://www.youtube.com"+str(soup.find('a', class_="yt-simple-endpoint inline-block style-scope ytd-thumbnail",href = True)['href']))
    return

def youtube(data):
    from CDQAApi.driver_module import driver
    driver.get('chrome://settings/clearBrowserData')
    latests = ["latest video","new video","newest video","any video"]
    flag = False
    for sval in latests:
        if sval in data:
            flag = youtube_latest(original_data=data)
            break

    shorts = ["short","shorts"]
    for sval in shorts:
        if sval in data:
            flag = youtube_shorts(original_data=data)
            break

    if flag == False:
        youtube_else(original_data=data)
    
    response = str("opening youtube")
    return response
        #print(soup.prettify())
        