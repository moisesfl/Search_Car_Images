import os
import shutil
import pandas as pd


rootPath = os.getcwd()
print(f'Directorio raíz: {rootPath}')
imagesRootPath = "C:/CIA/proba/"


def searchImages(excelListSEMCar):
    excelListSEMCar = list(excelListSEMCar)
    for dayFolderName in os.listdir(imagesRootPath):
        dayFolderPath = imagesRootPath + dayFolderName
        for carFolderName in os.listdir(dayFolderPath):
            carFolderPath = f"{dayFolderPath}/{carFolderName}"
            tempList = carFolderName.split("_")
            semFolder = tempList[1]

            semFolderWithCero = semFolder[:5] + "0" + semFolder[5:]
            print(semFolder)
            if (int(semFolderWithCero) in excelListSEMCar):
                print(f"Encontrado SEM: {semFolder}")
                # copiar carpeta e eliminar da lista excelListSEMCar
                pathToCopy = f"{rootPath}/./MivieCars/{carFolderName}"
                if not (os.path.exists(pathToCopy)):
                    shutil.copytree(f"{carFolderPath}",
                                    pathToCopy)
                    # delete element array
                    # no doy eliminado el elemento correspondiente
                    excelListSEMCar.remove(int(semFolderWithCero))

                else:
                    print("No copiado!Ya existe la carpeta!")
                    continue
            print(carFolderPath + "  SEM:" + tempList[1])

    for VIScar in excelListSEMCar:
        print(VIScar)


# Definimos una lista con las columnas que queremos leer
useCols = ['VIS', 'SEM']
df = pd.read_excel('App_test/Listado K9 mivie.xls', usecols=useCols)
# # print (df)
# lista = list[df]
# # for car in df['VIS'].values:
# #     print (car)
# Pasamos como argumemto la lista de valores de la columna SEM
searchImages(df['SEM'].values)
