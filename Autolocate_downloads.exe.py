import os
import shutil
import glob

source = 'C:\\Users\\Pao_de_Queijo\\Downloads\\'
my_dirct = {
    'C:\\Users\\Pao_de_Queijo\\Downloads\\Imagens': ['jpg','png','gif'],
    'C:\\Users\\Pao_de_Queijo\\Downloads\\Zippadas': ['rar','zip','7z','tar'],
    'C:\\Users\\Pao_de_Queijo\\Downloads\\Executaveis': ['exe','msi'],
    'C:\\Users\\Pao_de_Queijo\\Downloads\\PDF':['pdf','docx', 'doc', 'xls','txt'],
    'C:\\Users\\Pao_de_Queijo\\Downloads\\Musicas':['mp3','mp4'],
    'C:\\Users\\Pao_de_Queijo\\Downloads\\Outros' : ['rmskin','dll','ini','jar','properties','bat'],
    'C:\\Users\\Pao_de_Queijo\\Downloads\\Torrent' : ['torrent']
}
for destination, extensions in my_dirct.items():
    for ext in extensions:
        for file in glob.glob(source + '*.' + ext):
            print (file)
            shutil.move(file, destination)
