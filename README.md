# GO GO MEMORI2 [Pensando que esta solamente Freya]
### Here it is the module python catalog 'Freya'.
Freya is a Fremework <3, and this github is the python code.

## Start (Install and add catalogs)🚀
With Freya get light curve data is more simple.
Have option by CLI 'freya-admin', the options are:
  
  * Creates new catalogue who module inside Freya, where name is the name of catalogue what choose and source
  is where it comes from (available options: api,db).
  ```
  freya-admin --newcatalogue <name> <source>
  ```
  * Creates new api called FreyaAPI in path with call freya-admin, this opcion create a new flask application with
  all rutes necessaries.
  ```
  freya-admin --newapi
  ```
  * Add new resource in FreyaAPI, but first need whit catalogue exist in Freya or local folder and the call --addresource
  inside the folder FreyaAPI.
  ```
  freya-admin --addresource <name> 
  ```
  * You can creates local catalgos but first need create new folder, this call creates new local folder in path with call freya-admin, 
  and register path in sys.
  ```
  freya-admin --newfolderlocal
  ```
  * And want creates new catalogue who module in local folder, need call --newcataloglocal inside the folder created with --newfolderlocal.
  where name is the name of catalogue what choose and source is where it comes from (available options: api,db).
  ```
  freya-admin --newcataloguelocal <name> <source>
  ```
  * If you download any catalogue and want need rapid register, can use --registercatalogue. This method register path of local 
  catalogue for use need call inside catalogue folder (register in sys python).
  ```
  freya-admin --registercatalogue
  ```

### Install Freya and create module.🔧
#####pensando que el repositorio solo tiene el modulo Freya
First clone repository
```
pip install .
freya-admin --newcatalog ztf api|db
```
### Install FreyaAPI and add resource from module Freya.🔧
```
freya-admin --newapi
# Inside folder FreyaAPI
freya-admin --addresource ztf
```
### Install Freya and FreyaAPI then add resource from module Freya and use the local module.🔧
```
pip install .

freya-admin --newcatalog ztf api|db

freya-admin --newlocalfolder

# Inside local folder catalogs
freya-admin --newcataloglocal ztf_local api|db

freya-admin --newapi
# Inside folder FreyaAPI
freya-admin --addresource ztf
freya-admin --addresource ztf_local
```
## Start (Configure new catalogue)🚀
After add new local catalogue or created catalogue inside Freya 
and before use in FreyaApi or local with method gedData, 
need catalogue modify inside configure.py in folder of catalogue.

Specifically, you need to complete the four methods within configure.py,
if you want can use the methods.py to create generic methods and call
this in configure.py

## Start (Who use)🚀
How to use the Freya and FreyaAPI.
First you look the Demo in this github()

### How use the rute FreyaAPI
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
### How use a only Freya
If you want use Freya but without installing, you can use the method 'GetData'.
```
from Freya.catalogs.core import GetData

data_all_deg = GetData(catalogue='ztf',ra=(float),dec=(float),radius=(float),format='csv').get_lc_deg_all()
data_one_deg = GetData(catalogue='ztf_local',ra=(float),dec=(float),radius=(float),format='csv').get_lc_deg_nearest()
data_all_hms = GetData(catalogue='ztf',hms=(string),radius=(float),format='csv').get_lc_hms_all()
data_one_hms = GetData(catalcatalogueogs='ztf_local',hms=(string),radius=(float),format='csv').get_lc_hms_nearest()
```
## Build with 🛠️
* python
###
Jonimott de Malpais - [fernandezeric](https://github.com/fernandezeric)
