import os
import sys
import Freya.catalogs # __path__
import Freya.files.list_file as files_
import zipfile #read zip files
from Freya.files.verify_file import Verify


class Base():

    def __init__(self,**kwargs):
        self.name = kwargs.get('name')
        self.source = kwargs.get('source')
        self.path = kwargs.get('path')
        self.local = kwargs.get('local')
    """
    """
    def path_files_template_from(self):
        if self.source == 'api':
            return os.path.join(Freya.files.__path__[0],'file_templates','fromapi.zip')
        else :
            return os.path.join(Freya.files.__path__[0],'file_templates','fromdb.zip')
    """
    """
    def path_file_template_new_api(self):
        return os.path.join(Freya.files.__path__[0],'file_templates','newapi.zip')
    """
    """
    def path_file_template_resource(self):
        return os.path.join(Freya.files.__path__[0],'file_templates','newresource.zip')
    """
    """
    def create_module_catalog(self):

        if Verify().verify_source(self.source):
            raise TypeError (f'The source {self.source} not is valid')

        if Verify().verify_catalog_inside(self.name) or Verify().verify_catalog_local(self.name):  
            raise TypeError ('catalog already created')
        
        dir_catalogs = Freya.catalogs.__path__[0]
        path_new_catalog = os.path.join(dir_catalogs,self.name)
        path_tample_files_ = self.path_files_template_from()
        
        try: 
            os.mkdir(path_new_catalog) # created empty folder
            extract_zip = zipfile.ZipFile(path_tample_files_)
            extract_zip.extractall(path_new_catalog)
            extract_zip.close()
            #Replace word 'NAME' from the name catalog
            list_path = [os.path.join(path_new_catalog,'configure.py'),os.path.join(path_new_catalog,'methods.py')]
            files_.Files(list_path,'NAME',self.name).replace_in_files()
        except OSError as error:
            print(error)
    """

    """
    def create_module_catalog_local(self):
        if Verify().verify_source(self.source):
            raise TypeError (f'The source {self.source} not is valid')

        if Verify().verify_catalog_inside(self.name) or Verify().verify_catalog_local(self.name):  
            raise TypeError ('catalog already created')

        path_new_catalog = os.path.join(self.path,f'{self.name}')
        path_tample_files_ = self.path_files_template_from()
        
        try: 
            os.mkdir(path_new_catalog) # created empty folder
            extract_zip = zipfile.ZipFile(path_tample_files_)
            extract_zip.extractall(path_new_catalog)
            extract_zip.close()
            #Replace word 'NAME' from the name catalog
            list_path = [os.path.join(path_new_catalog,'configure.py'),os.path.join(path_new_catalog,'methods.py')]
            files_.Files(list_path,'Freya.catalogs','LocalCatalogs').replace_in_files()
            files_.Files(list_path,'NAME',self.name).replace_in_files()
        except OSError as error:
            print(error)
    """
    Created local folder from catalogs and add path to sys
    """
    def folder_local_catalog(self):
        path_folder_local = os.path.join(self.path,'LocalCatalogs')
        try:
            os.mkdir(path_folder_local)
            f = open(os.path.join(path_folder_local, '__init__.py'), 'w')
            f.close()
            sys.path.append(path_folder_local)

        except OSError as error:
            print(error)
    """
    """
    def create_new_api(self):
        path_template_api = self.path_file_template_new_api()
        path_new_api =  os.path.join(self.path,'FreyaAPI')
        try:
            os.mkdir(path_new_api)
            extract_zip = zipfile.ZipFile(path_template_api)
            extract_zip.extractall(path_new_api)
            extract_zip.close()
        except OSError as error:
            print(error)
    """
    """
    def create_new_resource(self):
        if not Verify().verify_catalog_inside(self.name) and not Verify().verify_catalog_local(self.name) :
            raise TypeError ('first created catalog inside Freya or local ')

        path_template_resource = self.path_file_template_resource()
        path_new_api =  self.path#os.path.join(self.path,'FreyaAPI')
        path_new_resource = os.path.join(path_new_api,f'resources/{self.name}_resource')
        try:
            os.mkdir(path_new_resource)
            extract_zip = zipfile.ZipFile(path_template_resource)
            extract_zip.extractall(path_new_resource)
            extract_zip.close()
            #Replace word 'NAME' from the name catalog
            list_path = [os.path.join(path_new_resource,'resource.py')]
            files_.Files(list_path,'NAME',self.name).replace_in_files()
        except OSError as error:
            print(error) 



