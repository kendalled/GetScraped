# Kendall Jackson MIT License

# GetScraped Private v1

#parse_listing from https://github.com/scrapehero/yellowpages-scraper

#!/usr/bin/env python

# -*- coding: utf-8 -*-

import requests

from lxml import html

import unicodecsv as csv

#import argparse

final_list = []

state = 'AL'

categories = ['Fire Departments']

cities = ['Abbeville','Adamsville','Addison','Akron','Alabaster','Albertville','Alexander City','Alexandria','Aliceville','Allgood','Altoona','Andalusia','Anderson','Anniston','Arab','Ardmore','Argo','Ariton','Arley','Ashford','Ashland','Ashville','Athens','Atmore','Attalla','Auburn','Autaugaville','Avon','Babbie','Baileyton','Banks','Bay Minette','Bayou La Batre','Bear Creek','Beatrice','Beaverton','Belk','Benton','Berry','Bessemer','Billingsley','Birmingham','Black','Blountsville','Blue Mountain','Blue Ridge','Blue Springs','Boaz','Boligee','Bon Air','Branchville','Brantley','Brent','Brewton','Bridgeport','Brighton','Brilliant','Brookside','Brookwood','Brundidge','Butler','Bynum','Cahaba Heights','Calera','Camden','Camp Hill','Carbon Hill','Cardiff','Carolina','Carrollton','Castleberry','Cedar Bluff','Center Point','Centre','Centreville','Chalkville','Chatom','Chelsea','Cherokee','Chickasaw','Childersburg','Citronelle','Clanton','Clay','Clayhatchee','Clayton','Cleveland','Clio','Coaling','Coffee Springs','Coffeeville','Coker','Collinsville','Colony','Columbia','Columbiana','Concord','Coosada','Cordova','Cottonwood','County Line','Courtland','Cowarts','Creola','Crossville','Cuba','Cullman','Dadeville','Daleville','Daphne','Dauphin Island','Daviston','Dayton','Deatsville','Decatur','Demopolis','Detroit','Dodge City','Dora','Dothan','Double Springs','Douglas','Dozier','Dutton','East Brewton','Eclectic','Edgewater','Edwardsville','Elba','Elberta','Eldridge','Elkmont','Elmore','Emelle','Enterprise','Epes','Ethelsville','Eufaula','Eunola','Eutaw','Eva','Evergreen','Excel','Fairfield','Fairhope','Fairview','Falkville','Faunsdale','Fayette','Five Points','Flomaton','Florala','Florence','Foley','Forestdale','Forkland','Fort Deposit','Fort Payne','Fort Rucker','Franklin','Frisco City','Fruithurst','Fulton','Fultondale','Fyffe','Gadsden','Gainesville','Gantt','Gantts Quarry','Garden City','Gardendale','Gaylesville','Geiger','Geneva','Georgiana','Geraldine','Gilbertown','Glen Allen','Glencoe','Glenwood','Goldville','Good Hope','Goodwater','Gordo','Gordon','Gordonville','Goshen','Grand Bay','Grant','Grayson Valley','Graysville','Greensboro','Greenville','Grimes','Grove Hill','Guin','Gulf Shores','Guntersville','Gurley','Gu-Win','Hackleburg','Haleburg','Haleyville','Hamilton','Hammondville','Hanceville','Harpersville','Hartford','Hartselle','Harvest','Hayden','Hayneville','Hazel Green','Headland','Heath','Heflin','Helena','Henagar','Highland Lake','Hillsboro','Hobson City','Hodges','Hokes Bluff','Holly Pond','Hollywood','Holt','Homewood','Hoover','Horn Hill','Hueytown','Huguley','Huntsville','Hurtsboro','Hytop','Ider','Indian Springs Village','Irondale','Jackson','Jacksons Gap','Jacksonville','Jasper','Jemison','Kansas','Kennedy','Killen','Kimberly','Kinsey','Kinston','Ladonia','La Fayette','Lake Purdy','Lakeview','Lake View','Lanett','Langston','Leeds','Leesburg','Leighton','Lester','Level Plains','Lexington','Libertyville','Lincoln','Linden','Lineville','Lipscomb','Lisman','Littleville','Livingston','Loachapoka','Lockhart','Locust Fork','Louisville','Lowndesboro','Loxley','Luverne','Lynn','McDonald Chapel','Macedonia','McIntosh','McKenzie','McMullen','Madison','Madrid','Malvern','Maplesville','Margaret','Marion','Maytown','Meadowbrook','Memphis','Mentone','Meridianville','Midfield','Midland City','Midway','Mignon','Millbrook','Millport','Millry','Minor','Mobile','Monroeville','Montevallo','Montgomery','Moody','Moores Mill','Mooresville','Morris','Mosses','Moulton','Moundville','Mountainboro','Mountain Brook','Mount Olive','Mount Vernon','Mulga','Munford','Muscle Shoals','Myrtlewood','Napier Field','Natural Bridge','Nauvoo','Nectar','Needham','Newbern','New Brockton','New Hope','New Market','New Site','Newton','Newville','North Bibb','North Courtland','North Johns','Northport','Notasulga','Oak Grove','Oak Hill','Oakman','Odenville','Ohatchee','Oneonta','Onycha','Opelika','Opp','Orange Beach','Orrville','Owens Cross Roads','Oxford','Ozark','Paint Rock','Parrish','Pelham','Pell City','Pennington','Petrey','Phenix City','Phil Campbell','Pickensville','Piedmont','Pike Road','Pinckard','Pine Apple','Pine Hill','Pine Ridge','Pinson','Pisgah','Pleasant Grove','Pleasant Groves','Point Clear','Pollard','Powell','Prattville','Priceville','Prichard','Providence','Ragland','Rainbow City','Rainsville','Ranburne','Red Bay','Red Level','Redstone Arsenal','Reece City','Reform','Rehobeth','Repton','Ridgeville','River Falls','Riverside','Riverview','Roanoke','Robertsdale','Rock Creek','Rockford','Rock Mills','Rogersville','Rosa','Russellville','Rutledge','St. Florian','Saks','Samson','Sand Rock','Sanford','Saraland','Sardis City','Satsuma','Scottsboro','Section','Selma','Selmont-West Selmont','Sheffield','Shiloh','Shorter','Silas','Silverhill','Sipsey','Skyline','Slocomb','Smiths','Smoke Rise','Snead','Somerville','Southside','South Vinemont','Spanish Fort','Springville','Steele','Stevenson','Sulligent','Sumiton','Summerdale','Susan Moore','Sweet Water','Sylacauga','Sylvania','Sylvan Springs','Talladega','Talladega Springs','Tallassee','Tarrant','Taylor','Theodore','Thomaston','Thomasville','Thorsby','Tillmans Corner','Town Creek','Toxey','Trafford','Triana','Trinity','Troy','Trussville','Tuscaloosa','Tuscumbia','Tuskegee','Underwood-Petersville','Union','Union Grove','Union Springs','Uniontown','Valley','Valley Head','Vance','Vernon','Vestavia Hills','Vina','Vincent','Vredenburgh','Wadley','Waldo','Walnut Grove','Warrior','Waterloo','Waverly','Weaver','Webb','Wedowee','West Blocton','West End-Cobb Town','West Jefferson','West Point','Wetumpka','White Hall','Wilsonville','Wilton','Winfield','Woodland','Woodville','Yellow Bluff','York']

