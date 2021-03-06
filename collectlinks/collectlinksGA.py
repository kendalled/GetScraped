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

state = 'GA'

categories = ['Abrasive Dealers','Abundant Life Churches','AC Repairs','Accommodation','Acupuncture','Adhesive','Adoption Centres','Adventure Clubs','Advertising','Advertising Agencies','Advocates','Aerobics','Aeronautical Engineering Colleges','Air And Train Ambulance Services','Air Cargo Agents','Air Conditioners','Air Coolers','Air Hostess Training Institutes','Air Pollution Control Equipment Dealers','Alliance Churches','Alloy, Iron & Steel Industries','Alternative Fuels Stations','Alternative Medicines','Aluminium Extrusion Industry','Ambulance Services','Ammonia Gas Dealers','Amusement Parks','Anglican Churches','Animation Training Institutes','Apostolic Churches','Apparels & Accessories','Apple Product Repair','Aquarium','Architects','Area Rugs & Mats','Armenian Churches','Arms & Ammunition Dealer','Arms And Ammunitions','Art Gallery','Art Paintings','Artificial Grass','Artificial Turf','Arts & Craft Classes','Astrologers','ATM Centres','Audio Video Systems','Auditoriums','Auto Dealers','Auto Service Centres','Automobile Engine Oil Dealers','Automobiles','Aviation Academies','Ayurvedic Food','Ayurvedic Medicines','Ayurvedic Treatment','B 2 B','B Pharmacy Colleges','B.Ed. Colleges','Baby Foods','Baby Store','Bakeries','Bakery Equipments','Balloon Decorations','Bamboo Flooring','Bangles','Banks','Banquet Halls','Baptist Churches','Bar Coding Machine Dealer','Bars','Bathroom Linen','Battery Dealers','BDS Colleges','Bean Bags','Beautician Training Institutes','Beauty & Wellness','Beauty And Cosmetic Products','Beauty Parlours','Bed Linen','Bed Room Furniture','Beef Shops','Belts & Wallets','Bicycle Stores','Bike Rentals','Billing Machine Dealers','Binding','Binoculars & Telescope','Birth Certificate Offices','Blocks Material','Blood Donation Centres','Blow Moulding Machine Dealer','Body Massage Parlours','Boilers','Book Publishers','Books Stores','Bore Well Drilling','Boutiques','Bowling','Brick Materials','Bridal Makeup','Budget Hotels','Building and Construction','Building Demolition','Building Materials','Bulk SMS Modems','Bulk Sms Services','Burqa Retailers','Business Cards','Business Consultants','Business Hotels','CA & ICWA Training Institutes','Cable Manufacturers','Cable Tv Operators','Cabs Services','Cafes','Cake Shops','Calvary Chapel Churches','Camera Accessories','Camera Lens','Cameras','Candles','Caps & Hats','Car Ac Repairs','Car Accessories','Car Dealers','Car Rentals','Car Repairs & Services','Carbon Dioxide Gas Dealers','Cargo & Logistics','Cargo Agents','Carpenters','Carpet & Rugs','Carpet And Carpet Tiles','Casual Dining','Catering Services','Catholic Churches','CBSC Schools','Cement Materials','Central Government Offices','Centreing Materials','Chairs','Chandeliers','Charitable Trusts','Chartered Accountants','Chartered Bus','Chat & Snacks','Chicken Shops','Children Wear','Childrens Hospitals','Chimneys','Snacks','Chit Funds','Chocolate Shops','Churches','Cinema Theaters','Citric Acid Dealers','City Clerk Offices','City Government Offices','Civil Contractors','Cleaning Tools & Accessories','Clinics','Clocks','Cloud Software','Clubs','CNG Pump Stations','Coarse Aggregates','Commercial Kitchen Equipment Dealers','Communication','Competitive Exams','Computer Accessories & Peripherals','Computers','Computers, Tablets & Mobiles','Conference Hall','Construction & Renovation','Construction Companies','Consultants','Contact Lenses','Content Writers','Contractors','Convention Centres','Cooking Classes','Cooks On Hire','Cooktops','Cookware','Corporate Catering Services','Corporate Gifts','Cosmetic Surgery','Couriers','Courts','CPAP & BIPAP Systems','Crackers','Crane Services','Cremation Grounds','Cremation Services','Curtain Accessories','Cushion & Cushion Covers','Cutlery','Dance Academies','Dead Body Freezer Box On Hire','Decor & Lightings','Decor & Show Pieces','Decoration Materials','Degree Colleges','Dental Clinics','Designing & Wood Carving','Detective Agencies','Dhaba','Diagnostic Centres','Diesel Gas Stations','Dietician','Digital Cameras','Digital Printers','Digital Weighing Scale Dealers','Dining','Dining Room Furniture','Dining Sets','Disc Jockey Training Institutes','Dishwasher','Diwan Sets','Doctors','Dog Training','Doors, Windows & Partitions','Drama Theaters','Dress Materials','Drilling Equipments','Driver Service Agents','Dry Fruits','Dry Ice Dealer','DSLR Cameras','DTP Services','Dvd & Vcd','Eastern Orthodox Churches','Education','Education Colleges','Education Consultants','Education Councils & Board Offices','Education Schools','Egg Shops','Electrical Contractors','Electrical Sub-Stations','Electrical Suppliers','Electricians','Electronic Accessories','Electronic Display Boards Manufacturer','Electronic Weighing Scale Dealers','Electronics','Elevators','Email Marketing','Embroidery Works','Emergency Services','Engineering Colleges','ENT Hospitals','Entrance Exams Coaching Centres','Establishments','Ethnic Wear','Evangelical Churches','Event Decorators','Event Management','Event Organizers','Event Venues','Events Catering Services','Excavation','Eye Hospitals','Eyeglasses','Fabrication & Welding Works','False Ceiling','Family Clubs','Fans','Farm Houses','Fashion Designers','Fashion Designing Training Institutes','Fast Food Centre','Fertility & Infertility Clinics','Fertilizer & Soil','Film And Television Institute Of India','Film Studios','Financial Planners','Financial Services','Fine Dining','Fire Alarms','Fire And Safety Course Training','Fire Extinguishers','Fire Protection Systems','Fire Safety Equipments','Fire Stations','Fish & Sea Food Shops','Fitness Centres','Flex Printing Services','Flooring','Flooring Installations','Flooring Tools & Materials','Florists','Flower Decorations','Food & Beverage Outlets','Food & Beverages','Food Courts','Food Machinery Manufacturer','Food Processing Equipment Manufacturer','Food Stores','Footwear','Foreign Exchange','Foursquare Churches','Frames','Fruit Juice Processing Machine Manufacture','Fruits','Full Gospel Churches','Function Halls','Funeral Band','Funeral Materials','Furnishings','Furniture','Furniture on Hire','Furniture Storage','Gaming Centres','Gardening Tools','Garments','Gas Dealers','Gas Stations','Gemological Institute Of India','General Hospitals','General order suppliers','General Pharmacies','GI Pipe Dealer','Gifts And Novelties','Glass Fitting Hardware','Glasswares','Go Karting','Goldsmiths','Gospel Churches','Government Hospitals','Government Offices','Graphic Designers','GRE & TOEFL Coaching Centres','Greek Orthodox Churches','Groceries','Groundwater Surveyors','Guest Houses','Gurudwaras','Water Heater Repair','Gymnasium','Gymnasium Equipments','Hair Fall Treatments','Hair Stylists','Hair Transplantation','Hair Treatments','Hall Decorations','Handicraft Items','Handlooms','Hardware And Network Training Institutes','Hardware And Networking','Hardware Stores','Hardware Tools','Hardwood Flooring','HD Cameras','Health','Health Clubs','Hearse Services','Heavy Vehicle Dealers','Helmet Dealers','Hispanic Churches','Home Appliances','Home Builders','Home Delivery Restaurants','Home Furniture','Home Needs','Home Theater Systems','Homeopathy Clinics','Homeopathy Medicines','Hosiery Store','Hospitals','Hotels','House Painters','Housekeeping Services','Hr Consultancies','Hydraulic & Pulley Equipment Dealers','Hydrochloric Acid Dealers','Hypermarkets','IB Schools','Ice Cream & Dessert Parlors','ICSE Schools','IGCSE Schools','Immigration Consultants','Income Tax Offices','Industrial Bearing Dealers','Industrial Belt Dealers','Industrial Burner Dealers','Industrial Chemical Dealers','Industrial Electronic Components Dealers','Industrial Equipments','Industrial Fan Dealers','Industrial Fire Extinguisher Dealers','industrial machine dealers','Industrial Safety Equipment Dealers','Industrial Spring Dealers','Industrial Trolleys Manufacturer','Innerwear And Loungewear','Institute Of Hotel Management','Insurance Agents','Interior Design Courses','Interior Designers','Internet Service Providers','Inverters','Investment Advisors','Irrigation Equipment Dealers','ITI Training','Jain Temples','Jeans','Jewellery','Jewellery Box Manufacturers','Journalism Training Institutes','Juice Centre','Junior Colleges','Kalyana Mandapam','Kennels','Kitchen & Dining','Kitchen Storage Containers','Lab Equipment And Chemical Suppliers','Labor Contractors','Laboratories','Ladies Bags & Purses','Ladies Dresses','Laminate Flooring','Language Training Institutes','Laptop Repair','Laptops','Lathe Machine Dealers','Laundry Services','Law Colleges','Lawn & Garden','Leather Goods Manufacturer','Legal & Financial Services','Legal Services','Libraries','Lifestyle Accessories','Lightings','Living Room Furniture','Loan Agencies','Loan Agents','Local Government Offices','Locks','Lodges','Logistic Companies','Logistics Services','Lounges','Luxury Hotels','Maggam Job Works','Makeup Artists','Manufacturer of Power Generators','Marriage Bureaus','Marriage Halls','Mass Communication & Journalism Colleges','Matching Centres','Maternity Hospitals','Mattresses','Meat & Poultry Shops','Media Advertising','Medical Coding Training Institutes','Medical Colleges','Medical Equipments','Medical Stockings','Meditation Centres','Mehandi Artists','Mennonite Churches','Mens Hostels','Mesh Dealers','Metal Industries','Methodist Churches','Metro Rail Stations','Microbreweries','Microwave Repairs','Military Recruiting Offices','Milk & Milk Products','Mineral Water Suppliers','Mobile Phones','Mobile Repairs','Mobile Repairs','Modular Furniture','Modular Kitchen Dealers','Money Transfer Agencies','Montessori Training Institutes','Moravian Churches','Morgues Services','Mormon Churches','Mosques','Motor Driving Schools','Mould Dies Manufacturer','Moving Media Ads','Mp3 Players','MS Pipe Dealer','Multispecialty Hospitals','Museums','Music Academies','Musical Instruments','Mutton Shops','Natural Flooring','Nature Cure Centers','Naturopathy','Network Securities','Networking Devices','New Age Churches','Newspaper Ads','NGO Clubs','NGOs & Social Service Organisations','Night Clubs','Night Life','Night Wears','Nitric Acid Dealers','Notary Services','Number Plate Manufacturers','Nursing Colleges','Nutritional Supplement Dealers','Office Furniture','Offices','Offset Printers','Old Age Homes','Old Cut Notes Exchange Services','Online Classes','Optics & Eyewear','Organ Donation Centres','Orphanages & Shelters','Orthodox Churches','Other Vehicles','Outdoor Advertising','Outdoor Catering Services','Outdoor Furniture','Overseas Education Consultants','Oxygen Concentrators','Oxygen Gas Dealers','P R P Hair Treatments','Packers And Movers','Packing Machine Manufacturers','Painters','Painting Suppliers','Pan Shops','Pants','Paper Rolls Manufacturers','Paper Stores','Parks','Part Time Jobs Consultancies','Party Halls','Passport Offices','Pawn Brokers','Pcs & Desktops','Pedicure & Manicure','Pen Stores','Pentecostal Churches','Perforated Sheet Manufacturers','Perfumes','Personal Fitness Trainers','Personality Development Training Institutes','Pest Control Services','Pet Shops','Pets','PG Colleges','Pharmaceutical Companies','Pharmaceutical Packaging Material Dealers','Pharmacies','Pharmacy Colleges','Photo Frames','Photo Studios','Photocopiers','Photographers','Photography Training Institutes','physiotherapist','Physiotherapy Clinics','Piercing','Pilot Training Institutes','Pipe Dealers','Pizza Restaurants','Placement Consultants','Plants','Plastic & Disposable Items','Plastic Injection Moulding Machine Dealer','Plastic Products Manufacturers','Play Schools','Play Stations','Playground Equipments','Playgrounds','Plumbers','Plumbing','Plywood & Laminates','Police Stations','Political Party Offices','Pollution Inspection Stations','Polymers & Asbestos Products Dealer','Polytechnic Colleges','Pork Shops','Post Offices','Power Generator Suppliers','Power Stations','Power Tools Dealers','Presbyterian Churches','Printed Circuit Board Dealers','Printers','Printing & Stationaries','Printing Machines','Printing Materials','Printing Press','Professional Services','Professionals','Project Management Training Institutes','Projectors','Promotional Products','Property Consultants','Property Dealers','Protestant Churches','Public Safety Offices','Pubs','Pumps & Controllers','Pundits','PVC Pipe Dealer','Quaker Churches','Quick Bites','Radio Jockey Training Institutes','Radio Stations','Radium Works','Railings','Railway Cargo Agents','Railway Stations','Ready Made Garments','Ready Mix Concrete','Real Estate','Real Estate Agents','Real Estate Developers','Real Estate Loans & Mortgages','Recording Studios','Reformed Churches','Refrigerator Repair','Refrigerators','Registry Offices','Rehabilitation Centres','Religion','Research Institutes','Residential Designers','Resins & Chemicals Manufacturer','Resorts','Restaurant Test','Restaurants','RO Water Purifier','Road Cargo Agents','Robotics Engineering','Robotics Training Institutes','Roofing Sheets','RTA Offices','Rubber Oil Seals Dealer','Rubber Product Dealer','Rubber Product Manufacturers','Rubber Stamps','Rudraksha','Russian Orthodox Churches','Sand Materials','Sandals & Floaters','Sanitaryware & Bathroom Accessories','Sarees & Blouses','Scalp Treatments','School District Offices','School For Mentally Challenged','Scrap Dealers','Screen Printers','Sea Cargo Agents','Seat Cover & Rexine Works','Security Guard Services','Security Services','Security Systems','Seeds','SelfDefence Training Services','Servers','Service Centres','Serviced Apartments','Seventh-Day Adventist Churches','Sewing Machine Dealers','Share Brokers','Shipping Companies','Shirts','Shoes','Shopping Malls','Shorts & Cargo','Sign Boards','Signage','Singing Classes','Skin Care Clinics','Snooker Parlours','Socks','Sofa Sets','Software & IT Services','Software Certifications','Software Dealers','Software Development','Software Training Institutes','Solar Products Manufacturers','Sound And Lighting On Hire','Sound Systems','Spa & Saloon','Spare Part Dealers','Spare Parts & Accessories','Speakers','Spiritual And Pooja Accessories','Spiritual Centres','Spoken English Institutes','Sports','Sports Academies','Sports Clubs','Sports Equipments','Sports Stores','Sports Wear','Sports, Entertainment & Hobbies','Stadiums','Stage Decorations','Stainless Steel Pipe Dealer','Stamp Papers','Standees & Demo Tents','State Board Schools','State Government Offices','Stationaries','Stationary Stores','Stations','Steel Wires & Ropes Manufacturers','Stem Cell Banking','Stock Brokers','Studios','Study Hall Centre','Sub-Registrar Offices','Suitings & Shirtings','Suits And Blazers','Sulphuric Acid Dealers','Sunglasses','Super Specialty Hospitals','Supermarkets','Surgical Instruments','Sweet Shops','Swimming Pools','Table Accessories','Tailoring Materials','Tailors','Tailors & Designers','Take Away Restaurants','Tattoo Makers','Telecommunications','Television Installation','Televisions','Temples','Tent Houses','Textiles','Theaters','Theme Parks','Thermocol Dealers','Ticketing','Tiles','Timber Depot','Tmt Iron & Steel Bars','Tours And Travels','Toy Shops','Trading Consultants','Training Institutes','Transportation','Travel Agencies','Travel Goods','Travel Services','Trophy & Momento Dealers','Trousers','T-Shirts','Tuitions','Tv Accessories','TV Studio','Two Wheelers Dealers','Two Wheelers Service Centres','Typing Institutes','Tyre Dealers','Unani Treatment','Underground Stations','Uniforms','Unitarian Universalist Churches','United Churches Of Christ','Unity Churches','Universities','UPS','UPSC & IAS Coaching Centres','Used Auto Dealers','Used Bike Dealers','Used Cars Dealers','Utensils','UV Water Purifier','Valve Dealer','Vegetables','Vehicle Glass Dealers','Vehicle On Hire','Vending Machine Manufacturer','Veterinary Hospitals','Veterinary Medicines','Video Editing Studios','Video Gaming Centres','Videographers','Vineyard Churches','Vinyl Flooring','Vocational Colleges','Wall Papers','Washing Machine Repair','Washing Machines','Water Cooler Suppliers','Water Parks','Water Purifier Dealers','Water Purifier Repairs','Water Softeners','Water Suppliers','Water Tank Suppliers','Waterproofing','Waterproofing Materials','Weather Stations','Web Designing Companies','Web Hosting Companies','Wedding & Events','Wedding Bands','Wedding Cards','Wedding Catering Services','Wedding Decorations','Wedding Planners','Weight Loss & Gain Centres','Welding Equipment','Welfare Offices','Wesleyan Churches','Wet Grinder Dealers','Wine Shops','Winter Wear','Wire Mesh Dealers','Womens Hostels','Wooden Flooring','Wrist Watch Repairs and Services','Wrist Watches','Xerox Shops','Yoga Centres','Zoo Parks','Zumba Fitness']

