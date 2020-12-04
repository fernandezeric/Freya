import sys
import importlib
from Freya.catalogs.core import GetData
class Resource_ztf_local():

    def __init__(self,**kwagrs):
        self.ra = kwagrs.get('ra')
        self.dec = kwagrs.get('dec')
        self.hms = kwagrs.get('hms')
        self.radius = kwagrs.get('radius')
        self.format = kwagrs.get('format')
        
    def get_lc_deg_all(self):
        data_method = GetData(catalogs='ztf_local',ra=self.ra,dec=self.dec,radius=self.radius,format=self.format).get_lc_deg_all()
        return data_method

    def get_lc_deg_nearest(self):
        data_method = GetData(catalogs='ztf_local',ra=self.ra,dec=self.dec,radius=self.radius,format=self.format).get_lc_deg_nearest()
        return data_method
    
    def get_lc_hms_all(self):
        data_method = GetData(catalogs='ztf_local',hms=self.hms,radius=self.radius,format=self.format).get_lc_hms_all()
        return data_method

    def get_lc_hms_nearest(self):
        data_method = GetData(catalogs='ztf_local',hms=self.hms,radius=self.radius,format=self.format).get_lc_hms_nearest() 
        return data_method
