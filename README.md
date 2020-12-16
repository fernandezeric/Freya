# GO GO MEMORI2 [Pensando que esta solamente Freya]
### Here it is the module python catalog 'Freya'.
Freya is a Fremework <3, and this github is the python code.

# Start (Commands CLI). 🚀
With Freya get light curve data is more simple.
Have option by CLI 'freya-admin', the options are:
  
  * Creates new catalog who module inside Freya, where name is the name of catalog what choose and source
  is where it comes from (available options: api,db).
  ```
  freya-admin --newcatalog <name> <source>
  ```
  * Creates new api called FreyaAPI in path with call freya-admin, this opcion create a new flask application with
  all rutes necessaries.
  ```
  freya-admin --newapi
  ```
  * Add new resource in FreyaAPI, but first need whit catalog exist in Freya or local folder and the call --addresource
  inside the folder FreyaAPI.
  ```
  freya-admin --addresource <name> 
  ```
  * You can creates local catalgos but first need create new folder, this call creates new local folder in path with call freya-admin, 
  and register path in sys.
  ```
  freya-admin --newfolderlocal
  ```
  * And want creates new catalog who module in local folder, need call --newcataloglocal inside the folder created with --newfolderlocal.
  where name is the name of catalog what choose and source is where it comes from (available options: api,db).
  ```
  freya-admin --newcataloglocal <name> <source>
  ```
  * If you download any catalog and want need rapid register, can use --registercatalog. This method register path of local 
  catalog for use need call inside catalog folder (register in sys python).
  ```
  freya-admin --registercatalog
  ```

# Install Freya. 🔧
First clone repository.
```
pip install . 

```
## Add new catalogs in Freya or local folders. 🔧
* If you want add modules catalogs inside Freya use for example:
```
freya-admin --newcatalog ztf api

```
* If you want use local folder and add new catalogs inside use for example:
```
# In any place of you system
freya-admin --newlocalfolder

# Inside local folder catalogs
freya-admin --newcataloglocal ztf_local api

```
* If you download any catalog for the github or other site use for example:
```
# Inside catalog
freya-admin --registercatalog

```

Independet how add catalog the next step is to connect catalog with Freya,
for this need completed fourt generic methods.
```
Inside folder new catalog find the following files
- configure.py
- methods.py 
- connect.py (if source is 'db') 

now inside 'configure.py' it find 

  - def get_lc_deg_all()

  - def get_lc_hms_all()

  - def get_lc_deg_nearest()

  - def get_lc_hms_nearest()

This methods need completed and return csv data 
with ligth curves.

Opcional you can use 'methods.py' for not overburden 'configure.py'
```
* For example default catalog ztf inside in Freya. 

'~/Freya/catalogs/ztf/configure.py'
```python

from Freya.catalogs.ztf.methods import Methods_ztf as mztf

class Configure_ztf():

    def __init__(self,**kwagrs):
        self.ra = kwagrs.get('ra')
        self.dec = kwagrs.get('dec')
        self.hms = kwagrs.get('hms')
        self.radius = kwagrs.get('radius')
        self.format = kwagrs.get('format')

    def get_lc_deg_all(self):
        data_return = mztf(ra=self.ra,dec=self.dec,radius=self.radius,format=self.format,nearest=False).zftcurves() 
        return data_return

    def get_lc_hms_all(self):
        data_return = mztf(hms=self.hms,radius=self.radius,format=self.format,nearest=False).zftcurves() 
        return data_return

    def get_lc_deg_nearest(self):
        data_return = mztf(ra=self.ra,dec=self.dec,radius=self.radius,format=self.format,nearest=True).zftcurves() 
        return data_return

    def get_lc_hms_nearest(self):
        data_return = mztf(hms=self.hms,radius=self.radius,format=self.format,nearest=True).zftcurves() 
        return data_return

```
'~/Freya/catalogs/ztf/methods.py'
```python

import requests
import io
from Freya.core import utils as u

import pandas
from astropy.io import ascii
from astropy.coordinates import SkyCoord
from astropy import units as u
from astropy.io.votable import parse,parse_single_table,from_table, writeto

class Methods_ztf():

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
        ztfdic = ''
        result_ = ascii.read(result.text)
        if len(result_) <= 0:
            ztfdic = 'light curve not found' 
            return ztfdic

        #the most close object to radius
        if self.nearest is True:
            
            result_ = result_.group_by('oid')
            minztf = self.id_nearest(result_)
            
            buf = io.StringIO()
            ascii.write(result_.groups[minztf],buf,format='csv')
            ztfdic =  buf.getvalue()
            return ztfdic

        # all objects in radius
        else:
            ztfdic = result.text
            return ztfdic

    def zftcurves(self):
        """ Get light curves of ztf objects 
        Parameters
        ----------
        """
        baseurl="https://irsa.ipac.caltech.edu/cgi-bin/ZTF/nph_light_curves"
        data = {}
        data['POS']=f'CIRCLE {self.ra} {self.dec} {self.radius}'
        data['FORMAT'] = self.format
        result = requests.get(baseurl,params=data)
        ztfdic = ''
        #return result
        if result.status_code != 200: 
            ztfdic = result.status_code 
            return ztfdic
        #if select csv 
        if self.format == 'csv':
            return self.csv_format(result)
```