def parse_listing(keyword,place):

    """



    Function to process yellowpage listing page

    : param keyword: search query

    : param place : place name



    """

    url = "https://www.yellowpages.com/search?search_terms={0}&geo_location_terms={1}".format(keyword,place)

    print("retrieving ",url)



    headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',

                'Accept-Encoding':'gzip, deflate, br',

                'Accept-Language':'en-GB,en;q=0.9,en-US;q=0.8,ml;q=0.7',

                'Cache-Control':'max-age=0',

                'Connection':'keep-alive',

                'Host':'www.yellowpages.com',

                'Upgrade-Insecure-Requests':'1',

                'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'

            }

    # Adding retries

    for retry in range(10):

        try:

            response = requests.get(url,verify=True, headers = headers )

            print("parsing page")

            if response.status_code==200:

                parser = html.fromstring(response.text)

                # making links absolute

                base_url = "https://www.yellowpages.com"

                parser.make_links_absolute(base_url)



                XPATH_LISTINGS = "//div[@class='search-results organic']//div[@class='v-card']"

                listings = parser.xpath(XPATH_LISTINGS)

                scraped_results = []



                for results in listings:

                    XPATH_BUSINESS_NAME = ".//a[@class='business-name']//text()"



                    XPATH_WEBSITE = ".//div[@class='info']//div[contains(@class,'info-section')]//div[@class='links']//a[contains(@class,'website')]/@href"



                    raw_business_name = results.xpath(XPATH_BUSINESS_NAME)



                    raw_website = results.xpath(XPATH_WEBSITE)





                    business_name = ''.join(raw_business_name).strip() if raw_business_name else None



                    website = ''.join(raw_website).strip() if raw_website else None


                    business_details = {

                                        'business_name':business_name,



                                        'website':website,

                                        'industry':keyword,

                                        'city': city,

                                        'state': 'AL'


                    }
                    if(website != '' and website != None):
                        scraped_results.append(business_details)



                #print(scraped_results)

                return scraped_results



            elif response.status_code==404:

                print("Could not find a location matching",place)

                #no need to retry for non existing page

                return []

            else:

                print("Failed to process page")

                return []



        except:

            print("Failed to process page")

            return []





def runtime(word, place):

    keyword = word

    place = place

    scraped_data =  parse_listing(keyword,place)

    if(scraped_data):
        return scraped_data

    else:
        return []


if __name__=="__main__":



    for city in cities:
        final_list = []
        for elem in categories:

            final_list.append(runtime(elem, city + ',' + state))

        print('STARTING FILE WRITE')

        print("Writing scraped data to %s-%s-yellowpages-Fire-links.csv"%(city, state))


        with open('%s-%s-yellowpages-scraped-links.csv'%(city,state),'ab') as csvfile:
            fieldnames = ['business_name', 'website', 'industry', 'city', 'state']

            writer = csv.DictWriter(csvfile, fieldnames = fieldnames, quoting=csv.QUOTE_ALL)

            writer.writeheader()

            for data in final_list:
                for keys in data:
                    writer.writerow(keys)





    print('DONE. Kendall is Awesome.')
