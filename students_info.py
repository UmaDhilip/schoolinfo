import pymongo
import json
import pandas as pd

import logging
import custlogger

split_file = __file__.split('\\')[-1]
(filename,ext) = split_file.split('.')
ext=".log"
fname = filename+ext
print(fname)

log = custlogger.create_logger(filename=fname,loglevel=logging.WARNING)

def open_connection():
    ''' Open the pymongo connection '''  
    
    clientObj = pymongo.MongoClient('mongodb://127.0.0.1:27017')
    dbObj = clientObj["school"]
    collObj = dbObj['schoolinfo']

    return(dbObj,collObj)
        

def read_input(dbObj, collObj):

    with open("C:\\Users\\mahii\Project\\schoolinfo\\school_info.json","r") as fileData:

        records = json.load(fileData)
        log.info(records)
        
        if isinstance(records, list):
            #collObj.insert_many(records)
            log.info("Records are successfully inserted inside the Mongo DB")

def main():
    dbObj,collObj = open_connection()
    read_input(dbObj,collObj)    


if __name__ == '__main__':
    main()

