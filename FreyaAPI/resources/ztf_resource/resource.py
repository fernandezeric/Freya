"""
"""
import sys
import importlib
#from Freya.catalogs.ztf.configure import Configure_ztf
from Freya.catalogs.core import GetData
class Resource_ztf():

    def __init__(self,**kwagrs):
        self.ra = kwagrs.get('ra')
        self.dec = kwagrs.get('dec')
        self.hms = kwagrs.get('hms')
        self.radius = kwagrs.get('radius')
        self.format = kwagrs.get('format')
        
    def get_lc_deg_all(self):
        #data_method = Configure_ztf(ra=self.ra,dec=self.dec,radius=self.radius,format=self.format).get_lc_deg_all()
        #return data_method
        data_method = GetData(catalogs='ztf',ra=self.ra,dec=self.dec,radius=self.radius,format=self.format).get_lc_deg_all()
        return data_method

    def get_lc_hms_all(self):
        data_method = GetData(catalogs='ztf',hms=self.hms,radius=self.radius,format=self.format).get_lc_hms_all()
        return data_method

    def get_lc_deg_nearest(self):
        data_method = GetData(catalogs='ztf',ra=self.ra,dec=self.dec,radius=self.radius,format=self.format).get_lc_deg_nearest()
        return data_method

    def get_lc_hms_nearest(self):
        data_method = GetData(catalogs='ztf',hms=self.hms,radius=self.radius,format=self.format).get_lc_hms_nearest() 
        return data_method