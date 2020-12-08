from Freya.core.base import Base

"""
Add new catalogue in local folder 
"""
class AddCatalogLocal(Base):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        super().create_module_catalog_local()