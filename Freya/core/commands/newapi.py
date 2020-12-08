from Freya.core.base import Base

"""
Created new FreyaAPI
"""
class NewAPI(Base):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        super().create_new_api()