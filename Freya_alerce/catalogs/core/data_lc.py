from Freya_alerce.catalogs.core.core import GetData

class DataLcDegree(GetData):
    """
    """
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
    
    def get_data(self):
        return super().generic_call_data('get_lc_deg')

class DataLcHms(GetData):
    """
    """
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

    def get_data(self):
        return super().generic_call_data('get_lc_hms')