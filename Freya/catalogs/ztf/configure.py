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

from Freya.catalogs.ztf import methods

class Configure_ztf():

    def __init__(self,**kwagrs):
        self.ra = kwagrs.get('ra')
        self.dec = kwagrs.get('dec')
        self.hms = kwagrs.get('hms')
        self.radius = kwagrs.get('radius')
        self.format = kwagrs.get('format')

    def get_lc_deg_all(self):
        retorno = {'get_lc_deg_all' : {'ra':self.ra,'dec':self.dec,'radius':self.radius,'format':self.format,'chiki':'el mejor'}}
        return retorno

    def get_lc_hms_all(self):
        retorno = {'get_lc_hms_all' : {'hms':self.hms,'radius':self.radius,'format':self.format,'chiki':'genio'}}
        return retorno

    def get_lc_deg_nearest(self):
        retorno = {'get_lc_deg_nearest' : {'ra':self.ra,'dec':self.dec,'radius':self.radius,'format':self.format,'chiki':'podeoro'}}
        return retorno

    def get_lc_hms_nearest(self):
        retorno = {'get_lc_hms_nearest' : {'hms':self.hms,'radius':self.radius,'format':self.format,'chiki':'bestia'}}
        return retorno
