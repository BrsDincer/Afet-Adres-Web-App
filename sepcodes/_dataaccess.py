import pandas as pd
import os

class DATAGATHERING(object):
    """
    DATA RESOURCES:
        
        #"https://afetadres.s3.eu-central-1.amazonaws.com/deprem_input.csv"
        #"https://afetadres.s3.eu-central-1.amazonaws.com/gas_station.csv"
        #"https://afetadres.s3.eu-central-1.amazonaws.com/crane_operator.csv"
        #"https://afetadres.s3.eu-central-1.amazonaws.com/internet_scan.csv"
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