#
# ## PROBAR
#
from astropy.coordinates import SkyCoord

class Utils:

    def deg_to_hms(self):
        """
        porque alguien aria esto? ni idea, buscarlo
        """
        pass

    def hms_to_deg(self,hms):
        """
        coord = SkyCoord(request.form['hms'],frame='icrs') #transform coord
        ra = coord.ra.degree
        dec = coord.dec.degree
        """
        coord = SkyCoord(hms,frame='icrs') #transform coord
        ra = coord.ra.degree
        dec = coord.dec.degree
        return ra,dec

    def nearest(self):
        pass

