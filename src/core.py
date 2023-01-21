import requests
from bs4 import BeautifulSoup
import datetime

'''
function to return date
when request was made
'''
def dtimestrformat():
    now = datetime.datetime.now() # current date and time
    year = now.strftime("%Y")
    month = now.strftime("%m")
    day = now.strftime("%d")
    time = now.strftime("%H:%M:%S")
    date_time = now.strftime("%m/%d/%YT%H:%M:%S")
    return date_time


#Response part
'''
Return the body of card's web page
'''
def extractor(link):
    res = requests.get(link)
    bs = BeautifulSoup(res.text, 'html.parser')
    section = list(bs.find("dl"))
    del(section[0:2])
    del(section[4:6])
    for i in range(len(section)):
        section[i] = section[i].text
    sectiona, sectionb,  = section[::2], section[1::2]
    d = dict(zip(sectiona,sectionb))
    d['link'] = link
    return d


#Parsing a transform json part

'''
obtain a clean dictionary
wit sanitize key
'''
def transform_dict_value(card: dict):
    card['Articoli disponibili'] = int(card['Articoli disponibili'])
    card['Da'] = float(card['Tendenza di prezzo'].split(' ')[0].replace(',','.'))
    card['Tendenza di prezzo'] = float(card['Tendenza di prezzo'].split(' ')[0].replace(',','.'))
    card['Prezzo medio 30 giorni'] = float(card['Prezzo medio 30 giorni'].split(' ')[0].replace(',','.'))
    card['Prezzo medio 7 giorni'] = float(card['Prezzo medio 7 giorni'].split(' ')[0].replace(',','.'))
    card['Prezzo medio 1 giorno'] = float(card['Prezzo medio 1 giorno'].split(' ')[0].replace(',','.'))
    #print("sanityzing dictionary --> ", card)
    return card


#To process the program launch the command as below
#
##1 Digit link
#link = input("Digit Link: ")
#
##2 Obtain data
#csanityze = extractor(link)
#
##3 Sanityze and convert in a dictionary with valid model
#
#dataJson = transform_dict_value(csanityze)
## 3.1 Print data and datetime
##  3.1.1 Print data to track request datetime
#print(f"************{dtimestrformat()}************")
#for i in csanityze.keys():
#    print(i, " " , csanityze[i])
#print("************************")
#print()
##4 get information and insert in a exisenst json file or in case a new json file
#
#