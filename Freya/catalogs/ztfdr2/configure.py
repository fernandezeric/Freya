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

from Freya.catalogs.ztfdr2 import methods

class Configure_ztfdr2():

    def get_lc_deg_all(ra,dec,radius,format):
        retorno = {'get_lc_deg_all' : {'ra':ra,'dec':dec,'radius':radius,'format':format,'chiki':'el mejor'}}
        return retorno

    def get_lc_hms_all(hms,radius,format):
        retorno = {'get_lc_hms_all' : {'hms':hms,'radius':radius,'format':format,'chiki':'genio'}}
        return retorno

    def get_lc_deg_nearest(ra,dec,radius,format):
        retorno = {'get_lc_deg_nearest' : {'ra':ra,'dec':dec,'radius':radius,'format':format,'chiki':'podeoro'}}
        return retorno

    def get_lc_hms_nearest(hms,radius,format):
        retorno = {'get_lc_hms_nearest' : {'hms':hms,'radius':radius,'format':format,'chiki':'bestia'}}
        return retorno
