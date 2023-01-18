import csv
import datetime
import os

#FIELD_NAMES = ['Date','Numero','Stampata in','Specie','Articoli disponibili','Da','Tendenza di prezzo','Prezzo medio 30 giorni','Prezzo medio 7 giorni','Prezzo medio 1 giorno','link']

'''function to check if data folder exist
    else create it.
'''
def check_folder_data_exist():
    path = "cardmarket_pokemon_data"

    isExist = os.path.exists(path)
    if not isExist:
        os.makedirs(path)
        return False
    else:
        return False
    
def check_if_file_exist(path,filename):
    return os.path.exists(path.join(filename))
    
def create_csv(filename,data):
    dt = datetime.datetime.now()
    #Convert datetime in ISOFORMAT
    data['Date'] = dt.isoformat()
    
    #Create and write on file
    with open(filename+'.csv','w',newline='') as f:
        writer = csv.DictWriter(f, fieldnames = data.keys())
        writer.writeheader()
        writer.writerow(data)
        
def add_row_to_csv(filename, data):
    dt = datetime.datetime.now()
    #Convert datetime in ISOFORMAT
    data['Date'] = dt.isoformat()
    
    #Append to EOF a new row with new data
    with open(filename+'.csv','a') as f:
        dictwriter_object = csv.DictWriter(f, fieldnames=data.keys())
        dictwriter_object.writerow(data)
        f.close()
        

def create_file_name(link):
    s = link.split("/")
    language = s[3]
    version = s[-2]
    name = s[-1]
    return language.upper() + "_" + version + "_" + name

#TEST CREATE_FILE_NAME
s = create_file_name('https://www.cardmarket.com/it/Pokemon/Products/Singles/Silver-Tempest/Radiant-Jirachi-SIT120')
print(s)

#TEST CREATE_CSV
#d = {'Numero': '120', 'Stampata in': 'Tempesta Argentata', 'Specie': 'Jirachi', 'Articoli disponibili': 947, 'Da': 1.39, 'Tendenza di prezzo': 1.39, 'Prezzo medio 30 giorni': 1.32, 'Prezzo medio 7 giorni': 1.38, 'Prezzo medio 1 giorno': 1.63, 'link': 'https://www.cardmarket.com/it/Pokemon/Products/Singles/Silver-Tempest/Radiant-Jirachi-SIT120'}
#create_csv(s, d)

#TEST ADD_ROW_TO_CSV
d = {'Numero': '120', 'Stampata in': 'Tempesta Argentata', 'Specie': 'Jirachi', 'Articoli disponibili': 947, 'Da': 1.39, 'Tendenza di prezzo': 1.39, 'Prezzo medio 30 giorni': 1.32, 'Prezzo medio 7 giorni': 1.38, 'Prezzo medio 1 giorno': 1.63, 'link': 'https://www.cardmarket.com/it/Pokemon/Products/Singles/Silver-Tempest/Radiant-Jirachi-SIT120'}
add_row_to_csv('IT_Silver-Tempest_Radiant-Jirachi-SIT120',d)