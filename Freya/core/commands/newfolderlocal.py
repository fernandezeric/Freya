from Freya.core.base import Base

"""
Created new folder for local catalogs
--------------------------------------
Parameters
path : (string) path where created local folder for catalogs
"""
class NewFolderLocal(Base):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        super().folder_local_catalog()