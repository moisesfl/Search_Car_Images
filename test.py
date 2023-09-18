import os
import shutil
import pandas as pd
import json

configFilePath = "./config.json"
rootPath = os.getcwd()
print(f'Directorio raíz: {rootPath}')
#imagesRootPath = "../Vehicles/" 

def readJSON (JSONFile):
    # Opening JSON file
    f = open(JSONFile)
    
    # returns JSON object as
    # a dictionary
    data = json.load(f)

    
    # Closing file
    f.close()
    return data["inputPath"]

def searchImages(excelListSEMCar, inputPath = "../Vehicles"):
    # np array to list
    excelListSEMCar = list(excelListSEMCar)
    # We go through all the directories
    for dayFolderName in os.listdir(inputPath):
        dayFolderPath = inputPath + dayFolderName
        print(f"Looking in the folder {dayFolderName}...")
        for carFolderName in os.listdir(dayFolderPath):
            carFolderPath = f"{dayFolderPath}/{carFolderName}"
            tempList = carFolderName.split("_")
            semFolder = tempList[1]
            # The list of NORES in excel has one more zero
            semFolderWithZero = semFolder[:5] + "0" + semFolder[5:]
            if (int(semFolderWithZero) in excelListSEMCar):
                # copy folder
                pathToCopy = f"{rootPath}/./MivieCars/{carFolderName}"
                if not (os.path.exists(pathToCopy)):
                    shutil.copytree(f"{carFolderPath}", pathToCopy)
                    # delete element list
                    excelListSEMCar.remove(int(semFolderWithZero))
                    print (f"   Mivie car with SEM {semFolder} found!")
                else:
                    print(f"    SEM {semFolder} not copied! The folder already exists!")
                    continue

    print ("Finished car search!")
    
    # for VIScar in excelListSEMCar:
    #     print(VIScar)

try:
    inputPath= readJSON(configFilePath)
    # We define a list with the columns we want to read
    useCols = ['VIS', 'SEM']
    df = pd.read_excel('Listado K9 mivie.xls', usecols=useCols)

    # We pass as argument the list of values of the SEM column
    searchImages(df['SEM'].values, inputPath)
    print("Finish script!")
    
    
except Exception as e:
    print("Error: " , e)

input();