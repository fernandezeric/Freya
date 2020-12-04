import os
import importlib
from Freya.files.verify_file import Verify
"""

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
        for catalog in self.catalogs:
            try :
                
                if Verify().verify_catalog_inside(catalog):
                    module = f'Freya.catalogs.{catalog}.configure'
                else :
                    module = f'LocalCatalogs.{catalog}.configure'

                mod = importlib.import_module(module) # import module
                class_ =  getattr(mod,f'Configure_{catalog}') # call class

                if call_method == 'get_lc_deg_all':
                    method_ = class_(ra = self.ra,
                                     dec = self.dec,
                                     radius = self.radius,
                                     format=self.format).get_lc_deg_all()# call method
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
               print(f'No find the catalog : {catalog}')

    def get_lc_deg_all(self):
        #self.generic_call_data('get_lc_deg_all')
        return self.generic_call_data('get_lc_deg_all')#self.dataReturn
    
    def get_lc_deg_nearest(self):
        return self.generic_call_data('get_lc_deg_nearest')

    def get_lc_hms_all(self):
        return self.generic_call_data('get_lc_hms_all')
    
    def get_lc_hms_nearest(self):
        return self.generic_call_data('get_lc_hms_nearest')

