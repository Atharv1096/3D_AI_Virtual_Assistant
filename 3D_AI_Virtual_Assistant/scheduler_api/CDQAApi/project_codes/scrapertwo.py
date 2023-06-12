from bs4 import BeautifulSoup
from selenium import webdriver
import csv
import json
import os

with open("scrape.json","w") as f:
    json.dump([], f)

def write_json(new_data, filename='scrape.json'):
    with open(filename,'r+') as file:
        file_data = json.load(file)
        file_data.append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent = 4)



options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Chrome("chromedriver", chrome_options=options)


#url = "https://rajpurkar.github.io/SQuAD-explorer/explore/1.1/dev/"
templist = ["https://rajpurkar.github.io/SQuAD-explorer/explore/1.1/dev/Super_Bowl_50.html",

"https://rajpurkar.github.io/SQuAD-explorer/explore/1.1/dev/Warsaw.html",

"https://rajpurkar.github.io/SQuAD-explorer/explore/1.1/dev/Normans.html",

"https://rajpurkar.github.io/SQuAD-explorer/explore/1.1/dev/Nikola_Tesla.html",

"https://rajpurkar.github.io/SQuAD-explorer/explore/1.1/dev/Computational_complexity_theory.html",

"https://rajpurkar.github.io/SQuAD-explorer/explore/1.1/dev/Teacher.html",

"https://rajpurkar.github.io/SQuAD-explorer/explore/1.1/dev/Martin_Luther.html",

"https://rajpurkar.github.io/SQuAD-explorer/explore/1.1/dev/Southern_California.html",

"https://rajpurkar.github.io/SQuAD-explorer/explore/1.1/dev/Sky_(United_Kingdom).html",

"https://rajpurkar.github.io/SQuAD-explorer/explore/1.1/dev/Victoria_(Australia).html",

"https://rajpurkar.github.io/SQuAD-explorer/explore/1.1/dev/Huguenot.html",

"https://rajpurkar.github.io/SQuAD-explorer/explore/1.1/dev/Steam_engine.html",

"https://rajpurkar.github.io/SQuAD-explorer/explore/1.1/dev/Oxygen.html",

"https://rajpurkar.github.io/SQuAD-explorer/explore/1.1/dev/1973_oil_crisis.html",

"https://rajpurkar.github.io/SQuAD-explorer/explore/1.1/dev/Apollo_program.html",

"https://rajpurkar.github.io/SQuAD-explorer/explore/1.1/dev/European_Union_law.html",

"https://rajpurkar.github.io/SQuAD-explorer/explore/1.1/dev/Amazon_rainforest.html",

"https://rajpurkar.github.io/SQuAD-explorer/explore/1.1/dev/Ctenophora.html",

"https://rajpurkar.github.io/SQuAD-explorer/explore/1.1/dev/Fresno,_California.html",

"https://rajpurkar.github.io/SQuAD-explorer/explore/1.1/dev/Packet_switching.html",

"https://rajpurkar.github.io/SQuAD-explorer/explore/1.1/dev/Black_Death.html",

"https://rajpurkar.github.io/SQuAD-explorer/explore/1.1/dev/Geology.html",

"https://rajpurkar.github.io/SQuAD-explorer/explore/1.1/dev/Newcastle_upon_Tyne.html",

"https://rajpurkar.github.io/SQuAD-explorer/explore/1.1/dev/Victoria_and_Albert_Museum.html",

"https://rajpurkar.github.io/SQuAD-explorer/explore/1.1/dev/American_Broadcasting_Company.html",

"https://rajpurkar.github.io/SQuAD-explorer/explore/1.1/dev/Genghis_Khan.html",

"https://rajpurkar.github.io/SQuAD-explorer/explore/1.1/dev/Pharmacy.html",

"https://rajpurkar.github.io/SQuAD-explorer/explore/1.1/dev/Immune_system.html",

"https://rajpurkar.github.io/SQuAD-explorer/explore/1.1/dev/Civil_disobedience.html",

"https://rajpurkar.github.io/SQuAD-explorer/explore/1.1/dev/Construction.html",

"https://rajpurkar.github.io/SQuAD-explorer/explore/1.1/dev/Private_school.html",

"https://rajpurkar.github.io/SQuAD-explorer/explore/1.1/dev/Harvard_University.html",

"https://rajpurkar.github.io/SQuAD-explorer/explore/1.1/dev/Jacksonville,_Florida.html",

"https://rajpurkar.github.io/SQuAD-explorer/explore/1.1/dev/Economic_inequality.html",

"https://rajpurkar.github.io/SQuAD-explorer/explore/1.1/dev/Doctor_Who.html",

"https://rajpurkar.github.io/SQuAD-explorer/explore/1.1/dev/University_of_Chicago.html",

"https://rajpurkar.github.io/SQuAD-explorer/explore/1.1/dev/Yuan_dynasty.html",

"https://rajpurkar.github.io/SQuAD-explorer/explore/1.1/dev/Kenya.html",

"https://rajpurkar.github.io/SQuAD-explorer/explore/1.1/dev/Intergovernmental_Panel_on_Climate_Change.html",

"https://rajpurkar.github.io/SQuAD-explorer/explore/1.1/dev/Chloroplast.html",

"https://rajpurkar.github.io/SQuAD-explorer/explore/1.1/dev/Prime_number.html",

"https://rajpurkar.github.io/SQuAD-explorer/explore/1.1/dev/Rhine.html",

"https://rajpurkar.github.io/SQuAD-explorer/explore/1.1/dev/Scottish_Parliament.html",

"https://rajpurkar.github.io/SQuAD-explorer/explore/1.1/dev/Islamism.html",

"https://rajpurkar.github.io/SQuAD-explorer/explore/1.1/dev/Imperialism.html",

"https://rajpurkar.github.io/SQuAD-explorer/explore/1.1/dev/United_Methodist_Church.html",

"https://rajpurkar.github.io/SQuAD-explorer/explore/1.1/dev/French_and_Indian_War.html",

"https://rajpurkar.github.io/SQuAD-explorer/explore/1.1/dev/Force.html" ]