And if you use catalog with source data base, need complete 'connect.py'
```
# Inside file connect.py
 - user
 - password
 - host
 - port
 - database
```
## New FreyaAPI
Other application of Freya is quick creation for the API used flask:
```
# In any directory in your system
freya-admin --newapi

```
In folder where is called create new flask application, it contains the
necessary routes generic that you only call and not modified, but first you need
add catalogs resources with :

```
# Inside folder FreyaAPI

freya-admin --addresource ztf
freya-admin --addresource ztf_local

# Only add resources if the catalog exists inside Freya, LocalFolder or 
# if you call --registercatalog.
```
Now you can run the FreyaAPI using : 

# Start (Who use)🚀
How to use the Freya and FreyaAPI.
First you look the complete demo (link al git que tenga todo)

## How use the rute FreyaAPI
The rutes in FreyaAPI are get methods and have four rutes.
```
 # Get light curves of objects with area in degrees.
 args : catalogs,ra,dec,radius,format
 Example:
  http://0.0.0.0:5000/get_lc?catalogs=ztf,ztf_local&ra=(float)&dec=(float)&radius=(float)&formnat=csv
 
 # Get light curve of object most close to area in degrees.
 args : catalogs,ra,dec,radius,format
 Example:
  http://0.0.0.0:5000/get_lc_nearest?catalogs=ztf,ztf_local&ra=(float)&dec=(float)&radius=(float)&formnat=csv    
```
```
 # Get light curves of objects with area in hh:mm:ss.
 args : catalogshms,radius,format
 Example:
  http://0.0.0.0:5000/get_lc_hms?catalogs=ztf,ztf_local&hms=(string)&radius=(float)&formnat=csv
 
 # Get light curve of object most close to area in hh:mm:ss.
 args : catalogshms,radius,format
 Example:
   http://0.0.0.0:5000/get_lc_hms_nearest?catalogs=ztf,ztf_local&hms=(string)&radius=(float)&formnat=csv   
```
## How use a only Freya
If you want use Freya but without installing, you can use the method 'GetData'.
```
from Freya.catalogs.core import GetData

data_all_deg = GetData(catalog='ztf',ra=(float),dec=(float),radius=(float),format='csv').get_lc_deg_all()
data_one_deg = GetData(catalog='ztf_local',ra=(float),dec=(float),radius=(float),format='csv').get_lc_deg_nearest()
data_all_hms = GetData(catalog='ztf',hms=(string),radius=(float),format='csv').get_lc_hms_all()
data_one_hms = GetData(catalog='ztf_local',hms=(string),radius=(float),format='csv').get_lc_hms_nearest()
```
# Build with 🛠️
* python
###
Jonimott de Malpais - [fernandezeric](https://github.com/fernandezeric)
