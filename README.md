# GO GO MEMORI2
### Here it is the module python catalog 'Freya', the api 'FreyaAPI' and local folder. Is a complete example.
Freya is a Fremework <3, and this github is the python code.

## Start 🚀
With Freya get light curve data is more simple.
Have option by CLI 'freya-admin', the options are:
  
  * Creates new catalogue who module inside Freya, where <name> is the name of catalogue what choose and <source>
  is where it comes from (available options: api,db).
  ```
  freya-admin --newcatalog <name> <source>
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
  where <name> is the name of catalogue what choose and <source> is where it comes from (available options: api,db).
  ```
  freya-admin --newcataloglocal <name> <source>
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

## Build with 🛠️
* python
* 
###
Jonimott de Malpais - [fernandezeric](https://github.com/fernandezeric)
