# Testing functionality
# Kendall Jackson
### possible regexp: [^\s@<>]+@[^\s@<>]+\.[^\s@<>]+
###  Backup regexp: '[\w.]+@[\w.]+'

import requests
import re
import unicodecsv as csv
import pandas as pd

# Reads website column, initializes counter variable
df = pd.read_csv('./Data/BigBear.csv')
final_list = []
email="sample@sample.com"

for index, row in df.iterrows():
    # if email exists
    if(index < 10):
        final_list.append({'business_name': row['business_name'], 'website': row['website'], 'industry': row['industry'], 'city': row['city'], 'state': row['state'], 'email': email })
            

print(final_list)
