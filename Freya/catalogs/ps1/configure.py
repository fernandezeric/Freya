
from Freya.catalogs.ps1.methods import Methods_ps1 as mps1

class Configure_ps1():

    #poner init al generico, se repite mucho
    def __init__():
        pass

    def get_lc_deg_all(self,ra,dec,radius,format):
        #retorno = {'get_lc_deg_all' : {'ra':ra,'dec':dec,'radius':radius,'format':format,'chiki':'el mejor'}}
        #return retorno
        self.ra = ra
        self.dec = dec
        self.radius = radius
        self.format = format
        self.nearest = False
        data_return = mps1(self.ra,self.dec,self.radius,self.format,self.nearest).ps1curves()
        return data_return

    def get_lc_hms_all(self,hms,radius,format):
        retorno = {'get_lc_hms_all' : {'hms':hms,'radius':radius,'format':format,'chiki':'genio'}}
        return retorno

    def get_lc_deg_nearest(self,ra,dec,radius,format):
        #retorno = {'get_lc_deg_nearest' : {'ra':ra,'dec':dec,'radius':radius,'format':format,'chiki':'podeoro'}}
        #return retorno
        self.ra = ra
        self.dec = dec
        self.radius = radius
        self.format = format
        self.nearest = False
        data_return = mps1(self.ra,self.dec,self.radius,self.format,self.nearest).ps1curves()
        return data_return

    def get_lc_hms_nearest(self,hms,radius,format):
        retorno = {'get_lc_hms_nearest' : {'hms':hms,'radius':radius,'format':format,'chiki':'bestia'}}
        return retorno
