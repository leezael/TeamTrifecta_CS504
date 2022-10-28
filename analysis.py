#%%
from get_data import fred_api
import pandas as pd

fred_sources = {'WPS101': 'Steel',
                'PWHEAMTUSDM': 'Wheat',
                'PCOALAUUSDM': 'Coal',
                'WPS0571': 'Gas',
                'PBARLUSDM': 'Barley',
                'PMAIZMTUSDM' : 'Corn'}

data = {}

for key, val in fred_sources.items():
    
    temp_df = fred_api(key, 'm', '2021-05-01', 'sum').pull()

    temp_df.columns = ['Date', 'Amount']

    temp_df['Commodity'] = [val for _ in range(temp_df.shape[0])]

    data[val] = temp_df

commodities_data = pd.concat(data).reset_index(drop=True)
# %%
