# GetScrapedConnect V1.0.1 (ASI Connect - Portrait Win Build)
# github.com/kendalled

import clipboard
import unicodecsv as csv
import pyautogui as pa
import random
import string


# UI references & setting delay
pa.PAUSE = 1.5

extension_pos = (982, 52)
copy_pos = (942, 170)
right_arrow_pos = (75, 515)

# Elements to be removed
asi_email1 = 'creditreporting@asicentral.com'
asi_email2 = 'support@asicentral.com'
ad_text = 'Upgrade the extension to autosave and automate your emails ID capture'

res = []

def cleanupData(string_input):
   
    # Removing ASI emails, empty elements, and ad text
    
    listy = string_input.split('\n')
    
    for ind, element in enumerate(listy):
        listy[ind] = element[:-1]
    if asi_email1 in listy:
      listy.remove(asi_email1)
    if asi_email2 in listy:
      listy.remove(asi_email2)  
    if ad_text in listy:
      listy.remove(ad_text)
    while '' in listy:
        listy.remove('')

    return(listy)

def get_25_emails():

    clipped_data = ''
    asi_number_pos_x = 98
    asi_number_pos_y = 596

    for i in range(25):
        #TODO: Click Red asi number (right end)
        pa.click(asi_number_pos_x, asi_number_pos_y)
        asi_number_pos_y += 43
        
        # rinses and repeats x 25 elements
    
    #Click extension, click copy all
    pa.click(extension_pos)
    pa.click(copy_pos)
    #Convert clipboard to string, pass through cleanupData()
    clipped_data = clipboard.paste()
    
    #returns data (to be appended to temp_list)
    return(cleanupData(clipped_data))

if __name__ == "__main__":
    temp_list = []
    
    
    #TODO: Change to 20
    for i in range(2):
        temp_list = get_25_emails()
                
        # click right arrow
        pa.click(right_arrow_pos)

        # creates uuid
        for element in temp_list:
            random_id = ''.join([random.choice(string.ascii_letters 
            + string.digits) for n in range(8)])
            res.append({'id': random_id,'email': element})
        
    #return/write csv output
    print(temp_list)
    with open('asi-connect-scraped-links.csv', 'wb') as f:
        fieldnames = ['id','email']
        writer = csv.DictWriter(f, fieldnames = fieldnames, quoting=csv.QUOTE_ALL)
        writer.writeheader()

        for data in res:
            writer.writerow(data)
            

   

    
