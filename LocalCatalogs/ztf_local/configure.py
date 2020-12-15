
from LocalCatalogs.ztf_local.methods import Methods_ztf_local as mztf_local

class Configure_ztf_local():

    def __init__(self,**kwagrs):
        self.ra = kwagrs.get('ra')
        self.dec = kwagrs.get('dec')
        self.hms = kwagrs.get('hms')
        self.radius = kwagrs.get('radius')
        self.format = kwagrs.get('format')

    def get_lc_deg_all(self):
        data_return = mztf_local(ra=self.ra,dec=self.dec,radius=self.radius,format=self.format,nearest=False).zftcurves() 
        return data_return

    def get_lc_hms_all(self):
        data_return = mztf_local(hms=self.hms,radius=self.radius,format=self.format,nearest=False).zftcurves() 
        return data_return

    def get_lc_deg_nearest(self):
        data_return = mztf_local(ra=self.ra,dec=self.dec,radius=self.radius,format=self.format,nearest=True).zftcurves() 
        return data_return

    def get_lc_hms_nearest(self):
        data_return = mztf_local(hms=self.hms,radius=self.radius,format=self.format,nearest=True).zftcurves() 
        return data_return


