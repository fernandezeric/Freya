from Freya.core.base import Base

"""
Register local catalogue regardless of where it is created,
need use inside the catalogue
--------------------------------------
Parameters
path : (string) path where
"""
class RegisterLocalCatalogue(Base):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        super().register_local_catalogue()