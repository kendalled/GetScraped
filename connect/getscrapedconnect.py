# GetScraped V3.0.1
# github.com/kendalled

import requests
import re
import unicodecsv as csv
#import pandas as pd
#from glob import glob
#import pyautogui as pa

# Negative Email Endings
negatives = ['domain.net','group.calendar.google','youremail.com','sample.com','yoursite.com','internet.com','companysite.com','sentry.io','domain.xxx','sentry.wixpress.com', 'example.com', 'domain.com', 'address.com', 'xxx.xxx', 'email.com', 'yourdomain.com']

stringy = '''
creditreporting@asicentral.com
maureen@promoteyourbusiness.ca
kyle@2kprinting.com
support@asicentral.com

Upgrade the extension to autosave and automate your emails ID capture.'''

def cleanupData(string_input):

  asi_email1 = 'creditreporting@asicentral.com'
  asi_email2 = 'support@asicentral.com'
  ad_text = 'Upgrade the extension to autosave and automate your emails ID capture.'



  listy = list(filter(('').__ne__, stringy.split('\n')))
  listy.remove(ad_text)
  listy.remove(asi_email1)
  listy.remove(asi_email2)
  print(listy)

if __name__ == "__main__":
  cleanupData(stringy)