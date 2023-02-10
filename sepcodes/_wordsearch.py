import pandas as pd

class WORDSEARCH(object):
    """
    WORD SEARCH IN DATA - FUNCTIONS
    """
    def __init__(self):
        self.__debris = ["enkaz",
                         "yıkık",
                         "çöktü",
                         "moloz",
                         "taş",
                         "alçı",
                         "yıkım",
                         "yıkıldı",
                         "çöküntü",
                         "yerlebir"]
        self.__child = ["biberon",
                        "süt",
                        "çocuk",
                        "bebek",
                        "küçük",
                        "mama"]
        self.__provisions = ["erzak",
                             "su",
                             "gıda",
                             "yiyecek",
                             "içecek",
                             "açlık",
                             "susuzluk"]
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
                         "sıkıştım",
                         "hipotermi",
                         "sıkıştılar"]
    def __str__(self):
        return "WORD SEARCH FUNCTION - SUBPROCESS"
    def __call__(self):
        return None
    def __getstate__(self):
        raise TypeError("[DENIED]")
    def __repr__(self):
        return WORDSEARCH.__doc__
    def _RUN_FOR_COUNT(self,dbinit:classmethod):
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
    def _RUN_FOR_CLASS(self,dbinit:classmethod):
        deb_lat = []
        deb_lon = []
        deb_mes = []
        chl_lat = []
        chl_lon = []
        chl_mes = []
        pro_lat = []
        pro_lon = []
        pro_mes = []
        inj_lat = []
        inj_lon = []
        inj_mes = []
        for cc,ms in enumerate(dbinit["MESAJ"]):
            for xd in self.__debris:
                if xd in ms.lower():
                    deb_lat.append(dbinit["ENLEM"][cc])
                    deb_lon.append(dbinit["BOYLAM"][cc])
                    deb_mes.append(ms)
            for xc in self.__child:
                if xc in ms.lower():
                    chl_lat.append(dbinit["ENLEM"][cc])
                    chl_lon.append(dbinit["BOYLAM"][cc])
                    chl_mes.append(ms)
            for xp in self.__provisions:
                if xp in ms.lower():
                    pro_lat.append(dbinit["ENLEM"][cc])
                    pro_lon.append(dbinit["BOYLAM"][cc])
                    pro_mes.append(ms)
            for xi in self.__injury:
                if xi in ms.lower():
                    inj_lat.append(dbinit["ENLEM"][cc])
                    inj_lon.append(dbinit["BOYLAM"][cc])
                    inj_mes.append(ms)
        return deb_lat,deb_lon,deb_mes,chl_lat,chl_lon,chl_mes,pro_lat,pro_lon,pro_mes,inj_lat,inj_lon,inj_mes
    def _MAKE_DATA(self,dbinit:classmethod):
        deb_lat,deb_lon,deb_mes,chl_lat,chl_lon,chl_mes,pro_lat,pro_lon,pro_mes,inj_lat,inj_lon,inj_mes = self._RUN_FOR_CLASS(dbinit)
        mdebdict = {"ENKAZ_İHTİMALİ_ENLEM":deb_lat,
                 "ENKAZ_İHTİMALİ_BOYLAM":deb_lon,
                 "MESAJ":deb_mes}
        mchldict = {"ÇOCUK_BULUNMA_İHTİMALİ_ENLEM":chl_lat,
                 "ÇOCUK_BULUNMA_İHTİMALİ_BOYLAM":chl_lon,
                 "MESAJ":chl_mes}
        mprodict = {"ERZAK_GEREKLİLİK_İHTİMALİ_ENLEM":pro_lat,
                 "ERZAK_GEREKLİLİK_İHTİMALİ_BOYLAM":pro_lon,
                 "MESAJ":pro_mes}
        minjdict = {"SAKATLANMA_İHTİMALİ_ENLEM":inj_lat,
                 "SAKATLANMA_İHTİMALİ_BOYLAM":inj_lon,
                 "MESAJ":inj_mes}
        mdebdata = pd.DataFrame(mdebdict)
        mdebdata.drop_duplicates()
        mdebdata.reset_index(drop=True,inplace=True)
        mchldata = pd.DataFrame(mchldict)
        mchldata.drop_duplicates()
        mchldata.reset_index(drop=True,inplace=True)
        mprodata = pd.DataFrame(mprodict)
        mprodata.drop_duplicates()
        mprodata.reset_index(drop=True,inplace=True)
        minjdata = pd.DataFrame(minjdict)
        minjdata.drop_duplicates()
        minjdata.reset_index(drop=True,inplace=True)
        return mdebdata,mchldata,mprodata,minjdata
        
        
        