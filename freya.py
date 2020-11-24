"""
source ../Entornos/Freya/bin/activate
"""

"""
- [ ] Nuevo caso de uso: Crear catalogo de manera local
- [ ] Mejorar código: argparse, pascal case, setup.py
- [ ] Crear un catálogo en Freya
"""
## crear modulo cli para los comandos dentro de freya
from Freya.core.base import AddCatalog,AddResource,NewAPI # seria mejor dividir en varios archivoss
from Freya.catalogs.core import GetData # seria mejor dividir en varios archivoss
import os
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
parser.add_argument('-p','--prueba', action='store_true', help="que wea nanito?")                  
#--------------------------------------------------------------------------------------#   
args = parser.parse_args()


if args.newcatalog :
    print("Created new catalog...")
    try:
        AddCatalog(name=args.newcatalog[0],source =args.newcatalog[1])
    except:
        raise TypeError (f'failed to create new catalog : {args.newcatalog[0]} inside Freya')
elif args.newcatalog_local : 
    print("Created new local catalog...")
    print(args.newcatalog_local)

elif args.newapi :
    print("Created new FreyaAPI...")
    #print(args.newapi)
    try:
        NewAPI(path=os.path.dirname(os.path.abspath(__file__)))
    except:
        raise TypeError ('failed to create new base to FreaAPI')
elif args.addresource : 
    print("add new resource to FreyaAPI...")
    #print(args.addresource)
    try:
        AddResource(name=args.addresource[0],path=os.path.dirname(os.path.abspath(__file__)))
    except:
        raise TypeError (f'failed to create resouce : {args.addresource[0]} inside FreyaAPI')

elif args.prueba :
    data = GetData(catalogs="ps1",ra=139.33444972,dec=68.6350604,radius=0.0002777,format='csv').get_lc_deg_all()
    print("*"*10)
    print(data)
    print("*"*10)

# else :
#     raise TypeError (f'Comando {sys.argv[1]} no valido, unicamente validos [newcatalog,newapi,addresource]')