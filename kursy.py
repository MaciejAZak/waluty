# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 21:04:12 2021

@author: Maciej-Lokal
"""
import pandas as pd
from datetime import datetime

liczba_jednostek = 100
profit_threshold = 0.04


def zakupWaluty(data, buy_price, tabela, liczba_jednostek, profit_threshold):
    print("#####")
    kwota_transakcji = liczba_jednostek * buy_price
    print(f"Dnia {data} kupiłem/amam {liczba_jednostek}EUR za {buy_price} - łącznie {kwota_transakcji}")
    var = False
    for index, rows in (df_buysell.iterrows()):
        if var == False:
            if index < data:
                pass
            else:
                zysk = rows['kurs kupna'] - buy_price
                if zysk > 0:
                    kwota_sprzedazy = liczba_jednostek * rows['kurs kupna']
                    if (kwota_sprzedazy / kwota_transakcji) >= 1 + profit_threshold:
                        print(f"Dnia {index} można sprzedać za {rows['kurs kupna']} z zyskiem {zysk * liczba_jednostek}")
                        total = kwota_transakcji + zysk * liczba_jednostek
                        var = True
                        return total
        else:
            pass
    
                    

kursy_path = ("C:\\Users\\Maciej-Lokal\\.spyder-py3\\waluty.csv")

df = pd.read_csv(kursy_path, delimiter = ";")
df["kurs sprzedaży"] = df["Kurs"] +0.03
df["kurs kupna"] = df["Kurs"] -0.03

print(df)

date = datetime.today()

day = date.strftime("%Y-%m-%d")
print(day)


print(df.loc[df["Data"] == day])

df_buysell = df[["Data", "kurs kupna", "kurs sprzedaży"]]
df_buysell['Data'] =pd.to_datetime(df.Data)
df_buysell.sort_values(by='Data', inplace = True)
df_buysell.set_index("Data", inplace = True)

print(df_buysell)
df_buysell.plot()

itr = next(df_buysell.iterrows())[1]
prev_month = itr.name.month

done = False
total_zainwestowanePLN = 0
totalEUR = 0
totalPLN = 0
for index, rows in (df_buysell.iterrows()):
    if index.month != prev_month:
        done = False
    if done == False:
        #print(rows.name)
        total_zainwestowanePLN += rows['kurs sprzedaży'] * liczba_jednostek
        zysk = zakupWaluty(rows.name,rows['kurs sprzedaży'], df_buysell, liczba_jednostek, profit_threshold)
        print(f"Udało się zarobić {zysk}")
        if zysk == None:
            totalEUR += liczba_jednostek
        else:
            totalPLN += zysk
        done = True
    prev_month = index.month
    
print(f"Zainwestowano {total_zainwestowanePLN}")
print(f"Ostatecznie masz {totalPLN} PLN i {totalEUR} EUR warte łącznie {totalPLN + (totalEUR * rows['kurs kupna'])} PLN")
print(f"Zarobiono {(totalPLN + (totalEUR * rows['kurs kupna'])) - total_zainwestowanePLN}")