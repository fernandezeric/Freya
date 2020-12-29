
from Freya.catalogs.PS1.methods import MethodsPS1 as mps1
from Freya.core.utils import Utils

class ConfigurePS1():

    def __init__(self,*args,**kwagrs):
        self.ra = kwagrs.get('ra')
        self.dec = kwagrs.get('dec')
        self.hms = kwagrs.get('hms')
        self.radius = kwagrs.get('radius')
        self.format = kwagrs.get('format')

    def get_lc_deg_all(self):
        data_return = mps1(ra=self.ra,dec=self.dec,radius=self.radius,format=self.format,nearest=False).ps1curves()
        return data_return

    def get_lc_hms_all(self):
        ra_,dec_ = Utils().hms_to_deg(self.hms)
        data_return = mps1(ra=ra_,dec=dec_,radius=self.radius,format=self.format,nearest=False).ps1curves()
        return data_return

    def get_lc_deg_nearest(self):
        data_return = mps1(ra=self.ra,dec=self.dec,radius=self.radius,format=self.format,nearest=True).ps1curves()
        return data_return

    def get_lc_hms_nearest(self):
        ra_,dec_ = Utils().hms_to_deg(self.hms)
        data_return = mps1(ra=ra_,dec=dec_,radius=self.radius,format=self.format,nearest=True).ps1curves()
        return data_return
