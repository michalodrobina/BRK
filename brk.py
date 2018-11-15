import pandas as pd
import math
import logging

brk_csv=pd.read_csv('brk-b_us_d(1).csv', index_col='Data')

usdpln_csv=pd.read_csv('usdpln_d(1).csv', index_col='Data')

price_max=brk_csv.Najwyzszy*usdpln_csv.Najwyzszy

price=brk_csv.Zamkniecie*usdpln_csv.Zamkniecie

zamk_usd=usdpln_csv.Zamkniecie

brk_csv['zamk_usd']=pd.Series(zamk_usd,index=brk_csv.index)

brk_csv['price']=pd.Series(round(price,2),index=brk_csv.index)

brk_csv=brk_csv.drop(columns=['Otwarcie','Najwyzszy','Najnizszy','Wolumen'])

brk_csv.to_csv('output.csv')

'''poszukiwanie 20% spadku'''

'''teraz petla'''

liczba=0
years = {'1996': 0}
for y in range(1997,2019):
    years[y]=0

logger = logging.getLogger('myapp')
hdlr=logging.FileHandler('brk.log')
formatter= logging.Formatter('%(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.INFO)

print('Data górki, cena na górce, data dołka, cena w dołku, spadek procentowo %')
logger.info('Data górki, cena na górce, data dołka, cena w dołku, spadek procentowo %')

for i in range(0,len(brk_csv)-1):
    from_max = brk_csv.iloc[i+1:]
    lok_min = from_max['price'].min()
    lok_min_index = from_max['price'].idxmin()
    if (math.isnan(brk_csv['price'].iloc[i]) == False):
        if (round(lok_min/brk_csv['price'].iloc[i]*100,1)<80):
            print(brk_csv.index[i], brk_csv['price'].iloc[i], lok_min_index, lok_min, round(lok_min/brk_csv['price'].iloc[i]*100,1))
            logger.info(str((brk_csv.index[i], brk_csv['price'].iloc[i], lok_min_index, lok_min, round(lok_min/brk_csv['price'].iloc[i]*100,1))))
            years[int(lok_min_index[:4])]=years.get(int(lok_min_index[:4]))+1
            liczba+=1
print('liczba: ',liczba,'/',len(brk_csv))

for k,v in years.items():
    print('{} {}'.format(k,v))
