"""
- [ ] Nuevo caso de uso: Crear catalogo de manera local
- [ ] Mejorar código: argparse, pascal case, setup.py
- [ ] Crear un catálogo en Freya
"""
from Freya.core.base import AddCatalog,AddResource,NewAPI
from Freya.catalogs.core import GetData # seria mejor dividir en varios archivoss
import argparse


#----------------------------COMMAND LINE----------------------------------------------#
parser = argparse.ArgumentParser()
#--------------------------------------------------------------------------------------#
parser.add_argument('-nc','--newcatalog', action='store', type=str, nargs=2, 
                        metavar=('name','source'),help="add new catalog inside Freya")
#--------------------------------------------------------------------------------------#
parser.add_argument('-ncl','--newcatalog_local', action='store', type=str, nargs=3, 
                        metavar=('name','source','path'),help="add new catalog who local module")
#--------------------------------------------------------------------------------------#     
parser.add_argument('-na','--newapi', action='store_true', help="create a new FreyaAPI")
#--------------------------------------------------------------------------------------#                        
parser.add_argument('-ar','--addresource', action='store', type=str, nargs=1, 
                        metavar=('name'),help="add module catalog who resource in FreyaApi")
#--------------------------------------------------------------------------------------#                        
args = parser.parse_args()


if args.newcatalog :
    print("Created new catalog...")
    print(args.newcatalog)
    # try:
    #     AddCatalog(args.newcatalog)
    # except:
    #     raise TypeError (f'Fallo al intentar crear el modulo catalogo {sys.argv[2]}')
elif args.newcatalog_local : 
    print("Created new local catalog...")
    print(args.newcatalog_local)
    # try:
    #     AddCatalog(args.newcatalog)
    # except:
    #     raise TypeError (f'Fallo al intentar crear el modulo catalogo {sys.argv[2]}')
elif args.newapi :
    print("Created new FreyaAPI...")
    print(args.newapi)
    # try:
    #     AddCatalog(args.newcatalog)
    # except:
    #     raise TypeError (f'Fallo al intentar crear el modulo catalogo {sys.argv[2]}')
elif args.addresource : 
    print("add new resource to FreyaAPI...")
    print(args.addresource)
    # try:
    #     AddCatalog(args.newcatalog)
    # except:
    #     raise TypeError (f'Fallo al intentar crear el modulo catalogo {sys.argv[2]}')

# elif sys.argv[1] == 'prueba':
#     data = GetData(catalogs="ztf",ra=1,dec=2,radius=3,format=4).get_lc_deg_all()
#     print("*"*10)
#     print(data)
#     print("*"*10)

# else :
#     raise TypeError (f'Comando {sys.argv[1]} no valido, unicamente validos [newcatalog,newapi,addresource]')