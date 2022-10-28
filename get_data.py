
#%%
import pandas as pd 
import json
import requests
import numpy as np

class fred_api:
    """Object that retrieves data from the Federal Reserve database and saves it to a designated Excel file"""
    
    def __init__(self, code: str, frequency: str = '', start_period: str = '', agg_func: str = ''):

        self.code = code

        self.frequency = '&frequency=' + frequency
        
        #YYYY-MM-DD
        self.start_period = '&observation_start=' + start_period

        if agg_func == '':
            self.agg_func = agg_func

        else:
            self.agg_func = '&aggregation_method=' + agg_func


        #other revelant object information
        self.api_key = '&api_key=33f26e3d2b0baab37e3ac5a4efe6133f'
        self.fred_path = 'https://api.stlouisfed.org/fred/series/observations?series_id='

        self.call = self.fred_path + self.code + self.start_period + self.frequency + self.agg_func + self.api_key +"&file_type=json"

    def pull(self) -> pd.DataFrame:
        """Pulls data from the FRED API to the and saves it to specified file path"""
        raw = requests.get(self.call).content

        dump = json.loads(raw)['observations']

        vals = {dump[data]['date']: dump[data]['value'] for data in range(len(dump))}
            
        self.df = pd.DataFrame({'Date': list(vals.keys()), self.code: list(vals.values())}).replace('.', np.nan).dropna(axis=0)

        return self.df


class acled_api:
    #TODO - Emailed ACLED to get API access
    def __init__(self) -> None:
        self.api_key = 'vBJ9mgM!NQG5FG-t1aUS'

        self.data = requests.get(f'https://api.acleddata.com/country/read/?key={self.api_key}&email=wpriddy@gmu.edu&country=Ukraine')

    def pull(self):

        return self.data
# %%
