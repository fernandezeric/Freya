from Freya.core.base import Base

"""
Add new catalogue inside Freya
"""
class AddCatalog(Base):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        super().create_module_catalog()