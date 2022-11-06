#%%
from get_data import fred_api
import pandas as pd
import csv

#fred_sources = {'WPS101': 'Steel',
#                'PWHEAMTUSDM': 'Wheat',
#                'PCOALAUUSDM': 'Coal',
#                'WPS0571': 'Gas',
#                'PBARLUSDM': 'Barley',
#                'PMAIZMTUSDM' : 'Corn'}

fred_sources = {'PIORECRUSDM': 'IronOre',
      'PSUNOUSDM': 'SunflowerOil',
      'PROILUSDM': 'RapeseedOil',
      'WPU10170674': 'StainlessSteel',
      'WPS101707': 'RolledSteel',
      'WPU101213': 'CastIron',
      'WPU139902094': 'Slag',
      'WPS029': 'AnimalFodder',
      'WPS0571': 'Gas',
      'PBARLUSDM': 'Barley',
      'PMAIZMTUSDM' : 'Corn',
      'WPS101': 'Steel',
      'PWHEAMTUSDM': 'Wheat',
      'PCU2111112111111':'CrudePetroleum',
      'PCU3241913241910': 'RefinedPetroleum',
      'PCOALAUUSDM': 'Coal',
      'WPS0571': 'Gas',
      'PCU2122212122210' : 'GoldOre',
      'WPU102504' : 'Nickel',
      'PALUMUSDM' : 'Aluminium',
      'PCOPPUSDM': 'Copper'}


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

# %%
