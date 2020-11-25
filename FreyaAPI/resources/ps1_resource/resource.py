"""
Aqui va el resource como una clase que llama por tercera ves el mismo cochino metodo
"""
import sys
import importlib
from Freya.catalogs.ps1.configure import Configure_ps1
class Resource_ps1():

    def __init__(self,ra,dec,radius,format):
        self.ra = ra
        self.dec = dec
        self.radius = radius
        self.format = format
        
    def get_lc_deg_all(self):
        data_method = Configure_ps1(self.ra,self.dec,self.radius,self.format).get_lc_deg_all()
        return data_method

    def get_lc_hms_all(self):
        data_method = Configure_ps1(self.hms,self.radius,self.format).get_lc_hms_all()
        return data_method

    def get_lc_deg_nearest(self):
        data_method = Configure_ps1(self.ra,self.dec,self.radius,self.format).get_lc_deg_nearest()
        return data_method

    def get_lc_hms_nearest(self):
        data_method = Configure_ps1(self.hms,self.radius,self.format).get_lc_hms_nearest() 
        return data_method