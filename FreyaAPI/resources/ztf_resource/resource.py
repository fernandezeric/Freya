"""
Aqui va el resource como una clase que llama por tercera ves el mismo cochino metodo
"""

"""
https://stackoverflow.com/questions/4383571/importing-files-from-different-folder
otros hablan de PYTHONPATH
"""
import sys
sys.path.insert(0, '/home/jonimottg/Escritorio/Avance/') #arreglar esta cosa 
import importlib
#from Freya.catalogs.ztf import configure # este debiria esta traudo de fabrica #BUSCAR COMO CAMBIAR XXX CARACTERES POR YYY CARACTERES EN UN ARCHIVO
class resource():

    def __init__(self,*args,**kwagrs):
        self.catalog = kwagrs.get('catalog') 
        self.ra = kwagrs.get('ra')
        self.dec = kwagrs.get('dec')
        self.hms = kwagrs.get('hms')
        self.radius = kwagrs.get('radius')
        self.format = kwagrs.get('format')
        
    def get_lc_deg_all(self):
        module = f'Freya.catalogs.{self.catalog}.configure'
        mod = importlib.import_module(module)
        data_method = getattr(mod,'get_lc_deg_all')(self.ra,self.dec,self.radius,self.format)
        return data_method

    def get_lc_hms_all(hms,radius,format):
        module = f'Freya.catalogs.{self.catalog}.configure'
        mod = importlib.import_module(module)
        data_method = getattr(mod,'get_lc_hms_all')(self.hms,self.radius,self.format)
        return data_method

    def get_lc_deg_nearest(ra,dec,radius,format):
        module = f'Freya.catalogs.{self.catalog}.configure'
        mod = importlib.import_module(module)
        data_method = getattr(mod,'get_lc_deg_nearest')(self.ra,self.dec,self.radius,self.format)
        return data_method

    def get_lc_hms_nearest(hms,radius,format):
        module = f'Freya.catalogs.{self.catalog}.configure'
        mod = importlib.import_module(module)
        data_method = getattr(mod,'get_lc_hms_nearest')(self.hms,self.radius,self.format)
        return data_method