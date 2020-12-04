"""
In this file you can created methods for 'configure.py'  
"""
import requests
import io
from Freya.core import utils as u
import pandas
from astropy.io import ascii
from astropy.coordinates import SkyCoord
from astropy import units as u
from astropy.io.votable import parse,parse_single_table,from_table, writeto

class Methods_ztf_local():
    
    def __init__(self,**kwagrs):
        self.ra = kwagrs.get('ra')
        self.dec = kwagrs.get('dec')
        self.hms = kwagrs.get('hms')
        self.radius = kwagrs.get('radius')
        self.format = kwagrs.get('format')
        self.nearest = kwagrs.get('nearest')

    def id_nearest (self,results):
        """ Get object id most closet to ra dec use a min angle
        Parameters
        ----------
        """
        angle = []
        c1 = SkyCoord(ra=self.ra,dec=self.dec,unit=u.degree)
        for group in results.groups:
            c2 = SkyCoord(group['ra'][0],group['dec'][0],unit=u.degree)
            angle.append(c1.separation(c2))
        return angle.index(min(angle))

    def csv_format(self,result):
        ztfdic = {}
        result_ = ascii.read(result.text)
        if len(result_) <= 0:
            ztfdic['-999'] = 'light curve not found' 
            return ztfdic

        result_ = result_.group_by('oid')
        #the most close object to radius
        if self.nearest is True:

            minztf = self.id_nearest(result_)
                
            buf = io.StringIO()
            ascii.write(result_.groups[minztf],buf,format='csv')
            ztfdic[str(result_.groups[minztf]['oid'][0])] =  buf.getvalue()
            return ztfdic

        # all objects in radius
        else:
            for group in result_.groups:
                buf = io.StringIO()
                ascii.write(group,buf,format='csv')
                ztfdic[str(group['oid'][0])] =  buf.getvalue()
            return ztfdic

    def votable_format(self,result):
        ztfdic = {}
        votable = result.text.encode(encoding='UTF-8')
        bio = io.BytesIO(votable)
        votable = parse(bio)
        table = parse_single_table(bio).to_table()

        if len(table) <= 0:
            ztfdic['0'] = 'not found' 
            return ztfdic #'not found'

        tablas = table.group_by('oid')

        #the most close object to radius
        if nearest is True:
                
            minztf = self.id_nearest(tablas)

            buf = io.BytesIO()
            votable = from_table(tablas.groups[minztf])
            writeto(votable,buf)
            ztfdic[str(tablas.groups[minztf]['oid'][0])] = (buf.getvalue().decode("utf-8"))
            return ztfdic
        # all objects in radius
        else :
            for group in tablas.groups:
                buf = io.BytesIO()
                votable = from_table(group)
                writeto(votable,buf)
                ztfdic[str(group['oid'][0])] = (buf.getvalue().decode("utf-8"))
            return ztfdic

    def zftcurves(self):
        """ Get light curves of ztf objects 
        Parameters
        ----------
        """
        baseurl="https://irsa.ipac.caltech.edu/cgi-bin/ZTF/nph_light_curves"
        data = {}
        data['POS']=f'CIRCLE {self.ra} {self.dec} {self.radius}'
        #data['BANDNAME']='r'
        data['FORMAT'] = self.format
        result = requests.get(baseurl,params=data)
        ztfdic = {}
        #self.csv_format(result)
        #return result
        if result.status_code != 200: 
            ztfdic['error code status'] = result.status_code 
            return ztfdic
        #if select csv 
        if self.format == 'csv':
            return self.csv_format(result)
        # # if select VOTable 
        # elif self.format == 'votable':
        #     return self.votable_format(result)
