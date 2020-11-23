"""
Cambiar todo esto y dejarlo creando archivos bonitos con un poco de contenido
"""
import fileinput #replace into files
import Freya.catalogs # __path__
import os

class Files():
    """
    Replace a word for new word in specific file
    """
    def __init__(self,paths,raplace_word,word):
        self.list_path = paths
        self.replace_word = raplace_word
        self.word = word

    def replace_in_files(self):
        # print(self.list_path)
        # print(self.replace_word)
        # print(self.word)
        for file in self.list_path:
            with fileinput.FileInput(f'{file}', inplace=True) as file_:
                for line in file_:
                    print(line.replace(f'{self.replace_word}', f'{self.word}'), end='')


class Cheak():

    def cheak_catalog(self,name):
        self.name = name
        dir_catalogs = Freya.catalogs.__path__[0] # dir modules
        if self.name  in os.listdir(dir_catalogs) :
             return True 
        return False
