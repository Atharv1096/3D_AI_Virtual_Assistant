from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import time
import webbrowser

import urllib



data = input("Enter video you want to search: ")
start_time = time.time()
#data = "play new video by mr beast"
# data = play new video by shreeman legend
latests = ["latest video","new video","newest video","any video"]
flag = False
for sval in latests:
    if sval in data:
        flag = True
        index=data.find("by")
        data = data[index+3:]
        data=data.replace(" ","")
        #print(data)
        url = "https://www.youtube.com/@"+str(data)+"/videos"
        from CDQAApi.driver_module import driver
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        #print(soup.prettify())
        latest_video = soup.find('a', class_="yt-simple-endpoint inline-block style-scope ytd-thumbnail", href=True)
        video_link = "https://www.youtube.com"+str(latest_video['href'])
        webbrowser.open(video_link)
        print("Execution time: "+str(time.time()-start_time)+" seconds")
        break

shorts = ["short","shorts"]
for sval in shorts:
    if sval in data:
        flag = True
        index=data.find("by")
        data = data[index+3:]
        data=data.replace(" ","")
        #print(data)
        url = "https://www.youtube.com/@"+str(data)+"/shorts"
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        #print(soup.prettify())
        latest_video = soup.find('a', class_="yt-simple-endpoint inline-block style-scope ytd-thumbnail", href=True)
        video_link = "https://www.youtube.com"+str(latest_video['href'])
        webbrowser.open(video_link)
        print("Execution time: "+str(time.time()-start_time)+" seconds")
        break

if flag == False:
    data = data.replace(" ","+")
    driver.get("https://www.youtube.com/results?search_query="+str(data))
    #youtube_search = driver.find_element(By.CLASS_NAME,"ytd-searchbox").send_keys(data)
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    webbrowser.open("https://www.youtube.com"+str(soup.find('a', class_="yt-simple-endpoint inline-block style-scope ytd-thumbnail",href = True)['href']))
    print("Execution time: "+str(time.time()-start_time)+" seconds")

    #print(soup.prettify())
    