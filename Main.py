from Models.DataBaseManipulation import *
from Models.GetField import *
from Models.CsvManipulation import *


def Main():
    
    #Requesting the input from user
    searchItem  = input("What are you looking for? ").replace(" ","-")

    #Retreiving all data from search
    item = GetField(searchItem=searchItem)      
    dataFrame = item.GetAllDataFrame()

    #saving into CSV
    csv = CsvManipulation(dataFrame,searchItem)
    csv.Save()

    #saving in DB
    db = DataBaseManipulation(searchItem.replace("-","_"),dataFrame)
    db.Save()
        

if __name__ == '__main__':
    Main()