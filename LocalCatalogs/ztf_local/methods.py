"""
In this file you can created methods for 'configure.py'  
"""
import requests
import io
from Freya.core import utils as u

class Methods_ztf_local():

    def __init__(self,**kwagrs):
        self.ra = kwagrs.get('ra')
        self.dec = kwagrs.get('dec')
        self.hms = kwagrs.get('hms')
        self.radius = kwagrs.get('radius')
        self.format = kwagrs.get('format')

    def method_ztf_local():
        return 1

    def method_ztf_local_2():
        return 2
