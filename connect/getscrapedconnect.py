# GetScrapedConnect V0.0.1 (ASI Connect - Windows Build)
# github.com/kendalled

import clipboard
import unicodecsv as csv
#import pyautogui as pa

# Element references
asi_number_pos = (250, 250)
extension_pos = (256, 256)
copy_pos = (123, 123)
right_arrow_pos = (321, 321)

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
    # Removing ASI emails, empty elements, and ad text
    listy = list(filter(('').__ne__, stringy.split('\n')))
    listy.remove(ad_text)
    listy.remove(asi_email1)
    listy.remove(asi_email2)
    print(listy)
    return(listy)

def get_100_emails():
    clipped_data = ''
    for i in range(100):
        #TODO: Click Red asi number (right end)
        pa.click(asi_number_pos)
        #TODO: Scroll down slightly
        
        # rinses and repeats x 100
    
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
    for i in range(3):
        temp_list = get_100_emails()
        for elem in temp_list:
            final_list.append(elem)
          
        # then, click right arrow
        pa.click(right_arrow_pos)
    
    #TODO: return/write csv output
    print(final_list)

   

    