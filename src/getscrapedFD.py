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
    def filter_func(x):
        ind = x.find('@') + 1
        return not (x[ind:] in negatives)

    try:
        site = requests.get(url, verify=True, headers=headers, timeout=(2, 2)).content.decode()
        possible_emails = re.findall(r'[A-Za-z0-9._%+-]{3,}@[a-z]{3,}\.[a-z]{2,}(?:\.[a-z]{2,})?', site)

        # Check if there are any valid emails
        if not possible_emails:
            # No emails found, try the '/contact' URL
            contact_url = url.rstrip('/') + '/contact'
            site_contact = requests.get(contact_url, verify=True, headers=headers, timeout=(2, 2)).content.decode()
            possible_emails = re.findall(r'[A-Za-z0-9._%+-]{3,}@[a-z]{3,}\.[a-z]{2,}(?:\.[a-z]{2,})?', site_contact)

        if possible_emails:
            res = list(set(filter(filter_func, possible_emails)))
            print('Email(s):\n')
            print(res)
            return res
        else:
            print('No Emails Found. Deleting...')
            return []
    except:
        print('Web Page Not Found. Deleting...')
        return []


def runtime(filepath):
    # Reads website column, initializes counter variable
    df = pd.read_csv(filepath)
    fileName = './Output/' + filepath[filepath.find('/Data/')+6:filepath.find('.csv')] + '-EMAILS2.csv'
    counter = 0
    final_list = []

    # Only appends businesses with valid email
    for index, row in df.iterrows():
        print(f'Processing row: ' + str(index))
        email = get_email(row['website'])
        if(email):
            for address in [elem.lower() for elem in email]:
                final_list.append({
                    'industry': row['industry'],
                    'business_name': row['business_name'],
                    'HQ addr1': row['HQ addr1'],
                    'HQ addr2': row['HQ addr2'],
                    'city': row['city'],
                    'state': row['state'],
                    'HQ zip': row['HQ zip'],
                    'Mail addr1': row['Mail addr1'],
                    'Mail addr2': row['Mail addr2'],
                    'Mail PO box': row['Mail PO box'],
                    'Mail city': row['Mail city'],
                    'Mail state': row['Mail state'],
                    'Mail zip': row['Mail zip'],
                    'HQ phone': row['HQ phone'],
                    'HQ fax': row['HQ fax'],
                    'County': row['County'],
                    'Dept Type': row['Dept Type'],
                    'Organization Type': row['Organization Type'],
                    'website': row['website'],
                    'Number Of Stations': row['Number Of Stations'],
                    'email': address
                })

            counter += len(email)
        # How many emails do you want? Set to 9999 for all.
        if(counter >= 99999):
            break
        # Printing Status
        print('------------------------')
        print(str(counter) + ' Email(s) found so far.')
        print('------------------------')

    # Writing to CSV
    with open(fileName, 'wb') as csvfile:
        
        fieldnames = [
    'industry', 'business_name', 'HQ addr1', 'HQ addr2', 'city', 'state', 'HQ zip',
    'Mail addr1', 'Mail addr2', 'Mail PO box', 'Mail city', 'Mail state', 'Mail zip',
    'HQ phone', 'HQ fax', 'County', 'Dept Type', 'Organization Type', 'website',
    'Number Of Stations', 'email'
        ]
        writer = csv.DictWriter(csvfile, fieldnames = fieldnames, quoting=csv.QUOTE_ALL)
        writer.writeheader()

        for data in final_list:
            writer.writerow(data)

    print('\nFile written! Kendall is the best. On to the next one!')

for entry in glob('./Data/fires.csv'):
    runtime(entry)
    # for debugging:
    # print(entry)

print('Finished all files.')
