"""
Need with you return method as follow : 

"""

from Freya.catalogs.ZTF.methods import MethodsZTF as mztf
from Freya.core.utils import Utils

class ConfigureZTF():

    def __init__(self,**kwagrs):
        self.ra = kwagrs.get('ra')
        self.dec = kwagrs.get('dec')
        self.hms = kwagrs.get('hms')
        self.radius = kwagrs.get('radius')
        self.format = kwagrs.get('format')

    def get_lc_deg_all(self):
        data_return = mztf(ra=self.ra,dec=self.dec,radius=self.radius,format=self.format,nearest=False).zftcurves() 
        return data_return

    def get_lc_hms_all(self):
        ra_,dec_ = Utils().hms_to_deg(self.hms)
        data_return = mztf(ra=ra_,dec=dec_,radius=self.radius,format=self.format,nearest=False).zftcurves() 
        return data_return

    def get_lc_deg_nearest(self):
        data_return = mztf(ra=self.ra,dec=self.dec,radius=self.radius,format=self.format,nearest=True).zftcurves() 
        return data_return

    def get_lc_hms_nearest(self):
        ra_,dec_ = Utils().hms_to_deg(self.hms)
        data_return = mztf(ra=ra_,dec=dec_,radius=self.radius,format=self.format,nearest=True).zftcurves() 
        return data_return