"""
Cambiar todo esto y dejarlo creando archivos bonitos con un poco de contenido
"""

class ListFile():

    def __init__(self,indicar):
        self.indicar = indicar
        self.list_a = ['__init__','methods','configure','connect_bd']
        self.list_b = ['__init__','methods','configure']

    def get_name_files(self):
        if self.indicar != 'api':
            return self.list_a
        else :
            return self.list_b