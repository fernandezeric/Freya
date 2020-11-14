# habria que ponerla manual
#from Freya.catalogs.ztf import configure as ztf
#from Freya.catalogs.ps1 import configure as ps1
#import Freya.catalogs
import os
import importlib
"""

"""
class GetData ():

    def __init__(self,nearest=False,format='csv',**kwargs):
        #crear algo que haga cheak a las variables, de quien es responsabilidad?
        self.catalogs = kwargs.get('catalogs').strip().split(",") #separa los catalogos en un array

        self.ra = kwargs.get('ra')
        self.dec = kwargs.get('dec')
        self.hms = kwargs.get('hms')
        self.radius = kwargs.get('radius')

        self.format = format
        self.nearest = nearest

        self.dataReturn = {}
        #print(self.catalogs)
        # Esto podría estar separado uno en cada archivo, si se quiere más generalidad.
    """
        module = f'resources.{catalog}_resource.resource'
        mod = importlib.import_module(module)
        my_class = getattr(mod, 'resource')
        my_instance = my_class().get_lc_deg_all()
    """   
    def get_lc_deg_all(self):
        for catalog in self.catalogs:
            try :
                """ Formabruta
                module = __import__(f'Freya.catalogs.{catalog}.configure',fromlist=['object'])
                data = getattr(module, 'get_lc_deg_all')(self.ra,self.dec,self.radius,self.format)
                """
                module = f'Freya.catalogs.{catalog}.configure'
                mod = importlib.import_module(module)
                data_method = getattr(mod,'get_lc_deg_all')(self.ra,self.dec,self.radius,self.format)
                self.dataReturn[f'{catalog}'] = data_method
            except :
                print(f'No se ha encontrado el siguiente catalogo : {catalog}')

        return self.dataReturn
    
    def get_lc_deg_nearest(self):
        for catalog in self.catalogs:
            try :
                module = f'Freya.catalogs.{catalog}.configure'
                mod = importlib.import_module(module)
                data_method = getattr(mod,'get_lc_deg_nearest')(self.ra,self.dec,self.radius,self.format)
                self.dataReturn[f'{catalog}'] = data_method
            except :
                print(f'No se ha encontrado el siguiente catalogo : {catalog}')

        return self.dataReturn

    def get_lc_hms_all(self):
        for catalog in self.catalogs:
            try :
                module = f'Freya.catalogs.{catalog}.configure'
                mod = importlib.import_module(module)
                data_method = getattr(mod,'get_lc_hms_all')(self.hms,self.radius,self.format)
                self.dataReturn[f'{catalog}'] = data_method
            except :
                print(f'No se ha encontrado el siguiente catalogo : {catalog}')

        return self.dataReturn
    
    def get_lc_hms_nearest(self):
        for catalog in self.catalogs:
            try :
                module = f'Freya.catalogs.{catalog}.configure'
                mod = importlib.import_module(module)
                data_method = getattr(mod,'get_lc_hms_nearest')(self.hms,self.radius,self.format)
                self.dataReturn[f'{catalog}'] = data_method
            except :
                print(f'No se ha encontrado el siguiente catalogo : {catalog}')

        return self.dataReturn

