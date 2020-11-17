import os
import Freya.catalogs # __path__
import Freya.files.list_file as files_
import zipfile #read zip files


class Base():

    def __init__(self,**kwargs):
        self.name = kwargs.get('name')
        self.source = kwargs.get('source')
        self.path = kwargs.get('path')

    def path_files_template_from(self):
        if self.source == 'api':
            return os.path.join(Freya.files.__path__[0],'file_templates','fromapi.zip')
        else :
            return os.path.join(Freya.files.__path__[0],'file_templates','fromdb.zip')
    
    def path_file_template_new_api(self):
        return os.path.join(Freya.files.__path__[0],'file_templates','newapi.zip')
    
    def path_file_template_resource(self):
        return os.path.join(Freya.files.__path__[0],'file_templates','newresource.zip')

    def create_module_catalog(self):
        if self.source not in ['api','bd'] :
            raise TypeError (f'La fuente {self.source} no es valida')
        dir_catalogs = Freya.catalogs.__path__[0] # directorios modulos catalogos
        path_new_catalog = os.path.join(dir_catalogs,self.name)
        path_tample_files_ = self.path_files_template_from()

        if self.name  in os.listdir(dir_catalogs) :
           raise TypeError ('catalog already created')

        try: 
            os.mkdir(path_new_catalog) # crea la carpeta , pero esta vacia
            extract_zip = zipfile.ZipFile(path_tample_files_)
            extract_zip.extractall(path_new_catalog)
            extract_zip.close()
            #Replace word 'NAME' from the name catalog
            list_path = [os.path.join(path_new_catalog,'configure.py'),os.path.join(path_new_catalog,'methods.py')]
            files_.Files(list_path,'NAME',self.name).replace_in_files()
        except OSError as error:
            print(error) 
    
    def create_new_api(self):
        path_template_api = self.path_file_template_new_api()
        path_new_api =  os.path.join(self.path,'IIIII')
        try:
            os.mkdir(path_new_api)
            extract_zip = zipfile.ZipFile(path_template_api)
            extract_zip.extractall(path_new_api)
            extract_zip.close()
        except OSError as error:
            print(error) 
    
    
    def create_new_resource(self):
        path_template_resource = self.path_file_template_resource()
        path_new_api =  os.path.join(self.path,'IIIII')#'/home/jonimottg/Escritorio/Avance/IIIII' #CAMBIAR POR FreyaAPI y que sea la unica
        path_new_resource = os.path.join(path_new_api,f'resources/{self.name}_resource') # join(newapi,nombre_resource)
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
          
class AddCatalog(Base):  #más bonito
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        super().create_module_catalog()

class AddResource(Base):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        super().create_new_resource()

class NewAPI(Base):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        super().create_new_api()
      



