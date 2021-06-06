# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 16:49:32 2021

@author: Maciej-Lokal
"""

import requests
from datetime import datetime
import pandas as pd

date = datetime.today()

day = date.strftime("%Y-%m-%d")
print(day)


oznaczenie = ["EUR", "CHF", "USD"]
for item in oznaczenie:
    adress = f"https://www.bankier.pl/narzedzia/archiwum-kursow-walutowych/get_answer?op=4&cur_symbol={item}&start_dt=2018-06-07&end_dt={day}&customs=0&table_name=0&fromDay=0&monthDay=1&avg=0&avg_type=1&idTable=gemiusHitSection16"
    r = requests.get(adress, allow_redirects=True)

    open(f'{item}.csv', 'wb').write(r.content)
    
for item in oznaczenie:
    print(f"tabela {item}")
    
    j = 0
    with open(f"{item}.csv", "r") as t:
        for line in t:
            j +=1
            
    lines = list()
    with open(f"{item}.csv", "r") as f:
        for line in f:
            lines.append(line)
    
    with open(f"{item}.csv", "w") as save:
        i = 0
        save.write(f"Data;Kurs;Zmiana;Nazwa Tabeli\n")
        for line in reversed(lines):
            i += 1
            if i > 4:
                if (j - i) > 2:
                    save.write(line)
                    
    df = pd.read_csv(f"{item}.csv", delimiter = ";", usecols = ["Data", "Kurs"])
    df["kurs_sprzedaży"] = df["Kurs"] +0.03
    df["kurs_kupna"] = df["Kurs"] -0.03
    print(df)