cities = ['Abbeville','Acworth','Adairsville','Adel','Adrian','Ailey','Alamo','Alapaha','Albany','Aldora','Allenhurst','Allentown','Alma','Alpharetta','Alston','Alto','Ambrose','Americus','Andersonville','Arabi','Aragon','Arcade','Argyle','Arlington','Arnoldsville','Ashburn','Athens-Clarke County (balance)','Atlanta','Attapulgus','Auburn','Augusta-Richmond County (balance)','Austell','Avalon','Avera','Avondale Estates','Baconton','Bainbridge','Baldwin','Ball Ground','Barnesville','Bartow','Barwick','Baxley','Bellville','Belvedere Park','Berkeley Lake','Berlin','Bethlehem','Between','Bibb City','Bishop','Blackshear','Blacksville','Blairsville','Blakely','Bloomingdale','Blue Ridge','Bluffton','Blythe','Bogart','Bonanza','Boston','Bostwick','Bowdon','Bowersville','Bowman','Braselton','Braswell','Bremen','Brinson','Bronwood','Brooklet','Brooks','Broxton','Brunswick','Buchanan','Buckhead','Buena Vista','Buford','Butler','Byromville','Byron','Cadwell','Cairo','Calhoun','Camak','Camilla','Candler-McAfee','Canon','Canton','Carl','Carlton','Carnesville','Carrollton','Cartersville','Cave Spring','Cecil','Cedartown','Centerville','Centralhatchee','Chamblee','Chatsworth','Chattanooga Valley','Chauncey','Chester','Chickamauga','Clarkesville','Clarkston','Claxton','Clayton','Clermont','Cleveland','Climax','Cobbtown','Cochran','Cohutta','Colbert','Coleman','College Park','Collins','Colquitt','Columbus city (balance)','Comer','Commerce','Concord','Conley','Conyers','Coolidge','Cordele','Corinth','Cornelia','Country Club Estates','Covington','Crawford','Crawfordville','Culloden','Cumming','Cusseta','Cuthbert','Dacula','Dahlonega','Daisy','Dallas','Dalton','Damascus','Danielsville','Danville','Darien','Dasher','Davisboro','Dawson','Dawsonville','Dearing','Decatur','Deenwood','Deepstep','Demorest','Denton','De Soto','Dexter','Dillard','Dock Junction','Doerun','Donalsonville','Dooling','Doraville','Douglas','Douglasville','Druid Hills','Dublin','Dudley','Duluth','Dunwoody','Du Pont','East Dublin','East Ellijay','East Griffin','Eastman','East Newnan','East Point','Eatonton','Edge Hill','Edison','Elberton','Ellaville','Ellenton','Ellijay','Emerson','Enigma','Ephesus','Eton','Euharlee','Evans','Experiment','Fairburn','Fairmount','Fair Oaks','Fairview','Fargo','Fayetteville','Fitzgerald','Flemington','Flovilla','Flowery Branch','Folkston','Forest Park','Forsyth','Fort Benning South','Fort Gaines','Fort Oglethorpe','Fort Stewart','Fort Valley','Franklin','Franklin Springs','Funston','Gainesville','Garden City','Garfield','Gay','Geneva','Georgetown','Georgetown','Gibson','Gillsville','Girard','Glennville','Glenwood','Good Hope','Gordon','Graham','Grantville','Gray','Grayson','Greensboro','Greenville','Gresham Park','Griffin','Grovetown','Gumbranch','Gumlog','Guyton','Hagan','Hahira','Hamilton','Hampton','Hannahs Mill','Hapeville','Haralson','Harlem','Harrison','Hartwell','Hawkinsville','Hazlehurst','Helen','Helena','Hephzibah','Hiawassee','Higgston','Hilltop','Hiltonia','Hinesville','Hiram','Hoboken','Hogansville','Holly Springs','Homeland','Homer','Homerville','Hoschton','Hull','Ideal','Ila','Indian Springs','Iron City','Irondale','Irwinton','Isle of Hope','Ivey','Jackson','Jacksonville','Jakin','Jasper','Jefferson','Jeffersonville','Jenkinsburg','Jersey','Jesup','Jonesboro','Junction City','Kennesaw','Keysville','Kings Bay Base','Kingsland','Kingston','Kite','La Fayette','LaGrange','Lake City','Lakeland','Lake Park','Lakeview','Lakeview Estates','Lavonia','Lawrenceville','Leary','Leesburg','Lenox','Leslie','Lexington','Lilburn','Lilly','Lincoln Park','Lincolnton','Lindale','Lithia Springs','Lithonia','Locust Grove','Loganville','Lone Oak','Lookout Mountain','Louisville','Lovejoy','Ludowici','Lula','Lumber City','Lumpkin','Luthersville','Lyerly','Lyons','Mableton','McCaysville','McDonough','McIntyre','Macon','McRae','Madison','Manassas','Manchester','Mansfield','Marietta','Marshallville','Martin','Martinez','Maxeys','Maysville','Meansville','Meigs','Menlo','Metter','Midville','Midway','Midway-Hardwick','Milan','Milledgeville','Millen','Milner','Mitchell','Molena','Monroe','Montezuma','Montgomery','Monticello','Montrose','Moody AFB','Moreland','Morgan','Morganton','Morrow','Morven','Moultrie','Mountain City','Mountain Park','Mountain Park','Mount Airy','Mount Vernon','Mount Zion','Nahunta','Nashville','Nelson','Newborn','Newington','Newnan','Newton','Nicholls','Nicholson','Norcross','Norman Park','North Atlanta','North Decatur','North Druid Hills','North High Shoals','Norwood','Nunez','Oak Park','Oakwood','Ochlocknee','Ocilla','Oconee','Odum','Offerman','Oglethorpe','Oliver','Omega','Orchard Hill','Oxford','Palmetto','Panthersville','Parrott','Patterson','Pavo','Payne','Peachtree City','Pearson','Pelham','Pembroke','Pendergrass','Perry','Phillipsburg','Pinehurst','Pine Lake','Pine Mountain','Pineview','Pitts','Plains','Plainville','Pooler','Portal','Porterdale','Port Wentworth','Poulan','Powder Springs','Preston','Pulaski','Putney','Quitman','Ranger','Raoul','Ray City','Rayle','Rebecca','Redan','Reed Creek','Register','Reidsville','Remerton','Rentz','Resaca','Rest Haven','Reynolds','Rhine','Riceboro','Richland','Richmond Hill','Riddleville','Rincon','Ringgold','Riverdale','Riverside','Roberta','Robins AFB','Rochelle','Rockmart','Rocky Ford','Rome','Roopville','Rossville','Roswell','Royston','Rutledge','St. Marys','St. Simons','Sale City','Salem','Sandersville','Sandy Springs','Santa Claus','Sardis','Sasser','Savannah','Scotland','Scottdale','Screven','Senoia','Shady Dale','Shannon','Sharon','Sharpsburg','Shellman','Shiloh','Siloam','Skidaway Island','Sky Valley','Smithville','Smyrna','Snellville','Social Circle','Soperton','Sparks','Sparta','Springfield','Stapleton','Statesboro','Statham','Stillmore','Stockbridge','Stone Mountain','Sugar Hill','Summertown','Summerville','Sumner','Sunny Side','Sunnyside','Sunset Village','Surrency','Suwanee','Swainsboro','Sycamore','Sylvania','Sylvester','Talbotton','Talking Rock','Tallapoosa','Tallulah Falls','Talmo','Tarrytown village','Taylorsville','Temple','Tennille','Thomaston','Thomasville','Thomson','Thunderbolt','Tifton','Tiger','Tignall','Toccoa','Toomsboro','Trenton','Trion','Tucker','Tunnel Hill','Turin','Twin City','Tybee Island','Tyrone','Ty Ty','Unadilla','Union City','Union Point','Unionville','Uvalda','Valdosta','Varnell','Vernonburg','Vidalia','Vidette','Vienna','Villa Rica','Vinings','Waco','Wadley','Waleska','Walnut Grove','Walthourville','Warm Springs','Warner Robins','Warrenton','Warwick','Washington','Watkinsville','Waverly Hall','Waycross','Waynesboro','Weston','West Point','Whigham','White','Whitemarsh Island','White Plains','Whitesburg','Willacoochee','Williamson','Wilmington Island','Winder','Winterville','Woodbine','Woodbury','Woodland','Woodstock','Woodville','Woolsey','Wrens','Wrightsville','Yatesville','Young Harris','Zebulon']

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

                #making links absolute

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

                                        'state': 'Georgia'


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

        print("Writing scraped data to %s-%s-yellowpages-scraped-links.csv"%(city, state))


        with open('%s-%s-yellowpages-scraped-links.csv'%(city,state),'ab') as csvfile:
            fieldnames = ['business_name', 'website', 'industry', 'city', 'state']

            writer = csv.DictWriter(csvfile, fieldnames = fieldnames, quoting=csv.QUOTE_ALL)

            writer.writeheader()

            for data in final_list:
                for keys in data:
                    writer.writerow(keys)





    print('DONE. Kendall is Awesome.')
