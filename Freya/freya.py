#command Freya
from Freya.core.commands.addcatalog import AddCatalog
from Freya.core.commands.addcataloglocal import AddCatalogLocal
from Freya.core.commands.addresource import AddResource
from Freya.core.commands.newapi import NewAPI
from Freya.core.commands.newfolderlocal import NewFolderLocal
from Freya.core.commands.registerlocalcatalog import RegisterLocalCatalog
#
import os
import argparse
import sys

"""
Define the CLI for Freya specific command line. 
"""
def main():

    #----------------------------COMMAND LINE----------------------------------------------#
    #parser = argparse.ArgumentParser()
    formatter = lambda prog: argparse.HelpFormatter(prog,max_help_position=70)
    parser = argparse.ArgumentParser(formatter_class=formatter)
    #--------------------------------------------------------------------------------------#
    parser.add_argument('-nc','--newcatalogue', action='store', 
                        metavar=('<name>','<source>'),
                        help="add new catalog inside Freya",
                        type=str, nargs=2)
    #--------------------------------------------------------------------------------------#     
    parser.add_argument('-nfl','--newfolderlocal', action='store_true',
                        help="create a new folder local from catalogs")
    #--------------------------------------------------------------------------------------#
    parser.add_argument('-ncl','--newcataloguelocal', action='store', 
                        metavar=('<name>','<source>'),
                        help="add new catalog who local module",
                        type=str, nargs=2)
    #--------------------------------------------------------------------------------------# 
    parser.add_argument('-na','--newapi', action='store_true', 
                        help="create a new FreyaAPI")
    #--------------------------------------------------------------------------------------#                        
    parser.add_argument('-ar','--addresource', action='store',
                        metavar='<name>',
                        help="add module catalog who resource in FreyaApi",
                        type=str, nargs=1)
    #--------------------------------------------------------------------------------------#     
    parser.add_argument('-rcl','--registercatalog',action='store_true',
                        help="register local catalogue")
    #--------------------------------------------------------------------------------------#
    args = parser.parse_args()


# metavar=''
    """
    Check what was the command line called, try call associated method.
    """
    if args.newcatalogue :
        print("Created new catalogue...")
        try:
            AddCatalog(name=args.newcatalogue[0],source=args.newcatalogue[1])
        except:
            raise TypeError (f'Failed to create new catalogue : {args.newcatalogue[0]} inside Freya')

    elif args.newcataloguelocal : 
        print("Created new local catalogue...")
        try:
            AddCatalogLocal(name=args.newcataloguelocal[0],source =args.newcataloguelocal[1],path=os.getcwd())
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
    
    elif args.registercatalog:
        print("Register new local catalogue")
        try:
            RegisterLocalCatalog(path=os.getcwd())
        except:
            raise TypeError ('Failed to register new local catalogue')

if __name__ == ' __main__':
          main()
