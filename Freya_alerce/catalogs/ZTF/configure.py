"""
configure.py is the most important file in Freya, this file is called for 
Freya’s core and FreyaAPI’s resources, is the only file you need to modify 
in principle. You need to complete the following methods. When using Freya’s 
method getData, you use this class for calls and depent what method call you 
need use ra and dec or hms, so that's why kwargs is used.
"""

from Freya_alerce.catalogs.ZTF.methods import MethodsZTF as mztf
from Freya_alerce.core.utils import Utils

class ConfigureZTF():
    """
    Parameters:
    ------------
    ra : (float) Right ascension
    dec :  (float) Declination
    hms : (string) HH:MM:SS
    radius: (float) Search radius
    format: (string) csv or votable
    """
    def __init__(self,**kwagrs):
        self.ra = kwagrs.get('ra')
        self.dec = kwagrs.get('dec')
        self.hms = kwagrs.get('hms')
        self.radius = kwagrs.get('radius')
        self.format = kwagrs.get('format')
        self.nearest = kwagrs.get('nearest')

    def get_lc_deg(self):
        """
        Return all ligth curves data or the most close object,inside degree area from ZTF catalog.
        """
        data_return = mztf(ra=self.ra,dec=self.dec,radius=self.radius,format=self.format,nearest=self.nearest).zftcurves() 
        return data_return
    
    def get_lc_hms(self):
        """Return all ligth curves data or the most close object, inside hh:mm:ss area from ZTF catalog"""
        ra_,dec_ = Utils().hms_to_deg(self.hms)
        data_return = mztf(ra=ra_,dec=dec_,radius=self.radius,format=self.format,nearest=self.nearest).zftcurves() 
        return data_return
