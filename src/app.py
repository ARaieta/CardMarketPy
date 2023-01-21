import os
import logging
from core import *
#OPTIONAL read file from config file


if __name__ == '__main__':
    
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
    print( links )
    for link in links:
        pass
        #obtain data
        data = extractor( link )
        dataJson = transform_dict_value( data )
        #print( dataJson )
        
    #visualize data on terminal for testing
        for k,v in dataJson.items():
            print(k, v)
        
        print("----------------")    
    #save information in the appropriate csv file 
        # or create csv file and save information in the appropriate csv file