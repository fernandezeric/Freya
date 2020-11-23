"""
Aqui va el resource como una clase que llama por tercera ves el mismo cochino metodo
"""
import sys
import importlib
from Freya.catalogs.ps1.configure import Configure_ps1
class Resource_ps1():

    def __init__(self,*args,**kwagrs):
        self.catalog = kwagrs.get('catalog') 
        self.ra = kwagrs.get('ra')
        self.dec = kwagrs.get('dec')
        self.hms = kwagrs.get('hms')
        self.radius = kwagrs.get('radius')
        self.format = kwagrs.get('format')
        
    def get_lc_deg_all(self):
        data_method = Configure_ps1().get_lc_deg_all(self.ra,self.dec,self.radius,self.format)
        return data_method

    def get_lc_hms_all(self):
        data_method = Configure_ps1().get_lc_hms_all(self.hms,self.radius,self.format)
        return data_method

    def get_lc_deg_nearest(self):
        data_method = Configure_ps1().get_lc_deg_nearest(self.ra,self.dec,self.radius,self.format)
        return data_method

    def get_lc_hms_nearest(self):
        data_method = Configure_ps1().get_lc_hms_nearest(self.hms,self.radius,self.format) 
        return data_method