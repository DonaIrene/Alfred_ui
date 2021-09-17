import os
import shutil
import glob

source = 'C:\\Users\\lucas\\Downloads\\'
my_dirct = {
    'C:\\Users\\lucas\\Downloads\\Imagens': ['jpg','png','gif'],
    'C:\\Users\\lucas\\Downloads\\Zippadas': ['rar','zip','7z','tar'],
    'C:\\Users\\lucas\\Downloads\\Executavais': ['exe','msi'],
    'C:\\Users\\lucas\\Downloads\\PDF':['pdf','docx', 'doc', 'xls'],
    'C:\\Users\\lucas\\Downloads\\Musicas':['mp3','mp4'],
    'C:\\Users\\lucas\\Downloads\\Outros' : ['.rmskin']
}
for destination, extensions in my_dirct.items():
    for ext in extensions:
        for file in glob.glob(source + '*.' + ext):
            print (file)
            shutil.move(file, destination)

