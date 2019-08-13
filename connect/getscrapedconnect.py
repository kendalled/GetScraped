# GetScrapedConnect V0.0.1 (ASI Connect - Windows Build)
# github.com/kendalled

import clipboard
import unicodecsv as csv
import pyautogui as pa

# UI references & setting delay
pa.PAUSE = 1

extension_pos = (980, 52)
copy_pos = (943, 170)
right_arrow_pos = (245, 513)

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
        
    listy.remove(asi_email1)
    listy.remove(asi_email2)
    listy.remove(ad_text)
    
    while '' in listy:
        listy.remove('')

    return(listy)

def get_25_emails():

    clipped_data = ''
    asi_number_pos_x = 103
    asi_number_pos_y = 593

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
    
    #returns data (to be appended to final_list)
    return(cleanupData(clipped_data))

if __name__ == "__main__":
    temp_list = []
    final_list = []
    
    #TODO: Change to 20
    for i in range(1):
        temp_list = get_25_emails()
        for elem in temp_list:
            final_list.append(elem)
    for j, element in enumerate(final_list):
        res.append({'id': j,'email': element})
            
          
        # click right arrow
        pa.click(right_arrow_pos)
    
    #return/write csv output
    print(final_list)
    with open('asi-connect-scraped-links.csv', 'wb') as f:
        fieldnames = ['id','email']
        writer = csv.DictWriter(f, fieldnames = fieldnames, quoting=csv.QUOTE_ALL)
        writer.writeheader()

        for data in res:
            writer.writerow(data)
            

   

    
