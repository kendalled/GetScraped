# GetScraped V3.0.1
# github.com/kendalled

import requests
import re
import unicodecsv as csv
import pandas as pd
from glob import glob

# Negative Email Endings
negatives = ['domain.net','group.calendar.google','youremail.com','sample.com','yoursite.com','internet.com','companysite.com','sentry.io','domain.xxx','sentry.wixpress.com', 'example.com', 'domain.com', 'address.com', 'xxx.xxx', 'email.com', 'yourdomain.com']

# Set Response Headers
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

def get_email(url):

    # Filtering Function
    def filter_func(x):
        ind = x.find('@')+1
        print('filtering...')
        return not (x[ind:] in negatives)


    # Get HTML, regexp match, filter out bad emails
    try:

        site = requests.get(url, verify=True, headers=headers, timeout=(2, 2)).content.decode()
        possible_emails = re.findall(r'[A-Za-z0-9._%+-]{3,}@[a-z]{3,}\.[a-z]{2,}(?:\.[a-z]{2,})?', site)
        print('Fetched Web Page.\n')
        res = list(set(filter(filter_func,possible_emails)))

    # Fail case 1
    except:
        print('Web Page Not Found. Deleting...')
        return []

    # Fail case 2
    if(not res):
        print('No Emails Found. Deleting...')
        return []

    # Success
    else:
        print('Email(s):\n')
        print(res)

        return res

    # Extraneous Fail case
    return []


def runtime(filepath):
    # Reads website column, initializes counter variable
    df = pd.read_csv(filepath)
    fileName = './Output/' + filepath[filepath.find('/Data/')+6:filepath.find('.csv')] + '-EMAILS.csv'
    counter = 0
    final_list = []

    # Only appends businesses with valid email
    for index, row in df.iterrows():
        email = get_email(row['website'])
        if(email):
            for address in [elem.lower() for elem in email]:
                final_list.append({'business': row['business_name'], 'website': row['website'], 'industry': row['industry'], 'city': row['city'], 'state': row['state'], 'email': address })
            counter += len(email)
        # How many emails do you want? Set to 9999 for all.
        if(counter >= 15):
            break
        # Printing Status
        print('------------------------')
        print(str(counter) + ' Email(s) found so far.')
        print('------------------------')

    # Writing to CSV
    with open(fileName, 'wb') as csvfile:
        
        fieldnames = ['business','website','industry','city','state','email']
        writer = csv.DictWriter(csvfile, fieldnames = fieldnames, quoting=csv.QUOTE_ALL)
        writer.writeheader()

        for data in final_list:
            writer.writerow(data)

    print('File written! Kendall is the best. On to the next one!')

for entry in glob('./Data/*.csv'):
    runtime(entry)

print('Finished all files.')
