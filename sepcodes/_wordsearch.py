import pandas as pd

class WORDSEARCH(object):
    """
    WORD SEARCH IN DATA - FUNCTIONS
    """
    def __init__(self):
        self.__debris = ["enkaz","yıkık","çöktü","moloz","taş","alçı"]
        self.__child = ["biberon","süt","çocuk","bebek","küçük","mama"]
        self.__provisions = ["erzak","su","gıda","yiyecek","içecek","açlık","susuzluk"]
        self.__injury = ["sakatlık",
                         "sakatlanmak",
                         "yaralanmak",
                         "yaralandı",
                         "sakatlandı",
                         "kanıyor",
                         "kanama",
                         "kırıldı",
                         "kırılmak",
                         "risk",
                         "ölüm",
                         "sıkışma",
                         "sıkıştı",
                         "sıkıştım"]
    def __str__(self):
        return "WORD SEARCH FUNCTION - SUBPROCESS"
    def __call__(self):
        return None
    def __getstate__(self):
        raise TypeError("[DENIED]")
    def __repr__(self):
        return WORDSEARCH.__doc__
    def _RUN(self,dbinit:classmethod):
        deb = 0
        chl = 0
        pro = 0
        inj = 0
        for ep in dbinit:
            for xd in self.__debris:
                if xd in ep.lower():
                    deb += 1
            for xc in self.__child:
                if xc in ep.lower():
                    chl += 1
            for xp in self.__provisions:
                if xp in ep.lower():
                    pro += 1
            for xi in self.__injury:
                if xi in ep.lower():
                    inj += 1
        return deb,chl,pro,inj
        