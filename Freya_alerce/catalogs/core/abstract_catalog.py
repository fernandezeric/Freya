from abc import ABC, abstractmethod

class BaseCatalog(ABC):

    @abstractmethod
    def get_lc_deg():
        """
       Get all ligth curves data or the most close object, inside degree area.

        Return
        -------
        Return numpy array 2d with rows represent the objects and columns : ['obj','ra','dec','mjd','mg','filter'].
            obj : double
                Id of object in catalog
            ra : double
                Right ascension
            dec : double
                Declination
            mjd : double
                Julian day
            mg : double
                Magnitud
            filter : str
                Band 
        """
        return ""

    @abstractmethod 
    def get_lc_hms():
        """
        Get all ligth curves data or the most close object, inside hh:mm:ss area.
        Return
        -------
        Return numpy array 2d with rows represent the objects and columns : ['obj','ra','dec','mjd','mg','filter'].
            obj : double
                Id of object in catalog
            ra : double
                Right ascension
            dec : double
                Declination
            mjd : double
                Julian day
            mg : double
                Magnitud
            filter : str
                Band 
        """
        return ""
