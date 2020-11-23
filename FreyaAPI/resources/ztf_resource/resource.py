"""
Aqui va el resource como una clase que llama por tercera ves el mismo cochino metodo
"""
import sys
import importlib
from Freya.catalogs.ztf.configure import Configure_ztf
class Resource_ztf():

    def __init__(self,**kwagrs):
        self.catalog = kwagrs.get('catalog') 
        self.ra = kwagrs.get('ra')
        self.dec = kwagrs.get('dec')
        self.hms = kwagrs.get('hms')
        self.radius = kwagrs.get('radius')
        self.format = kwagrs.get('format')
        
    def get_lc_deg_all(self):
        # module = f'Freya.catalogs.{self.catalog}.configure'
        # mod = importlib.import_module(module)
        # data_method = getattr(mod,'get_lc_deg_all')(self.ra,self.dec,self.radius,self.format)
        data_method = Configure_ztf().get_lc_deg_all(self.ra,self.dec,self.radius,self.format)
        return data_method

    def get_lc_hms_all(self):
        data_method = Configure_ztf().get_lc_hms_all(self.hms,self.radius,self.format)
        return data_method

    def get_lc_deg_nearest(self):
        data_method = Configure_ztf().get_lc_deg_nearest(self.ra,self.dec,self.radius,self.format)
        return data_method

    def get_lc_hms_nearest(self):
        data_method = Configure_ztf().get_lc_hms_nearest(self.hms,self.radius,self.format) 
        return data_method