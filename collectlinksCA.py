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

state = 'CA'

categories = ['Abrasive Dealers','Abundant Life Churches','AC Repairs','Accommodation','Acupuncture','Adhesive','Adoption Centres','Adventure Clubs','Advertising','Advertising Agencies','Advocates','Aerobics','Aeronautical Engineering Colleges','Air And Train Ambulance Services','Air Cargo Agents','Air Conditioners','Air Coolers','Air Hostess Training Institutes','Air Pollution Control Equipment Dealers','Alliance Churches','Alloy, Iron & Steel Industries','Alternative Fuels Stations','Alternative Medicines','Aluminium Extrusion Industry','Ambulance Services','Ammonia Gas Dealers','Amusement Parks','Anglican Churches','Animation Training Institutes','Apostolic Churches','Apparels & Accessories','Apple Product Repair','Aquarium','Architects','Area Rugs & Mats','Armenian Churches','Arms & Ammunition Dealer','Arms And Ammunitions','Art Gallery','Art Paintings','Artificial Grass','Artificial Turf','Arts & Craft Classes','Astrologers','ATM Centres','Audio Video Systems','Auditoriums','Auto Dealers','Auto Service Centres','Automobile Engine Oil Dealers','Automobiles','Aviation Academies','Ayurvedic Food','Ayurvedic Medicines','Ayurvedic Treatment','B 2 B','B Pharmacy Colleges','B.Ed. Colleges','Baby Foods','Baby Store','Bakeries','Bakery Equipments','Balloon Decorations','Bamboo Flooring','Bangles','Banks','Banquet Halls','Baptist Churches','Bar Coding Machine Dealer','Bars','Bathroom Linen','Battery Dealers','BDS Colleges','Bean Bags','Beautician Training Institutes','Beauty & Wellness','Beauty And Cosmetic Products','Beauty Parlours','Bed Linen','Bed Room Furniture','Beef Shops','Belts & Wallets','Bicycle Stores','Bike Rentals','Billing Machine Dealers','Binding','Binoculars & Telescope','Birth Certificate Offices','Blocks Material','Blood Donation Centres','Blow Moulding Machine Dealer','Body Massage Parlours','Boilers','Book Publishers','Books Stores','Bore Well Drilling','Boutiques','Bowling','Brick Materials','Bridal Makeup','Budget Hotels','Building and Construction','Building Demolition','Building Materials','Bulk SMS Modems','Bulk Sms Services','Burqa Retailers','Business Cards','Business Consultants','Business Hotels','CA & ICWA Training Institutes','Cable Manufacturers','Cable Tv Operators','Cabs Services','Cafes','Cake Shops','Calvary Chapel Churches','Camera Accessories','Camera Lens','Cameras','Candles','Caps & Hats','Car Ac Repairs','Car Accessories','Car Dealers','Car Rentals','Car Repairs & Services','Carbon Dioxide Gas Dealers','Cargo & Logistics','Cargo Agents','Carpenters','Carpet & Rugs','Carpet And Carpet Tiles','Casual Dining','Catering Services','Catholic Churches','CBSC Schools','Cement Materials','Central Government Offices','Centreing Materials','Chairs','Chandeliers','Charitable Trusts','Chartered Accountants','Chartered Bus','Chat & Snacks','Chicken Shops','Children Wear','Childrens Hospitals','Chimneys','Snacks','Chit Funds','Chocolate Shops','Churches','Cinema Theaters','Citric Acid Dealers','City Clerk Offices','City Government Offices','Civil Contractors','Cleaning Tools & Accessories','Clinics','Clocks','Cloud Software','Clubs','CNG Pump Stations','Coarse Aggregates','Commercial Kitchen Equipment Dealers','Communication','Competitive Exams','Computer Accessories & Peripherals','Computers','Computers, Tablets & Mobiles','Conference Hall','Construction & Renovation','Construction Companies','Consultants','Contact Lenses','Content Writers','Contractors','Convention Centres','Cooking Classes','Cooks On Hire','Cooktops','Cookware','Corporate Catering Services','Corporate Gifts','Cosmetic Surgery','Couriers','Courts','CPAP & BIPAP Systems','Crackers','Crane Services','Cremation Grounds','Cremation Services','Curtain Accessories','Cushion & Cushion Covers','Cutlery','Dance Academies','Dead Body Freezer Box On Hire','Decor & Lightings','Decor & Show Pieces','Decoration Materials','Degree Colleges','Dental Clinics','Designing & Wood Carving','Detective Agencies','Dhaba','Diagnostic Centres','Diesel Gas Stations','Dietician','Digital Cameras','Digital Printers','Digital Weighing Scale Dealers','Dining','Dining Room Furniture','Dining Sets','Disc Jockey Training Institutes','Dishwasher','Diwan Sets','Doctors','Dog Training','Doors, Windows & Partitions','Drama Theaters','Dress Materials','Drilling Equipments','Driver Service Agents','Dry Fruits','Dry Ice Dealer','DSLR Cameras','DTP Services','Dvd & Vcd','Eastern Orthodox Churches','Education','Education Colleges','Education Consultants','Education Councils & Board Offices','Education Schools','Egg Shops','Electrical Contractors','Electrical Sub-Stations','Electrical Suppliers','Electricians','Electronic Accessories','Electronic Display Boards Manufacturer','Electronic Weighing Scale Dealers','Electronics','Elevators','Email Marketing','Embroidery Works','Emergency Services','Engineering Colleges','ENT Hospitals','Entrance Exams Coaching Centres','Establishments','Ethnic Wear','Evangelical Churches','Event Decorators','Event Management','Event Organizers','Event Venues','Events Catering Services','Excavation','Eye Hospitals','Eyeglasses','Fabrication & Welding Works','False Ceiling','Family Clubs','Fans','Farm Houses','Fashion Designers','Fashion Designing Training Institutes','Fast Food Centre','Fertility & Infertility Clinics','Fertilizer & Soil','Film And Television Institute Of India','Film Studios','Financial Planners','Financial Services','Fine Dining','Fire Alarms','Fire And Safety Course Training','Fire Extinguishers','Fire Protection Systems','Fire Safety Equipments','Fire Stations','Fish & Sea Food Shops','Fitness Centres','Flex Printing Services','Flooring','Flooring Installations','Flooring Tools & Materials','Florists','Flower Decorations','Food & Beverage Outlets','Food & Beverages','Food Courts','Food Machinery Manufacturer','Food Processing Equipment Manufacturer','Food Stores','Footwear','Foreign Exchange','Foursquare Churches','Frames','Fruit Juice Processing Machine Manufacture','Fruits','Full Gospel Churches','Function Halls','Funeral Band','Funeral Materials','Furnishings','Furniture','Furniture on Hire','Furniture Storage','Gaming Centres','Gardening Tools','Garments','Gas Dealers','Gas Stations','Gemological Institute Of India','General Hospitals','General order suppliers','General Pharmacies','GI Pipe Dealer','Gifts And Novelties','Glass Fitting Hardware','Glasswares','Go Karting','Goldsmiths','Gospel Churches','Government Hospitals','Government Offices','Graphic Designers','GRE & TOEFL Coaching Centres','Greek Orthodox Churches','Groceries','Groundwater Surveyors','Guest Houses','Gurudwaras','Water Heater Repair','Gymnasium','Gymnasium Equipments','Hair Fall Treatments','Hair Stylists','Hair Transplantation','Hair Treatments','Hall Decorations','Handicraft Items','Handlooms','Hardware And Network Training Institutes','Hardware And Networking','Hardware Stores','Hardware Tools','Hardwood Flooring','HD Cameras','Health','Health Clubs','Hearse Services','Heavy Vehicle Dealers','Helmet Dealers','Hispanic Churches','Home Appliances','Home Builders','Home Delivery Restaurants','Home Furniture','Home Needs','Home Theater Systems','Homeopathy Clinics','Homeopathy Medicines','Hosiery Store','Hospitals','Hotels','House Painters','Housekeeping Services','Hr Consultancies','Hydraulic & Pulley Equipment Dealers','Hydrochloric Acid Dealers','Hypermarkets','IB Schools','Ice Cream & Dessert Parlors','ICSE Schools','IGCSE Schools','Immigration Consultants','Income Tax Offices','Industrial Bearing Dealers','Industrial Belt Dealers','Industrial Burner Dealers','Industrial Chemical Dealers','Industrial Electronic Components Dealers','Industrial Equipments','Industrial Fan Dealers','Industrial Fire Extinguisher Dealers','industrial machine dealers','Industrial Safety Equipment Dealers','Industrial Spring Dealers','Industrial Trolleys Manufacturer','Innerwear And Loungewear','Institute Of Hotel Management','Insurance Agents','Interior Design Courses','Interior Designers','Internet Service Providers','Inverters','Investment Advisors','Irrigation Equipment Dealers','ITI Training','Jain Temples','Jeans','Jewellery','Jewellery Box Manufacturers','Journalism Training Institutes','Juice Centre','Junior Colleges','Kalyana Mandapam','Kennels','Kitchen & Dining','Kitchen Storage Containers','Lab Equipment And Chemical Suppliers','Labor Contractors','Laboratories','Ladies Bags & Purses','Ladies Dresses','Laminate Flooring','Language Training Institutes','Laptop Repair','Laptops','Lathe Machine Dealers','Laundry Services','Law Colleges','Lawn & Garden','Leather Goods Manufacturer','Legal & Financial Services','Legal Services','Libraries','Lifestyle Accessories','Lightings','Living Room Furniture','Loan Agencies','Loan Agents','Local Government Offices','Locks','Lodges','Logistic Companies','Logistics Services','Lounges','Luxury Hotels','Maggam Job Works','Makeup Artists','Manufacturer of Power Generators','Marriage Bureaus','Marriage Halls','Mass Communication & Journalism Colleges','Matching Centres','Maternity Hospitals','Mattresses','Meat & Poultry Shops','Media Advertising','Medical Coding Training Institutes','Medical Colleges','Medical Equipments','Medical Stockings','Meditation Centres','Mehandi Artists','Mennonite Churches','Mens Hostels','Mesh Dealers','Metal Industries','Methodist Churches','Metro Rail Stations','Microbreweries','Microwave Repairs','Military Recruiting Offices','Milk & Milk Products','Mineral Water Suppliers','Mobile Phones','Mobile Repairs','Mobile Repairs','Modular Furniture','Modular Kitchen Dealers','Money Transfer Agencies','Montessori Training Institutes','Moravian Churches','Morgues Services','Mormon Churches','Mosques','Motor Driving Schools','Mould Dies Manufacturer','Moving Media Ads','Mp3 Players','MS Pipe Dealer','Multispecialty Hospitals','Museums','Music Academies','Musical Instruments','Mutton Shops','Natural Flooring','Nature Cure Centers','Naturopathy','Network Securities','Networking Devices','New Age Churches','Newspaper Ads','NGO Clubs','NGOs & Social Service Organisations','Night Clubs','Night Life','Night Wears','Nitric Acid Dealers','Notary Services','Number Plate Manufacturers','Nursing Colleges','Nutritional Supplement Dealers','Office Furniture','Offices','Offset Printers','Old Age Homes','Old Cut Notes Exchange Services','Online Classes','Optics & Eyewear','Organ Donation Centres','Orphanages & Shelters','Orthodox Churches','Other Vehicles','Outdoor Advertising','Outdoor Catering Services','Outdoor Furniture','Overseas Education Consultants','Oxygen Concentrators','Oxygen Gas Dealers','P R P Hair Treatments','Packers And Movers','Packing Machine Manufacturers','Painters','Painting Suppliers','Pan Shops','Pants','Paper Rolls Manufacturers','Paper Stores','Parks','Part Time Jobs Consultancies','Party Halls','Passport Offices','Pawn Brokers','Pcs & Desktops','Pedicure & Manicure','Pen Stores','Pentecostal Churches','Perforated Sheet Manufacturers','Perfumes','Personal Fitness Trainers','Personality Development Training Institutes','Pest Control Services','Pet Shops','Pets','PG Colleges','Pharmaceutical Companies','Pharmaceutical Packaging Material Dealers','Pharmacies','Pharmacy Colleges','Photo Frames','Photo Studios','Photocopiers','Photographers','Photography Training Institutes','physiotherapist','Physiotherapy Clinics','Piercing','Pilot Training Institutes','Pipe Dealers','Pizza Restaurants','Placement Consultants','Plants','Plastic & Disposable Items','Plastic Injection Moulding Machine Dealer','Plastic Products Manufacturers','Play Schools','Play Stations','Playground Equipments','Playgrounds','Plumbers','Plumbing','Plywood & Laminates','Police Stations','Political Party Offices','Pollution Inspection Stations','Polymers & Asbestos Products Dealer','Polytechnic Colleges','Pork Shops','Post Offices','Power Generator Suppliers','Power Stations','Power Tools Dealers','Presbyterian Churches','Printed Circuit Board Dealers','Printers','Printing & Stationaries','Printing Machines','Printing Materials','Printing Press','Professional Services','Professionals','Project Management Training Institutes','Projectors','Promotional Products','Property Consultants','Property Dealers','Protestant Churches','Public Safety Offices','Pubs','Pumps & Controllers','Pundits','PVC Pipe Dealer','Quaker Churches','Quick Bites','Radio Jockey Training Institutes','Radio Stations','Radium Works','Railings','Railway Cargo Agents','Railway Stations','Ready Made Garments','Ready Mix Concrete','Real Estate','Real Estate Agents','Real Estate Developers','Real Estate Loans & Mortgages','Recording Studios','Reformed Churches','Refrigerator Repair','Refrigerators','Registry Offices','Rehabilitation Centres','Religion','Research Institutes','Residential Designers','Resins & Chemicals Manufacturer','Resorts','Restaurant Test','Restaurants','RO Water Purifier','Road Cargo Agents','Robotics Engineering','Robotics Training Institutes','Roofing Sheets','RTA Offices','Rubber Oil Seals Dealer','Rubber Product Dealer','Rubber Product Manufacturers','Rubber Stamps','Rudraksha','Russian Orthodox Churches','Sand Materials','Sandals & Floaters','Sanitaryware & Bathroom Accessories','Sarees & Blouses','Scalp Treatments','School District Offices','School For Mentally Challenged','Scrap Dealers','Screen Printers','Sea Cargo Agents','Seat Cover & Rexine Works','Security Guard Services','Security Services','Security Systems','Seeds','SelfDefence Training Services','Servers','Service Centres','Serviced Apartments','Seventh-Day Adventist Churches','Sewing Machine Dealers','Share Brokers','Shipping Companies','Shirts','Shoes','Shopping Malls','Shorts & Cargo','Sign Boards','Signage','Singing Classes','Skin Care Clinics','Snooker Parlours','Socks','Sofa Sets','Software & IT Services','Software Certifications','Software Dealers','Software Development','Software Training Institutes','Solar Products Manufacturers','Sound And Lighting On Hire','Sound Systems','Spa & Saloon','Spare Part Dealers','Spare Parts & Accessories','Speakers','Spiritual And Pooja Accessories','Spiritual Centres','Spoken English Institutes','Sports','Sports Academies','Sports Clubs','Sports Equipments','Sports Stores','Sports Wear','Sports, Entertainment & Hobbies','Stadiums','Stage Decorations','Stainless Steel Pipe Dealer','Stamp Papers','Standees & Demo Tents','State Board Schools','State Government Offices','Stationaries','Stationary Stores','Stations','Steel Wires & Ropes Manufacturers','Stem Cell Banking','Stock Brokers','Studios','Study Hall Centre','Sub-Registrar Offices','Suitings & Shirtings','Suits And Blazers','Sulphuric Acid Dealers','Sunglasses','Super Specialty Hospitals','Supermarkets','Surgical Instruments','Sweet Shops','Swimming Pools','Table Accessories','Tailoring Materials','Tailors','Tailors & Designers','Take Away Restaurants','Tattoo Makers','Telecommunications','Television Installation','Televisions','Temples','Tent Houses','Textiles','Theaters','Theme Parks','Thermocol Dealers','Ticketing','Tiles','Timber Depot','Tmt Iron & Steel Bars','Tours And Travels','Toy Shops','Trading Consultants','Training Institutes','Transportation','Travel Agencies','Travel Goods','Travel Services','Trophy & Momento Dealers','Trousers','T-Shirts','Tuitions','Tv Accessories','TV Studio','Two Wheelers Dealers','Two Wheelers Service Centres','Typing Institutes','Tyre Dealers','Unani Treatment','Underground Stations','Uniforms','Unitarian Universalist Churches','United Churches Of Christ','Unity Churches','Universities','UPS','UPSC & IAS Coaching Centres','Used Auto Dealers','Used Bike Dealers','Used Cars Dealers','Utensils','UV Water Purifier','Valve Dealer','Vegetables','Vehicle Glass Dealers','Vehicle On Hire','Vending Machine Manufacturer','Veterinary Hospitals','Veterinary Medicines','Video Editing Studios','Video Gaming Centres','Videographers','Vineyard Churches','Vinyl Flooring','Vocational Colleges','Wall Papers','Washing Machine Repair','Washing Machines','Water Cooler Suppliers','Water Parks','Water Purifier Dealers','Water Purifier Repairs','Water Softeners','Water Suppliers','Water Tank Suppliers','Waterproofing','Waterproofing Materials','Weather Stations','Web Designing Companies','Web Hosting Companies','Wedding & Events','Wedding Bands','Wedding Cards','Wedding Catering Services','Wedding Decorations','Wedding Planners','Weight Loss & Gain Centres','Welding Equipment','Welfare Offices','Wesleyan Churches','Wet Grinder Dealers','Wine Shops','Winter Wear','Wire Mesh Dealers','Womens Hostels','Wooden Flooring','Wrist Watch Repairs and Services','Wrist Watches','Xerox Shops','Yoga Centres','Zoo Parks','Zumba Fitness']

