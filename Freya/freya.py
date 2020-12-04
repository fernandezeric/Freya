from Freya.core.commands.addcatalog import AddCatalog
from Freya.core.commands.addcataloglocal import AddCatalogLocal
from Freya.core.commands.addresource import AddResource
from Freya.core.commands.newapi import NewAPI
from Freya.core.commands.newfolderlocal import NewFolderLocal
from Freya.catalogs.core import GetData
import os
import argparse
import sys

def main():

    #----------------------------COMMAND LINE----------------------------------------------#
    parser = argparse.ArgumentParser()
    #--------------------------------------------------------------------------------------#
    parser.add_argument('-nc','--newcatalog', action='store', type=str, nargs=2, 
                            metavar=('<name>','<source>'),help="add new catalog inside Freya")
    #--------------------------------------------------------------------------------------#
    parser.add_argument('-ncl','--newcataloglocal', action='store', type=str, nargs=2, 
                            metavar=('<name>','<source>'),help="add new catalog who local module")
    #--------------------------------------------------------------------------------------#     
    parser.add_argument('-nfl','--newfolderlocal', action='store_true', help="create a new folder local from catalogs")
    #--------------------------------------------------------------------------------------#     
    parser.add_argument('-na','--newapi', action='store_true', help="create a new FreyaAPI")
    #--------------------------------------------------------------------------------------#                        
    parser.add_argument('-ar','--addresource', action='store', type=str, nargs=1, 
                            metavar=('<name>'),help="add module catalog who resource in FreyaApi")
    #--------------------------------------------------------------------------------------#      
    parser.add_argument('-p','--prueba', action='store_true', help="PRUEBAS - ELIMINAR")                  
    #--------------------------------------------------------------------------------------# 
    args = parser.parse_args()


    if args.newcatalog :
        print("Created new catalog...")
        try:
            AddCatalog(name=args.newcatalog[0],source=args.newcatalog[1])
        except:
            raise TypeError (f'Failed to create new catalog : {args.newcatalog[0]} inside Freya')

    elif args.newcataloglocal : 
        print("Created new local catalog...")
        #print(args.newcatalog_local,os.getcwd())
        try:
            AddCatalogLocal(name=args.newcataloglocal[0],source =args.newcataloglocal[1],path=os.getcwd())
        except:
            raise TypeError ('Fauled to create local module')

    elif args.newapi :
        print("Created new FreyaAPI...")
        try:
            NewAPI(path=os.getcwd())
        except:
            raise TypeError ('Failed to create new base to FreaAPI')

    elif args.addresource : 
        print("Add new resource to FreyaAPI...")
        try:
            AddResource(name=args.addresource[0],path=os.getcwd())
        except:
            raise TypeError (f'Failed to create resouce : {args.addresource[0]} inside FreyaAPI')

    elif args.newfolderlocal :
        print("Created a new folder from local catalogs...")
        try:
            NewFolderLocal(path=os.getcwd())
        except:
            raise TypeError ('Failed to create new local folder')



    elif args.prueba :
        data = GetData(catalogs="ztf",ra=139.33444972,dec=68.6350604,radius=0.0002777,format='csv').get_lc_deg_all()
        print("*"*10)
        print(data)
        print("*"*10)
        #print(__file__)
        #print(os.path.abspath(__file__))
        #print(sys.argv)
        ## path of execute freya-admin
        #print(os.path.join(os.getcwd(), 'FreyaAPI'))

if __name__ == ' __main__':
          main()