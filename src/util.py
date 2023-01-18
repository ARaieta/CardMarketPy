import csv
import datetime


FIELD_NAMES = ['Date','Numero','Stampata in','Specie','Articoli disponibili','Da','Tendenza di prezzo','Prezzo medio 30 giorni','Prezzo medio 7 giorni','Prezzo medio 1 giorno','link']

def writeNewCsv(newfilename: str,data: dict) -> None:
    dt = datetime.datetime.now()
    
    data['Date'] = dt.isoformat()
    with open(newfilename+'.csv', 'w',newline='') as f:
        writer = csv.DictWriter(f, fieldnames = data.keys())
        writer.writeheader()
        writer.writerow(data)
        
def addDataToCsv(csvName, data,field_names):
    with open(csvName+'.csv','a') as f:
        dictwriter_object = csv.DictWriter(f, fieldnames=field_names)
        dictwriter_object.writerow(data)
        f.close()
        
