import requests
from bs4 import BeautifulSoup
import datetime

'''
#extractor for 
name  
code  
series  
rarity  
specie  
avaibleN  
start_price  
avg_price_30_day  
avg_price_7_day  
avg_price_1_day 
'''

def cleanForDbModel(card: dict):
    card['Articoli disponibili'] = int(card['Articoli disponibili'])
    card['Da'] = float(card['Tendenza di prezzo'].split(' ')[0].replace(',','.'))
    card['Tendenza di prezzo'] = float(card['Tendenza di prezzo'].split(' ')[0].replace(',','.'))
    card['Prezzo medio 30 giorni'] = float(card['Prezzo medio 30 giorni'].split(' ')[0].replace(',','.'))
    card['Prezzo medio 7 giorni'] = float(card['Prezzo medio 7 giorni'].split(' ')[0].replace(',','.'))
    card['Prezzo medio 1 giorno'] = float(card['Prezzo medio 1 giorno'].split(' ')[0].replace(',','.'))
    #print("sanityzing dictionary --> ", card)
    return card

def createFileListLink():
    pass

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

def add_to_list(link: str) -> None:
    pass


card = extractor(input("metti il link porcodio!: "))

'''
{
    'Numero': '010', 
    'Stampata in': 'Pokémon GO', 
    'Specie': 'Charizard', 
    'Articoli disponibili': '404', 
    'Da': '0,80 €', 
    'Tendenza di prezzo': '1,82 €', 
    'Prezzo medio 30 giorni': '1,60 €', 
    'Prezzo medio 7 giorni': '1,55 €', 
    'Prezzo medio 1 giorno': '1,01 €', 
    'link': 'https://www.cardmarket.com/it/Pokemon/Products/Singles/Pokemon-GO/Charizard-PGO010?isReverseHolo=Y'
}
'''
csanityze = cleanForDbModel(card)
def dtimestrformat():
    now = datetime.datetime.now() # current date and time
    year = now.strftime("%Y")
    month = now.strftime("%m")
    day = now.strftime("%d")
    time = now.strftime("%H:%M:%S")
    date_time = now.strftime("%m/%d/%YT%H:%M:%S")
    return date_time

print(f"************{dtimestrformat()}************")
for i in csanityze.keys():
    print(i, " " , csanityze[i])
print(f"************************")
print()