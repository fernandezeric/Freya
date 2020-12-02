from Freya.core.base import Base

class AddCatalog(Base):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        super().create_module_catalog()