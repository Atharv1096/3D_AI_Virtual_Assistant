from bs4 import BeautifulSoup
from selenium import webdriver
import csv



def gscraper(data):
    data.replace(' ','+')
    url = "https://www.google.com/search?q="+str(data)+"&start=0"
    from CDQAApi.driver_module import driver
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

    #print(result)
    return result

def gscraperlist(data):
    data.replace(' ','+')
    url = "https://www.google.com/search?q="+str(data)+"&start=0"
    from CDQAApi.driver_module import driver
    driver.get(url)

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    temp=[]
    for result in soup.find_all('div',class_="TT9RUc uV10if"):
            result1 = str(result.find('div', class_="JjtOHd").get_text())
            result2 = str(result.find('div', class_="ellip yF4Rkc AqEFvb").get_text())
            result = result1 + " > " + result2
            temp.append(result)
    return temp



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