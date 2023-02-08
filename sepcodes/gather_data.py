import json,requests
import pandas as pd

# rp = requests.get("https://api.afetharita.com/feeds/locations?format=json")

# tp = json.loads(rp.text)
# print(len(tp["results"]))
# print(tp["results"][1]["formatted_address"])
# print(tp["results"][1]["loc"][0])
# print(tp["results"][1]["loc"][1])
# print(tp["results"][1]["raw"]["full_text"])

addr = []
loc_lat = []
loc_lon = []
mss = []
for xp in range(1,615):
    rp = requests.get(f"https://api.afetharita.com/feeds/locations?format=json&page={xp}")
    tp = json.loads(rp.text)
    for xi in range(len(tp["results"])):
        addr.append(tp["results"][xi]["formatted_address"])
        loc_lat.append(tp["results"][xi]["loc"][0])
        loc_lon.append(tp["results"][xi]["loc"][1])
        mss.append(tp["results"][xi]["raw"]["full_text"])
        print(f"DONE: {str(xp)}-{str(xi)}")
    
dict_all = {"ADRES":addr,
            "ENLEM":loc_lat,
            "BOYLAM":loc_lon,
            "MESAJ":mss}
df = pd.DataFrame(dict_all)
df.to_csv("internet_kullanicilari.csv")