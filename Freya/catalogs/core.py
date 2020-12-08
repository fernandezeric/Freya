import os
import importlib
from Freya.files.verify_file import Verify
"""
Class to get data from module catalogue configured in Freya, first check if catalog exist inside Freya
and if not exist try import catalog from local folder. The data get is all ligh curve of object in area use
degrees (ra,dec,radius) or use the format hh:mm:ss (hh:mm:ss,radius).
Other option is get the only light curve of object most close to area selected.
"""
class GetData ():

    def __init__(self,**kwargs):
        self.catalogs = kwargs.get('catalogs').strip().split(",") #split catalogs in a list
        self.ra = kwargs.get('ra')
        self.dec = kwargs.get('dec')
        self.hms = kwargs.get('hms')
        self.radius = kwargs.get('radius')
        self.format = kwargs.get('format')
        self.dataReturn = {}

        if self.format not in ['csv']:
             return "inadmissible format in consult data"
    

    def generic_call_data(self,call_method):
        for catalogue in self.catalogs:
            try :
                """
                Search catalogue insiede Freya, if not exist search inside local folder.
                """
                if Verify().verify_catalog_inside(catalogue):
                    module = f'Freya.catalogs.{catalogue}.configure'
                elif Verify().verify_catalog_local(catalogue) :
                    module = f'LocalCatalogs.{catalogue}.configure'

                # Import catalogue
                mod = importlib.import_module(module)
                # Call class
                class_ =  getattr(mod,f'Configure_{catalogue}') 
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

                #self.dataReturn[f'{catalog}'] = method_
                return method_
            except :
                print(f'No find the catalog : {catalogue}')

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

