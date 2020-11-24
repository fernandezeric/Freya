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

class Methods_zft():

    def __init__(self,**kwagrs):
        self.ra = kwagrs.get('ra')
        self.dec = kwagrs.get('dec')
        self.hms = kwagrs.get('hms')
        self.radius = kwagrs.get('radius')
        self.format = kwagrs.get('format')

    def id_nearest (ra,dec,radius,results):
        """ Get object id most closet to ra dec
        Parameters
        ----------
        """
        angle = []
        c1 = SkyCoord(ra=ra,dec=dec,unit=u.degree)
        for group in results.groups:
            c2 = SkyCoord(group['ra'][0],group['dec'][0],unit=u.degree)
            angle.append(c1.separation(c2))
        return angle.index(min(angle))

    def csv_format(ra,dec,radius,nearest,result):
        ztfdic = {}
        result = ascii.read(result.text)

        if len(result) <= 0:
            ztfdic['-1'] = 'not found' 
            return ztfdic # change to more general

        results = result.group_by('oid')

        #the most close object to radius
        if nearest is True:

            minztf = id_nearest(ra,dec,radius,results)
                
            buf = io.StringIO()
            ascii.write(results.groups[minztf],buf,format='csv')
            ztfdic[str(results.groups[minztf]['oid'][0])] =  buf.getvalue()
            return ztfdic

        # all objects in radius
        else:
            for group in results.groups:
                buf = io.StringIO()
                ascii.write(group,buf,format='csv')
                ztfdic[str(group['oid'][0])] =  buf.getvalue()
            return ztfdic

    def votable_format(ra,dec,radius,nearest,result):
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
                
            minztf = id_nearest(ra,dec,radius,tablas)

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

    def json_format(ra,dec,radius,nearest,result):
        ztfdic = {}
        result = ascii.read(result.text)

        if len(result) <= 0:
            ztfdic['-1'] = 'not found' 
            return ztfdic # change to more general

        results = result.group_by('oid')

        #the most close object to radius
        if nearest is True:

            minztf = id_nearest(ra,dec,radius,results)
                
            #buf = io.StringIO()
            #ascii.write(results.groups[minztf],buf,format='pandas.json')
            ztfdic[str(results.groups[minztf]['oid'][0])] =  results.groups[minztf].to_pandas().to_json()#buf.getvalue()
            return ztfdic

        # all objects in radius
        else:
            for group in results.groups:
                #buf = io.StringIO()
                #print(group.to_pandas().to_json())
                #buf.write(group,format='pandas.json', sep=' ', header=False)
                ztfdic[str(group['oid'][0])] =  group.to_pandas().to_json()#buf.getvalue()
            return ztfdic

    def zftcurves(ra,dec,radius,format,nearest):
        """ Get light curves of ztf objects 
        Parameters
        ----------
        """
        baseurl="https://irsa.ipac.caltech.edu/cgi-bin/ZTF/nph_light_curves"
        data = {}
        data['POS']=f'CIRCLE {ra} {dec} {radius}'
        #data['BANDNAME']='r'
        data['FORMAT'] = format
        #temporal
        if format == 'json':
            data['FORMAT'] = 'csv'
        result = requests.get(baseurl,params=data)
        ztfdic = {}

        if result.status_code != 200: 
            ztfdic['not found'] = result.status_code 
            return ztfdic #'not found' # change to more general
        
        #if select csv 
        elif format == 'csv':
            return csv_format(ra,dec,radius,nearest,result)

        # if select VOTable 
        elif format == 'votable':
            return votable_format(ra,dec,radius,nearest,result)
        
        #if select json
        elif format == 'json':
            return json_format(ra,dec,radius,nearest,result)