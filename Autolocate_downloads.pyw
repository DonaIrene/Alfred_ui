import os
import shutil
import glob
import time
from unittest.mock import patch

#Directorio padrao do file
source = 'C:\\Users\\Pao_de_Queijo\\Downloads\\'
newSource = 'C:\\Users\\Pao_de_Queijo\\Downloads'


#Pastas destino dos downloaded files (ou outros)
my_dirct = {
    'D:\\Tokio_School\\Python\\' : ['ipynb'],
    f'{newSource}\\Imagens': ['jpg','png','gif','jpeg'],
    f'{newSource}\\Zippadas': ['rar','zip','7z','tar'],
    f'{newSource}\\Executaveis': ['exe','msi'],
    f'{newSource}\\PDF':['pdf','docx', 'doc', 'xls','txt'],
    f'{newSource}\\Musicas':['mp3','mp4'],
    f'{newSource}\\Torrent' : ['torrent'],
    #Aconselhavel deixar (outros) no final do set, pois pode criar conflito ao mover ficheiros#
    f'{newSource}\\Outros' : ['rmskin','dll','jar','properties','bat'],
}

#verificicacao do file e do seu tipo 
for i in range(4320):
    for destination, extensions in my_dirct.items():
        for ext in extensions:
            for file in glob.glob(source + '*.' + ext):
                print (file)
                shutil.move(file, destination)
    time.sleep(180)
