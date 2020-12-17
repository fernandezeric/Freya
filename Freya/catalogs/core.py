import os
import importlib
from Freya.files.verify_file import Verify

"""
Class to get data from module catalog configured in Freya, first check if catalog exist inside Freya
and if not exist try import catalog from local folder. The data get is all ligh curve of object in area use
degrees (ra,dec,radius) or use the format hh:mm:ss (hh:mm:ss,radius).
Other option is get the only light curve of object most close to area selected.
"""
class GetData ():
    """
    Parameters
    --------------------------------------
    ra (float): (degrees) Right Ascension
    dec (float): (degrees) Declination
    hms (string): format hh:mm:ss
    radius (float): Search radius
    format (string): csv,
    """

    def __init__(self,**kwargs):
        self.catalog = kwargs.get('catalog').strip()
        self.ra = kwargs.get('ra')
        self.dec = kwargs.get('dec')
        self.hms = kwargs.get('hms')
        self.radius = kwargs.get('radius')
        self.format = kwargs.get('format')

        if self.format not in ['csv','votable']:
             return "inadmissible format in consult data"
    

    def generic_call_data(self,call_method):
        # try :
        """
        Search catalog insiede Freya, if not exist search inside local folder.
        """
        if Verify().verify_catalog_inside(self.catalog):
            module = f'Freya.catalogs.{self.catalog}.configure'
        elif Verify().verify_catalog_local(self.catalog) :
            module = f'LocalCatalogs.{self.catalog}.configure'
        elif Verify().verify_catalog_local_(self.catalog):
            module = f'{self.catalog}.configure'

        # Import self.catalog
        mod = importlib.import_module(module)
        # Call class
        class_ =  getattr(mod,f'Configure_{self.catalog}') 
        # Call method especific of class
        if call_method == 'get_lc_deg_all':
            method_ = class_(ra = self.ra,
                                dec = self.dec,
                                radius = self.radius,
                                format=self.format).get_lc_deg_all()
        elif call_method == 'get_lc_deg_nearest':
            method_ = class_(ra = self.ra,
                                dec = self.dec,
                                radius = self.radius,
                                format=self.format).get_lc_deg_nearest()
        
        elif call_method == 'get_lc_hms_all':
            method_ = class_(hms = self.hms,
                                radius = self.radius,
                                format = self.format).get_lc_hms_all()
        
        elif call_method == 'get_lc_hms_nearest':
            method_ = class_(hms = self.hms,
                                radius = self.radius,
                                format = self.format).get_lc_hms_nearest()
        return method_
        # except :
        #     print(f'No find the catalog : {self.catalog}')

    # Return all light curve object in degrees area
    def get_lc_deg_all(self):
        return self.generic_call_data('get_lc_deg_all')
    # Return the light curve most close to degrees area
    def get_lc_deg_nearest(self):
        return self.generic_call_data('get_lc_deg_nearest')
    # Return all light curve object in hh:mm:ss area
    def get_lc_hms_all(self):
        return self.generic_call_data('get_lc_hms_all')
    # Return the light curve most close to hh:mm:ss area
    def get_lc_hms_nearest(self):
        return self.generic_call_data('get_lc_hms_nearest')

Data = GetData(catalog='ztf',hms='9h17m20.26793280000689s +4h34m32.414496000003936s',radius=0.00356,format='csv').get_lc_hms_nearest()
#Data = GetData(catalog='ps1',ra=139.33444972,dec=68.6350604,radius=0.00356,format='csv').get_lc_deg_all()
#print(Data)