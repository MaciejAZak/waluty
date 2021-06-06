# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 16:45:36 2021

@author: annpl
"""

import pandas as pd
kursy_path = 'D:\\PythonProjects\\KursyWalut\\'
file_name = 'transakcje_historia.csv'


df = pd.read_csv(f'{kursy_path}{file_name}', encoding='utf-8', delimiter=';')
print(df)



user_date = input('Podaj datę w formacie: rrrr-mm-dd: ')
user_exchange_rate = input('Kurs: ')
user_units = input('Liczba jednostek: ')
user_transaction_type = input('Rodzaj transakcji(K - kupno, S - sprzedaż): ')
user_currency = input('Waluta (EUR, CHF, USD): ')

#df = df.append([user_date, user_exchange_rate, user_units, user_transaction_type])
df = df.append({'Data': user_date, 'Kurs': user_exchange_rate,'Liczba_jednostek': user_units, 'Rodzaj_transakcji': user_transaction_type, 'Waluta': user_currency}, ignore_index=True)
print(df)
df.to_csv(f'{kursy_path}{file_name}', encoding='utf-8', index=False, sep=';')

# with open(f'{kursy_path}{file_name}', 'r+', encoding='utf-8') as f:
#     for line in f:
#         print(line)