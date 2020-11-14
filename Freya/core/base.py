import os
import sys
sys.path.insert(0, '/home/jonimottg/Escritorio/Avance/') #arreglar esta cosa 
import Freya.catalogs # __path__
import Freya.files
import tempfile
import zipfile


class Base():

    def __init__(self,argv,*argvs,**kwargs):
        self.type = argv[1] # arreglar esta parte, puede que no vengan
        self.name = argv[2]
        self.source = argv[3]
        self.path = kwargs.get('path')
        #print(self.path)
    # def get_name_files(self):
    #     return ListFile(self.source).get_name_files()
    
    def path_files_template_from(self):
        if self.source == 'api':
            return os.path.join(Freya.files.__path__[0],'file_templates','fromapi.zip')
        else :
            return os.path.join(Freya.files.__path__[0],'file_templates','fromdb.zip')
    
    def path_file_template_new_api(self):
        return os.path.join(Freya.files.__path__[0],'file_templates','newapi.zip')
    
    def path_file_template_resource(self):
        return os.path.join(Freya.files.__path__[0],'file_templates','resource.zip')

    #buscar la forma que descomprima los archivos templates
    def create_module_catalog(self):
        if self.source not in ['api','bd'] :
            raise TypeError (f'La fuente {self.source} no es valida')
        # namesFile = self.getNameFiles()
        dir_catalogs = Freya.catalogs.__path__[0] # directorios modulos catalogos
        path_new_catalog = os.path.join(dir_catalogs,self.name)
        path_tample_files_ = self.path_files_template_from()
        #print(path_new_catalog)
        #print(path_tample_files_)
        if self.name  in os.listdir(dir_catalogs) :
           raise TypeError ('Ya tiene ese catalogo amiguito')

        try: 
            os.mkdir(path_new_catalog) # crea la carpeta , pero esta vacia
            print(1)
            extract_zip = zipfile.ZipFile(path_tample_files_)
            extract_zip.extractall(path_new_catalog)
            extract_zip.close()
            # for file in namesFile:
            #     with open(os.path.join(pathNewCatalog, f'{file}.py'), 'w') as fp: 
            #         pass # aqui si es que llega a escribir

        except OSError as error:
            print(error) 
    
    def create_new_api(self):
        path_template_api = self.path_file_template_new_api()
        path_new_api =  os.path.join(self.path,'IIIII')#'/home/jonimottg/Escritorio/Avance/IIIII' #mas hard no puede ser
        try:
            os.mkdir(path_new_api)
            extract_zip = zipfile.ZipFile(path_template_api)
            extract_zip.extractall(path_new_api)
            extract_zip.close()
        except OSError as error:
            print(error) 
        #print(path_new_api)
    
    def create_new_resource(self):
        path_template_resource = self.path_file_template_resource()
        path_new_api =  os.path.join(self.path,'IIIII')#'/home/jonimottg/Escritorio/Avance/IIIII'
        path_new_resource = os.path.join(path_new_api,f'resources/{self.name}_resource') # join(newapi,nombre_resource)
        try:
            #descompime en las path
            #print(path_template_api)
            #print(path_new_api)
            #print(path_new_resource)
            os.mkdir(path_new_resource)
            extract_zip = zipfile.ZipFile(path_template_resource)
            extract_zip.extractall(path_new_resource)
            extract_zip.close()
        except OSError as error:
            print(error) 
        return
          
class AddCatalog(Base):  #más bonito
    def __init__(self,argv,*argvs,**kwargs):
        super().__init__(argv,*argvs,**kwargs)
        super().create_module_catalog()

class AddResource(Base):
    def __init__(self,argv,*argvs,**kwargs):
        super().__init__(argv,*argvs,**kwargs)
        super().create_new_resource()

class NewAPI(Base):
    def __init__(self,argv,*argvs,**kwargs):
        super().__init__(argv,*argvs,**kwargs)
        super().create_new_api()
      



