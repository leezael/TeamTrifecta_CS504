#import dependencies
import pandas as pd
import csv

#read file
filename = '/Users/dcolu/OneDrive/Documents/GitHub/TeamTrifecta_CS504/scripts/data/commodity_exports.csv'
df = pd.read_csv(filename, encoding = "ISO-8859-1")
df.head()


