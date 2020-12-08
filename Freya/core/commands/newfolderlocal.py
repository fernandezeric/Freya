from Freya.core.base import Base

"""
Created new folder for local catalogue 
"""
class NewFolderLocal(Base):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        super().folder_local_catalog()