size = int(len(templist[0]))
tempval = templist[0][59:size-5]

response = driver.get(templist[0])


soup = BeautifulSoup(driver.page_source, "html.parser")


para_div = soup.find('div', class_='para-wrap').find('pre').get_text()
#print(para_div)
id=1
with open(str(tempval)+'.txt','w',encoding="utf-8") as txtfile:
    txtfile.write('[')
    for entry in soup.find_all('div', class_='para-wrap'):
        paravalue = str(entry.find('pre').get_text())
        #txtfile.write("paragraph : "+paravalue)
        #txtfile.write('\n')
        txtfile.write('\n\t{\n\t\t"context":"')
        tmp = str(paravalue)
        tmp = tmp.replace('"','')
        txtfile.write(tmp)
        txtfile.write('",')
        txtfile.write('\n\t\t"qas": [')
        #print("paragraph : "+paravalue)
        for qasentry in entry.find('div', class_='qas-wrap'):
            questionvalue = qasentry.find('strong', class_='question').get_text()
            #print("question : "+questionvalue)
            txtfile.write('\n\t\t\t{\n\t\t\t\t"id": "')
            strobj = str(id).zfill(4)
            txtfile.write(strobj)
            id = id+1
            txtfile.write('",\n\t\t\t\t"is_impossible" : false,\n\t\t\t\t"question" : "')
            tmpq = str(questionvalue)
            txtfile.write(tmpq)
            txtfile.write('",')
            txtfile.write('\n\t\t\t\t"answers": [')
            
            
            #print("Answer: "+str(ansentry.get_text()))
            #txtfile.write("answer : "+str(ansentry.get_text()))
            ansentry = qasentry.find('span', class_='answer')
            
            answervalue = str(ansentry.get_text())
            #txtfile.write('\n')
            tmpa = str(answervalue)
            tmpa = tmpa.replace('"','')
            txtfile.write('\n\t\t\t\t\t{\n\t\t\t\t\t\t"text": "')
            txtfile.write(tmpa)
            txtfile.write('",\n\t\t\t\t\t\t"answer_start": ')
            ansstart = paravalue.find(tmpa)
            txtfile.write(str(ansstart))
            txtfile.write('\n\t\t\t\t\t}')
            #length = len(txtfile)
            #txtfile = txtfile[:length-2]
            txtfile.write('\n\t\t\t\t]\n\t\t\t},')
            #print('\n\n')
            #txtfile.write("question : "+questionvalue)
            #txtfile.write('\n')
        
        txtfile.write('\n\t\t]\n\t},')
            


"""write_json({
    "context": paravalue,
    "qas": [
        {
            "is_impossible" : False,
            "question" : questionvalue,
            "answers" : [
                {
                   "text" : answervalue, 
                }
            ]
        }
    ],
})


"answers" : [
                {
                   "text" : answervalue, 
                }
            ]"""