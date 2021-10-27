import os
import shutil
import glob

source = 'C:\\Users\\Lucas Costa\\Downloads\\'
my_dirct = {
    'C:\\Users\\Lucas Costa\\Downloads\\Imagens': ['jpg','png','gif'],
    'C:\\Users\\Lucas Costa\\Downloads\\Zippadas': ['rar','zip','7z','tar'],
    'C:\\Users\\Lucas Costa\\Downloads\\Executaveis': ['exe','msi'],
    'C:\\Users\\Lucas Costa\\Downloads\\PDF':['pdf','docx', 'doc', 'xls'],
    'C:\\Users\\Lucas Costa\\Downloads\\Musicas':['mp3','mp4'],
    'C:\\Users\\Lucas Costa\\Downloads\\Outros' : ['.rmskin']
}
for destination, extensions in my_dirct.items():
    for ext in extensions:
        for file in glob.glob(source + '*.' + ext):
            print (file)
            shutil.move(file, destination)
