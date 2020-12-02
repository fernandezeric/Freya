from Freya.core.base import Base

class AddResource(Base):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        super().create_new_resource()