
from Freya.catalogs.ps1.methods import Methods_ps1 as mps1
from Freya.core.utils import Utils

class Configure_ps1():

    #poner init al generico, se repite mucho
    def __init__(self,*args,**kwagrs):
        self.ra = kwagrs.get('ra')
        self.dec = kwagrs.get('dec')
        self.hms = kwagrs.get('hms')
        self.radius = kwagrs.get('radius')
        self.format = kwagrs.get('format')

    def get_lc_deg_all(self):
        #retorno = {'get_lc_deg_all' : {'ra':ra,'dec':dec,'radius':radius,'format':format,'chiki':'el mejor'}}
        #return retorno
        data_return = mps1(self.ra,self.dec,self.radius,self.format,False).ps1curves()
        return data_return

    def get_lc_hms_all(self):
        #retorno = {'get_lc_hms_all' : {'hms':hms,'radius':radius,'format':format,'chiki':'genio'}}
        ra_,dec_ = Utils.hms_to_deg(self.hms)
        data_return = mps1(ra_,dec_,self.radius,self.format,False).ps1curves()
        return data_return

    def get_lc_deg_nearest(self):
        #retorno = {'get_lc_deg_nearest' : {'ra':ra,'dec':dec,'radius':radius,'format':format,'chiki':'podeoro'}}
        #return retorno
        data_return = mps1(self.ra,self.dec,self.radius,self.format,True).ps1curves()
        return data_return

    def get_lc_hms_nearest(self):
        #retorno = {'get_lc_hms_nearest' : {'hms':hms,'radius':radius,'format':format,'chiki':'bestia'}}
        ra_,dec_ = Utils.hms_to_deg(self.hms)
        data_return = mps1(ra_,dec_,self.radius,self.format,True).ps1curves()
        return data_return
