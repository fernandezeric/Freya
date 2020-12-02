"""
In this file you can created methods for 'configure.py'  
"""
import requests
import io
from Freya.core import utils as u

class Methods_NAME():

    def __init__(self,**kwagrs):
        self.ra = kwagrs.get('ra')
        self.dec = kwagrs.get('dec')
        self.hms = kwagrs.get('hms')
        self.radius = kwagrs.get('radius')
        self.format = kwagrs.get('format')

    def method_NAME():
        return 1

    def method_NAME_2():
        return 2
