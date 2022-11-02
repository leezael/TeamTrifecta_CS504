#%%
from get_data import fred_api
import pandas as pd
import csv

fred_sources = {'WPS101': 'Steel',
                'PWHEAMTUSDM': 'Wheat',
                'PCOALAUUSDM': 'Coal',
                'WPS0571': 'Gas',
                'PBARLUSDM': 'Barley',
                'PMAIZMTUSDM' : 'Corn'}

data = []
df = pd.DataFrame(data)

for key, val in fred_sources.items():
    print("Key:", key)    
    temp_df = fred_api(key, 'm', '2018-01-01', 'sum').pull()
    temp_df.columns = ['Date', 'Amount']

    temp_df['Commodity'] = [val for _ in range(temp_df.shape[0])]
    #print(temp_df)
 #   temp_df.to_csv("commodity.csv",sep=',', header=True)
#    temp_df.write.option("header",True).option("sep",",").csv("commodity_data.csv")
   # print(df)
    df=pd.concat([df, temp_df]) # df.union(temp_df)

print(df)
df.to_csv("commodity_all.csv",sep=',', header=True)

war_data = pd.read_excel(r'data/Ukraine_Black_Sea_2020_2022_Oct21.xlsx')
# %%
