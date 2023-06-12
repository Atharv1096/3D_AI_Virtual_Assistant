from bs4 import BeautifulSoup
from selenium import webdriver
import webbrowser
from .chatgpt_connector import *




def gscraper(original_data):
    data = original_data
    from CDQAApi.driver_module import driver
    driver.get('chrome://settings/clearBrowserData')
    data.replace(' ','+')
    url = "https://www.google.com/search?q="+str(data)+"&start=0"
    driver.get(url)
    result = ""
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    if soup.find('div', class_="Z0LcW t2b5Cf") != None:
        result = soup.find('div', class_="Z0LcW t2b5Cf").get_text()
    elif soup.find('div', class_="Z0LcW t2b5Cf") == None and soup.find('div', class_="Z0LcW t2b5Cf CfV8xf")!=None:
        result = soup.find('div', class_="Z0LcW t2b5Cf CfV8xf")
        result = result.find('a').get_text()
    elif soup.find('div', class_="Z0LcW t2b5Cf CfV8xf") == None and soup.find('div', class_="kno-rdesc") !=None:
        result = soup.find('div', class_="kno-rdesc")
        result = result.find('span').get_text()
    elif soup.find('div', class_="kno-rdesc")==None and soup.find('div', class_="Z0LcW AZCkJd d2J77b t2b5Cf") != None:
        result = soup.find('div', class_="Z0LcW AZCkJd d2J77b t2b5Cf")
        result = result.find('div', class_="IZ6rdc").get_text()
    elif soup.find('div', class_="Z0LcW AZCkJd d2J77b t2b5Cf") == None and soup.find('div', class_ = "Z0LcW t2b5Cf vMhfn")!=None:
        result = soup.find('div', class_="Z0LcW t2b5Cf vMhfn").get_text()
    elif soup.find('div', class_ = "Z0LcW t2b5Cf vMhfn")==None and soup.find('div', class_ = "junCMe") !=None:
        result = soup.find('div', class_="junCMe")
        result = result.find('div', class_="title").get_text()
    """elif soup.find('div', class_ = "junCMe") ==None and soup.find('span', class_="hgKElc") != None:
        result = soup.find('span', class_="hgKElc").get_text()"""

    if (result == ""):
        result = gscraper_else(original_data=original_data)

    #print(result)
    return result

def gscraperlist(original_data):
    data = original_data
    from CDQAApi.driver_module import driver
    driver.get('chrome://settings/clearBrowserData')
    data.replace(' ','+')
    url = "https://www.google.com/search?q="+str(data)+"&start=0"
    driver.get(url)

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    temp=[]
    if "cast" in data or "members" in data:
        for result in soup.find_all('div',class_="TT9RUc uV10if"):
                result1 = str(result.find('div', class_="JjtOHd").get_text())
                result2 = str(result.find('div', class_="ellip yF4Rkc AqEFvb").get_text())
                result = result1 + " > " + result2
                temp.append(result)
    elif "companies" in data or "startups" in data:
        for result in soup.find_all('div', class_="FZPZX q8U8x PZPZlf"):
            result = str(result.get_text())
            temp.append(result)
    return temp

def gscraper_else(original_data):
    data = original_data
    from CDQAApi.driver_module import driver
    driver.get('chrome://settings/clearBrowserData')
    data.replace(' ', '+')  # wiki
    url = "https://www.google.com/search?q="+str(data)+"&start=0"
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    href = soup.find("div", class_="yuRUbf").find("a").get("href")
    
    print(href)
    webbrowser.open(href)
    #print(chatgpt_func(data=data))
    """data.replace(" ","+")
    webbrowser.open("https://www.google.com/search?q="+data+"&start=0")"""

def google_open(original_data):
    data = original_data
    from CDQAApi.driver_module import driver
    driver.get('chrome://settings/clearBrowserData')
    data.replace(' ','+') #wiki
    url = "https://www.google.com/search?q="+str(data)+"&start=0"
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    #link = soup.find('div', class_="byrV5b").find('cite').get_text().replace(soup.find('div', class_="byrV5b").find('span', class_="dyjrff qzEoUe").get_text(),"")
    link2 = str(soup.find('div', class_="byrV5b").find('cite').get_text())
    if "›" in link2:
        linkind = link2[:link2.find("›")-1]
        webbrowser.open(linkind)
        return
    webbrowser.open(link2)

    response = str("Opening Site")
    return response

    """url = "https://www.google.com/search?q="+str(data)+"&start=0"
    driver.get(url)

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    if soup.find('div', class_="Z0LcW t2b5Cf") != None:
        result = soup.find('div', class_="Z0LcW t2b5Cf").get_text()
    elif soup.find('div', class_="Z0LcW t2b5Cf") == None and soup.find('div', class_="Z0LcW t2b5Cf CfV8xf")!=None:
        result = soup.find('div', class_="Z0LcW t2b5Cf CfV8xf")
        result = result.find('a').get_text()
    elif soup.find('div', class_="Z0LcW t2b5Cf CfV8xf") == None and soup.find('div', class_="kno-rdesc") !=None:
        result = soup.find('div', class_="kno-rdesc")
        result = result.find('span').get_text()
    elif soup.find('div', class_="kno-rdesc")==None and soup.find('div', class_="Z0LcW AZCkJd d2J77b t2b5Cf") != None:
        result = soup.find('div', class_="Z0LcW AZCkJd d2J77b t2b5Cf")
        result = result.find('div', class_="IZ6rdc").get_text()
    elif soup.find('div', class_="Z0LcW AZCkJd d2J77b t2b5Cf") == None and soup.find('div', class_ = "Z0LcW t2b5Cf vMhfn")!=None:
        result = soup.find('div', class_="Z0LcW t2b5Cf vMhfn").get_text()
    elif soup.find('div', class_ = "Z0LcW t2b5Cf vMhfn")==None and soup.find('div', class_ = "junCMe") !=None:
        result = soup.find('div', class_="junCMe")
        result = result.find('div', class_="title").get_text()
    


    print(result)"""