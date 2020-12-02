import os
import importlib
"""

"""
class GetData ():

    def __init__(self,format='csv',**kwargs):
        self.catalogs = kwargs.get('catalogs').strip().split(",") #split catalogs in a list # cheack with use post and not get method
        self.ra = kwargs.get('ra')
        self.dec = kwargs.get('dec')
        self.hms = kwargs.get('hms')
        self.radius = kwargs.get('radius')
        self.format = format
        self.dataReturn = {}

        if self.format in ['csv']:
             raise TypeError("inadmissible format in consult data")

    def get_lc_deg_all(self):
        for catalog in self.catalogs:
            try :
                module = f'Freya.catalogs.{catalog}.configure'
                mod = importlib.import_module(module) # import module
                class_ =  getattr(mod,f'Configure_{catalog}') # call class
                method_ = class_(ra = self.ra,dec = self.dec,
                                radius = self.radius,format=self.format).get_lc_deg_all()# call method
                self.dataReturn[f'{catalog}'] = method_
            except :
               print(f'No find the catalog : {catalog}')

        return self.dataReturn
    
    def get_lc_deg_nearest(self):
        for catalog in self.catalogs:
            try :
                module = f'Freya.catalogs.{catalog}.configure'
                mod = importlib.import_module(module) # import module
                class_ =  getattr(mod,f'Configure_{catalog}') # call class
                method_ = class_(ra = self.ra,dec = self.dec,
                                radius = self.radius,format=self.format).get_lc_deg_nearest()
                self.dataReturn[f'{catalog}'] = method_
            except :
                print(f'No find the catalog : {catalog}')

        return self.dataReturn

    def get_lc_hms_all(self):
        for catalog in self.catalogs:
            try :
                module = f'Freya.catalogs.{catalog}.configure'
                mod = importlib.import_module(module) # import module
                class_ =  getattr(mod,f'Configure_{catalog}') # call class
                method_ = class_(hms = self.hms,radius = self.radius,format = self.format).get_lc_hms_all()
                self.dataReturn[f'{catalog}'] = method_
            except :
                print(f'No find the catalog : {catalog}')

        return self.dataReturn
    
    def get_lc_hms_nearest(self):
        for catalog in self.catalogs:
            try :
                module = f'Freya.catalogs.{catalog}.configure'
                mod = importlib.import_module(module) # import module
                class_ =  getattr(mod,f'Configure_{catalog}') # call class
                method_ = class_(hms = self.hms,radius = self.radius,format = self.format).get_lc_hms_nearest()
                self.dataReturn[f'{catalog}'] = method_
            except :
                print(f'No find the catalog : {catalog}')

        return self.dataReturn

