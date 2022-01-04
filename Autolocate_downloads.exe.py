import os
import shutil
import glob

#Directorio padrao do file
source = 'C:\\Users\\Pao_de_Queijo\\Downloads\\'

#Pastas destino dos downloaded files (ou outros)
my_dirct = {
    'D:\\Tokio_School\\Python\\' : ['ipynb'],
    'C:\\Users\\Pao_de_Queijo\\Downloads\\Imagens': ['jpg','png','gif','jpeg'],
    'C:\\Users\\Pao_de_Queijo\\Downloads\\Zippadas': ['rar','zip','7z','tar'],
    'C:\\Users\\Pao_de_Queijo\\Downloads\\Executaveis': ['exe','msi'],
    'C:\\Users\\Pao_de_Queijo\\Downloads\\PDF':['pdf','docx', 'doc', 'xls','txt'],
    'C:\\Users\\Pao_de_Queijo\\Downloads\\Musicas':['mp3','mp4'],
    'C:\\Users\\Pao_de_Queijo\\Downloads\\Torrent' : ['torrent'],

    #Aconselhavel deixar (outros) no final do set, pois pode criar conflito ao mover ficheiros#
    'C:\\Users\\Pao_de_Queijo\\Downloads\\Outros' : ['rmskin','dll','ini','jar','properties','bat'],
}
#verificicacao do file e do seu tipo 
for destination, extensions in my_dirct.items():
    for ext in extensions:
        for file in glob.glob(source + '*.' + ext):
            print (file)
            shutil.move(file, destination)
