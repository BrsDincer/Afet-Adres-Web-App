import pandas as pd
import os

class DATAGATHERING(object):
    """
    DATA RESOURCES:
        
        #"https://afetadres.s3.eu-central-1.amazonaws.com/deprem_input.csv"
        #"https://afetadres.s3.eu-central-1.amazonaws.com/gas_station.csv"
        #"https://afetadres.s3.eu-central-1.amazonaws.com/crane_operator.csv"
        #"https://afetadres.s3.eu-central-1.amazonaws.com/internet_scan.csv"
        #"https://afetadres.s3.eu-central-1.amazonaws.com/child_need_data.csv"
        #"https://afetadres.s3.eu-central-1.amazonaws.com/debris_need_data.csv"
        #"https://afetadres.s3.eu-central-1.amazonaws.com/provision_need_data.csv"
        #"https://afetadres.s3.eu-central-1.amazonaws.com/injury_need_data.csv"
        #"https://afetadres.s3.eu-central-1.amazonaws.com/mersin_konaklama.csv"
        #"https://afetadres.s3.eu-central-1.amazonaws.com/ShelterandAccommodationAreas.csv"
        #"https://afetadres.s3.eu-central-1.amazonaws.com/FoodSpots.csv"
        #"https://afetadres.s3.eu-central-1.amazonaws.com/TransportationToDisasterAreas.csv"
        #"https://afetadres.s3.eu-central-1.amazonaws.com/ShelterOpportunitiesOutsideTheDisasterArea.csv"
        #"https://afetadres.s3.eu-central-1.amazonaws.com/PharmacyTrucks.csv"
        #"https://afetadres.s3.eu-central-1.amazonaws.com/LocationsofAidTrucks.csv"
        #"https://afetadres.s3.eu-central-1.amazonaws.com/AuthorizedContactNumbers.csv"
    """
    def __init__(self,dm:str):
        self.__dt = dm
    def __str__(self):
        return "DATA GATHERING - SUBPROCESS"
    def __call__(self):
        return None
    def __getstate__(self):
        raise TypeError("[DENIED]")
    def __repr__(self):
        return DATAGATHERING.__doc__
    def _READFILE(self):
        return pd.read_csv(self.__dt)
    def _SPEC(self,nminit:str):
        return self._READFILE()[nminit]
