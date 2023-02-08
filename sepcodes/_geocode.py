from geopy.geocoders import Nominatim

class GEOLOCATIONGATHERING(object):
    """
    RETURN GEOLOCATION ATTRIBUTES
    """
    def __init__(self):
        self.__fc = Nominatim(user_agent="gemgeo")
    def __str__(self):
        return "GEOLOCATION INFORMATION - SUBPROCESS"
    def __call__(self):
        return None
    def __getstate__(self):
        raise TypeError("[DENIED]")
    def __repr__(self):
        return GEOLOCATIONGATHERING.__doc__
    def _RETURNRAW(self,addr:str):
        rw = self.__fc.geocode(addr)
        if rw != None:
            return rw.raw
        else:
            return None
    def _RETURNALL(self,addr:str):
        try:
            rw = self._RETURNRAW(addr)
            try:
                if rw != None:
                    main = rw["display_name"]
                    lat = rw["lat"]
                    lon = rw["lon"]
                    return main,lat,lon
                else:
                    pass
            except:
                return None,None,None
        except:
            None,None,None