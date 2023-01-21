import os
import logging
from core import *
from json_handler import *
import time
#OPTIONAL read file from config file

PATH="cardmarket_pokemon_data"

def run():
    #set logging info
    logging.basicConfig()
    logger = logging.getLogger()
    logger.setLevel( logging.INFO )
    
    #read link to keep under control from a url file list
    if os.path.exists( 'url_list.txt' ):
        logging.info( "Found file" )
    else:
        f = open( 'url_list.txt','w' )
        f.write( "############Link list##############" )
        f.close()
        logging.info( "Created File" )
    
    #load link list
    links = None
    with open( "url_list.txt", "r" ) as f:
        links = [ x.rstrip() for x in f.readlines() ]
    
    logging.info( "URL load correctly" )
    #retrieve data from cardmarket page
    for link in links:
        pass
        #obtain data
        data = extractor( link )
        dataJson = transform_dict_value( data )
        #print( dataJson )
        
    #visualize data on terminal for testing
        folder_data_creation()
        
        filename=create_file_name(link)
        
        if check_if_file_exist(PATH, filename):
            #save information in the appropriate csv file
            add_row_to_csv(filename, dataJson)
            print("entra A")
        else:
            #create csv file and save information in the appropriate csv file
            create_csv_and_add_first_row(filename, dataJson)
            print("entra BB")

if __name__ == '__main__':
    run()
        

# TODO list
