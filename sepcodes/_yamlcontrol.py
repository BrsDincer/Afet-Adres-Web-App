import yaml
import os

rt = os.path.dirname(os.path.relpath((__file__)))

class YAMLREADING(object):
    """
    YAML READING - FUNCTIONS
    """
    def __init__(self):
        self.__fl = os.path.join(rt,"__tilelayers.yaml")
    def __str__(self):
        return "YAML READING - SUBPROCESS"
    def __call__(self):
        return None
    def __getstate__(self):
        raise TypeError("[DENIED]")
    def __repr__(self):
        return YAMLREADING.__doc__
    def _DATA(self):
        return yaml.safe_load(open(self.__fl,"r"))
    def _TILE(self):
        dt = self._DATA()["tiles"]
        return dt
    