cities = ['Acton','Adelanto','Agoura Hills','Alameda','Alamo','Albany','Alhambra','Aliso Viejo','Almanor','Alondra Park','Alpaugh','Alpine','Alpine Village','Altadena','Alta Sierra','Alturas','Alum Rock','Amador City','American Canyon','Amesti','Anaheim','Anderson','Angels City','Angwin','Antioch','Apple Valley','Aptos','Aptos Hills-Larkin Valley','Arbuckle','Arcadia','Arcata','Arden-Arcade','Armona','Arnold','Aromas','Arroyo Grande','Artesia','Arvin','Ashland','Atascadero','Atherton','Atwater','Auberry','Auburn','August','Avalon','Avenal','Avery','Avocado Heights','Azusa','Bakersfield','Baldwin Park','Banning','Barstow','Bay Point','Bayview','Bayview-Montalvin','Baywood-Los Osos','Beale AFB','Bear Valley','Bear Valley Springs','Beaumont','Beckwourth','Belden','Bell','Bellflower','Bell Gardens','Belmont','Belvedere','Benicia','Ben Lomond','Berkeley','Bermuda Dunes','Bertsch-Oceanview','Bethel Island','Beverly Hills','Big Bear City','Big Bear Lake','Big Bend','Biggs','Big Pine','Big River','Biola','Bishop','Blackhawk-Camino Tassajara','Black Point-Green Point','Blairsden','Bloomington','Blue Lake','Bluewater','Blythe','Bodega Bay','Bodfish','Bolinas','Bombay Beach','Bonadelle Ranchos-Madera Ranchos','Bonita','Bonsall','Bootjack','Boron','Boronda','Borrego Springs','Bostonia','Boulder Creek','Bowles','Boyes Hot Springs','Bradbury','Bradley','Brawley','Brea','Brentwood','Bret Harte','Brisbane','Broadmoor','Bucks Lake','Buellton','Buena Park','Buena Vista','Burbank','Burbank','Burlingame','Burney','Buttonwillow','Byron','Bystrom','Cabazon','Calabasas','Calexico','California City','Calimesa','Calipatria','Calistoga','Calwa','Camarillo','Cambria','Cambrian Park','Cameron Park','Campbell','Camp Pendleton North','Camp Pendleton South','Cantua Creek','Canyondam','Canyon Lake','Capitola','Caribou','Carlsbad','Carmel-by-the-Sea','Carmel Valley Village','Carmichael','Carpinteria','Carrick','Carson','Cartago','Caruthers','Casa Conejo','Casa de Oro-Mount Helix','Castro Valley','Castroville','Cathedral City','Cayucos','Ceres','Cerritos','Challenge-Brownsville','Channel Islands Beach','Charter Oak','Cherryland','Cherry Valley','Chester','Chico','Chilcoot-Vinton','China Lake Acres','Chinese Camp','Chino','Chino Hills','Chowchilla','Chualar','Chula Vista','Citrus','Citrus Heights','Claremont','Clayton','Clearlake','Clearlake Oaks','Clio','Cloverdale','Clovis','Clyde','Coachella','Coalinga','Cobb','Colfax','Colma','Colton','Columbia','Colusa','Commerce','Compton','Concord','Concow','Copperopolis','Corcoran','Corning','Corona','Coronado','Corralitos','Corte Madera','Costa Mesa','Cotati','Coto de Caza','Cottonwood','Country Club','Covelo','Covina','Crescent City','Crescent City North','Crescent Mills','Crest','Crestline','C-Road','Crockett','Cromberg','Cudahy','Culver City','Cupertino','Cutler','Cutten','Cypress','Daly City','Dana Point','Danville','Darwin','Davis','Day Valley','Deer Park','Del Aire','Delano','Delhi','Delleker','Del Mar','Del Monte Forest','Del Rey','Del Rey Oaks','Del Rio','Denair','Derby Acres','Desert Hot Springs','Desert Shores','Desert View Highlands','Diablo','Diamond Bar','Diamond Springs','Dillon Beach','Dinuba','Discovery Bay','Dixon','Dixon Lane-Meadow Creek','Dollar Point','Dorrington','Dorris','Dos Palos','Downey','Duarte','Dublin','Ducor','Dunsmuir','Durham','Dustin Acres','Earlimart','East Blythe','East Compton','East Foothills','East Hemet','East La Mirada','East Los Angeles','East Oakdale','Easton','East Orosi','East Palo Alto','East Pasadena','East Porterville','East Quincy','East Richmond Heights','East San Gabriel','East Shore','East Sonora','Edgewood','Edwards AFB','El Cajon','El Centro','El Cerrito','El Cerrito','El Dorado Hills','Eldridge','El Granada','Elk Grove','Elkhorn','Elmira','El Monte','El Paso de Robles (Paso Robles)','El Rio','El Segundo','El Sobrante','El Verano','Emerald Lake Hills','Emeryville','Empire','Encinitas','Escalon','Escondido','Esparto','Etna','Eureka','Exeter','Fairbanks Ranch','Fairfax','Fairfield','Fair Oaks','Fairview','Fallbrook','Fall River Mills','Farmersville','Farmington','Fellows','Felton','Ferndale','Fetters Hot Springs-Agua Caliente','Fillmore','Firebaugh','Florence-Graham','Florin','Folsom','Fontana','Foothill Farms','Foothill Ranch','Ford City','Foresthill','Forest Meadows','Forestville','Fort Bragg','Fort Jones','Fortuna','Foster City','Fountain Valley','Fowler','Frazier Park','Freedom','Fremont','French Camp','French Gulch','Fresno','Friant','Fruitdale','Fullerton','Furnace Creek','Galt','Gardena','Garden Acres','Garden Grove','Gazelle','Georgetown','Gerber-Las Flores','Gilroy','Glen Avon','Glendale','Glendora','Glen Ellen','Golden Hills','Gold River','Goleta','Gonzales','Goshen','Graeagle','Grand Terrace','Granite Bay','Granite Hills','Grass Valley','Graton','Grayson','Greenfield','Greenhorn','Green Valley','Greenview','Greenville','Grenada','Gridley','Groveland-Big Oak Flat','Grover Beach','Guadalupe','Guerneville','Gustine','Hacienda Heights','Half Moon Bay','Hamilton Branch','Hamilton City','Hanford','Harbison Canyon','Hawaiian Gardens','Hawthorne','Hayfork','Hayward','Healdsburg','Heber','Hemet','Hercules','Hermosa Beach','Hesperia','Hickman','Hidden Hills','Hidden Meadows','Hidden Valley Lake','Highgrove','Highland','Highlands-Baywood Park','Hillsborough','Hilmar-Irwin','Hollister','Holtville','Home Garden','Home Gardens','Homeland','Homewood Canyon-Valley Wells','Hornbrook','Hughson','Humboldt Hill','Huntington Beach','Huntington Park','Huron','Hydesville','Idyllwild-Pine Cove','Imperial','Imperial Beach','Independence','Indian Falls','Indian Wells','Indio','Industry','Inglewood','Interlaken','Inverness','Inyokern','Ione','Iron Horse','Irvine','Irwindale','Isla Vista','Isleton','Ivanhoe','Jackson','Jamestown','Jamul','Johannesburg','Johnsville','Joshua Tree','Julian','Keddie','Keeler','Keene','Kelseyville','Kennedy','Kensington','Kentfield','Kerman','Kernville','Kettleman City','Keyes','King City','Kings Beach','Kingsburg','Kirkwood','Klamath','Knightsen','La Canada Flintridge','La Crescenta-Montrose','Ladera Heights','Lafayette','Laguna','Laguna Beach','Laguna Hills','Laguna Niguel','Laguna West-Lakeside','Laguna Woods','Lagunitas-Forest Knolls','La Habra','La Habra Heights','Lake Almanor Country Club','Lake Almanor Peninsula','Lake Almanor West','Lake Arrowhead','Lake Davis','Lake Elsinore','Lake Forest','Lakehead-Lakeshore','Lake Isabella','Lakeland Village','Lake Los Angeles','Lake Nacimiento','Lake of the Pines','Lake of the Woods','Lakeport','Lake San Marcos','Lakeside','Lakeview','Lake Wildwood','Lakewood','La Mesa','La Mirada','Lamont','Lanare','Lancaster','La Palma','La Porte','La Presa','La Puente','La Quinta','La Riviera','Larkfield-Wikiup','Larkspur','Las Flores','Las Lomas','Lathrop','Laton','La Verne','Lawndale','Laytonville','Lebec','Le Grand','Lemon Cove','Lemon Grove','Lemoore','Lemoore Station','Lennox','Lenwood','Lewiston','Lexington Hills','Lincoln','Lincoln Village','Linda','Linden','Lindsay','Little Grass Valley','Littlerock','Live Oak','Live Oak','Livermore','Livingston','Lockeford','Lodi','Loma Linda','Loma Rica','Lomita','Lompoc','London','Lone Pine','Long Beach','Loomis','Los Alamitos','Los Alamos','Los Altos','Los Altos Hills','Los Angeles','Los Banos','Los Gatos','Los Molinos','Lost Hills','Lower Lake','Loyalton','Loyola','Lucas Valley-Marinwood','Lucerne','Lynwood','McArthur','McCloud','Macdoel','McFarland','McKinleyville','McKittrick','Madera','Madera Acres','Magalia','Malibu','Mammoth Lakes','Manhattan Beach','Manteca','Manton','March AFB','Maricopa','Marina','Marina del Rey','Mariposa','Markleeville','Martinez','Marysville','Mayflower Village','Maywood','Meadow Valley','Meadow Vista','Mecca','Meiners Oaks','Mendocino','Mendota','Menlo Park','Mentone','Merced','Mesa','Mesa Vista','Mettler','Middletown','Millbrae','Mill Valley','Millville','Milpitas','Mineral','Mira Loma','Mira Monte','Mission Canyon','Mission Hills','Mission Viejo','Mi-Wuk Village','Modesto','Mohawk Vista','Mojave','Mokelumne Hill','Mono Vista','Monrovia','Montague','Montara','Montclair','Montebello','Montecito','Monterey','Monterey Park','Monte Rio','Monte Sereno','Montgomery Creek','Moorpark','Morada','Moraga','Moreno Valley','Morgan Hill','Morongo Valley','Morro Bay','Moss Beach','Moss Landing','Mountain Mesa','Mountain Ranch','Mountain View','Mountain View','Mountain View Acres','Mount Hebron','Mount Shasta','Muir Beach','Murphys','Murrieta','Murrieta Hot Springs','Muscoy','Myrtletown','Napa','National City','Nebo Center','Needles','Nevada City','Newark','Newman','Newport Beach','Newport Coast','Nice','Niland','Nipomo','Norco','North Auburn','North Edwards','North El Monte','North Fair Oaks','North Highlands','North Lakeport','North Woodbridge','Norwalk','Novato','Nuevo','Oakdale','Oakhurst','Oakland','Oakley','Oak Park','Oak View','Occidental','Oceano','Oceanside','Ocotillo','Oildale','Ojai','Olancha','Olivehurst','Ontario','Onyx','Opal Cliffs','Orange','Orange Cove','Orangevale','Orcutt','Orinda','Orland','Orosi','Oroville','Oroville East','Oxnard','Pacheco','Pacifica','Pacific Grove','Pajaro','Palermo','Palmdale','Palm Desert','Palm Springs','Palo Alto','Palo Cedro','Palos Verdes Estates','Palo Verde','Paradise','Paramount','Parksdale','Parkway-South Sacramento','Parkwood','Parlier','Pasadena','Patterson','Paxton','Pearsonville','Pedley','Penn Valley','Perris','Petaluma','Phoenix Lake-Cedar Ridge','Pico Rivera','Piedmont','Pine Hills','Pine Mountain Club','Pine Valley','Pinole','Piru','Pismo Beach','Pittsburg','Pixley','Placentia','Placerville','Planada','Pleasant Hill','Pleasanton','Plumas Eureka','Plymouth','Point Arena','Point Reyes Station','Pollock Pines','Pomona','Poplar-Cotton Center','Port Costa','Porterville','Port Hueneme','Portola','Portola Hills','Portola Valley','Poway','Prattville','Prunedale','Quail Valley','Quartz Hill','Quincy','Rail Road Flat','Rainbow','Raisin City','Ramona','Rancho Calaveras','Rancho Cordova','Rancho Cucamonga','Rancho Mirage','Rancho Murieta','Rancho Palos Verdes','Rancho San Diego','Rancho Santa Fe','Rancho Santa Margarita','Rancho Tehama Reserve','Randsburg','Red Bluff','Redding','Redlands','Redondo Beach','Redway','Redwood City','Reedley','Rialto','Richgrove','Richmond','Ridgecrest','Ridgemark','Rio Dell','Rio del Mar','Rio Linda','Rio Vista','Ripon','Riverbank','Riverdale','Riverdale Park','Riverside','Rocklin','Rodeo','Rohnert Park','Rolling Hills','Rolling Hills Estates','Rollingwood','Romoland','Rosamond','Rosedale','Roseland','Rosemead','Rosemont','Roseville','Ross','Rossmoor','Round Mountain','Round Valley','Rowland Heights','Rubidoux','Running Springs','Sacramento','St. Helena','Salida','Salinas','Salton City','Salton Sea Beach','San Andreas','San Anselmo','San Antonio Heights','San Ardo','San Bernardino','San Bruno','San Buenaventura','San Carlos','San Clemente','Sand City','San Diego','San Diego Country Estates','San Dimas','San Fernando','San Francisco','San Gabriel','Sanger','San Geronimo','San Jacinto','San Joaquin','San Joaquin Hills','San Jose','San Juan Bautista','San Juan Capistrano','San Leandro','San Lorenzo','San Lucas','San Luis Obispo','San Marcos','San Marino','San Martin','San Mateo','San Miguel','San Pablo','San Rafael','San Ramon','Santa Ana','Santa Barbara','Santa Clara','Santa Clarita','Santa Cruz','Santa Fe Springs','Santa Maria','Santa Monica','Santa Paula','Santa Rosa','Santa Venetia','Santa Ynez','Santee','Saratoga','Sausalito','Scotts Valley','Seal Beach','Searles Valley','Seaside','Sebastopol','Sedco Hills','Seeley','Selma','Seven Trees','Shackelford','Shafter','Shandon','Shasta Lake','Shaver Lake','Shingle Springs','Shingletown','Shoshone','Sierra Madre','Signal Hill','Simi Valley','Solana Beach','Soledad','Solvang','Sonoma','Sonora','Soquel','Soulsbyville','South Dos Palos','South El Monte','South Gate','South Lake Tahoe','South Oroville','South Pasadena','South San Francisco','South San Gabriel','South San Jose Hills','South Taft','South Whittier','South Woodbridge','South Yuba City','Spreckels','Spring Garden','Spring Valley','Springville','Squaw Valley','Squirrel Mountain Valley','Stallion Springs','Stanford','Stanton','Stinson Beach','Stockton','Storrie','Stratford','Strathmore','Strawberry','Suisun City','Summerland','Sun City','Sunnyside-Tahoe City','Sunnyslope','Sunnyvale','Sunol','Sunol-Midtown','Susanville','Sutter','Sutter Creek','Taft','Taft Heights','Taft Mosswood','Tahoe Vista','Talmage','Tamalpais-Homestead Valley','Tara Hills','Taylorsville','Tecopa','Tehachapi','Tehama','Temecula','Temelec','Temple City','Templeton','Tennant','Terra Bella','Thermalito','Thousand Oaks','Thousand Palms','Three Rivers','Tiburon','Tierra Buena','Tipton','Tobin','Tomales','Toro Canyon','Torrance','Tracy','Tranquillity','Traver','Trinidad','Truckee','Tulare','Tulelake','Tuolumne City','Tupman','Turlock','Tustin','Tustin Foothills','Twain','Twain Harte','Twentynine Palms','Twentynine Palms Base','Twin Lakes','Ukiah','Union City','Upland','Upper Lake','Vacaville','Valinda','Vallecito','Vallejo','Valle Vista','Valley Acres','Valley Center','Valley Ranch','Valley Springs','Val Verde','Vandenberg AFB','Vandenberg Village','Vernon','Victorville','View Park-Windsor Hills','Villa Park','Vincent','Vine Hill','Vineyard','Visalia','Vista','Waldon','Wallace','Walnut','Walnut Creek','Walnut Grove','Walnut Park','Wasco','Waterford','Watsonville','Weaverville','Weed','Weedpatch','Weldon','West Athens','West Bishop','West Carson','West Compton','West Covina','Westhaven-Moonstone','West Hollywood','Westlake Village','Westley','West Menlo Park','Westminster','West Modesto','Westmont','Westmorland','West Point','West Puente Valley','West Sacramento','West Whittier-Los Nietos','Westwood','Wheatland','Whitehawk','Whittier','Wildomar','Wilkerson','Williams','Willits','Willowbrook','Willow Creek','Willows','Wilton','Winchester','Windsor','Winter Gardens','Winterhaven','Winters','Winton','Wofford Heights','Woodacre','Woodcrest','Woodlake','Woodland','Woodside','Woodville','Wrightwood','Yorba Linda','Yosemite Lakes','Yosemite Valley','Yountville','Yreka','Yuba City','Yucaipa','Yucca Valley']

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

                                        'state': 'CA'


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
