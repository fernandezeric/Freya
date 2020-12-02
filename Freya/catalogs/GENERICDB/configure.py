"""
Need with you return method as follow : 

{
    'id_1' : 'data_1',
    'id_2' : 'data_2',
    .
    .
    .
    'id_n' : 'data_n'
}
"""

from Freya.catalogs.NAME.methods import Methods_NAME as mNAME

class Configure_NAME():

    def __init__(self,**kwagrs):
        self.ra = kwagrs.get('ra')
        self.dec = kwagrs.get('dec')
        self.hms = kwagrs.get('hms')
        self.radius = kwagrs.get('radius')
        self.format = kwagrs.get('format')

    def get_lc_deg_all(self):
        data_return = mNAME(ra=self.ra,dec=self.dec,radius=self.radius,format=self.format,nearest=False).zftcurves() 
        return data_return

    def get_lc_hms_all(self):
        data_return = mNAME(hms=self.hms,radius=self.radius,format=self.format,nearest=False).zftcurves() 
        return data_return

    def get_lc_deg_nearest(self):
        data_return = mNAME(ra=self.ra,dec=self.dec,radius=self.radius,format=self.format,nearest=True).zftcurves() 
        return data_return

    def get_lc_hms_nearest(self):
        data_return = mNAME(hms=self.hms,radius=self.radius,format=self.format,nearest=True).zftcurves() 
        return data_return

