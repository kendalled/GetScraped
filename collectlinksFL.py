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

state = 'FL'

categories = ['Abrasive Dealers','Abundant Life Churches','AC Repairs','Accommodation','Acupuncture','Adhesive','Adoption Centres','Adventure Clubs','Advertising','Advertising Agencies','Advocates','Aerobics','Aeronautical Engineering Colleges','Air And Train Ambulance Services','Air Cargo Agents','Air Conditioners','Air Coolers','Air Hostess Training Institutes','Air Pollution Control Equipment Dealers','Alliance Churches','Alloy, Iron & Steel Industries','Alternative Fuels Stations','Alternative Medicines','Aluminium Extrusion Industry','Ambulance Services','Ammonia Gas Dealers','Amusement Parks','Anglican Churches','Animation Training Institutes','Apostolic Churches','Apparels & Accessories','Apple Product Repair','Aquarium','Architects','Area Rugs & Mats','Armenian Churches','Arms & Ammunition Dealer','Arms And Ammunitions','Art Gallery','Art Paintings','Artificial Grass','Artificial Turf','Arts & Craft Classes','Astrologers','ATM Centres','Audio Video Systems','Auditoriums','Auto Dealers','Auto Service Centres','Automobile Engine Oil Dealers','Automobiles','Aviation Academies','Ayurvedic Food','Ayurvedic Medicines','Ayurvedic Treatment','B 2 B','B Pharmacy Colleges','B.Ed. Colleges','Baby Foods','Baby Store','Bakeries','Bakery Equipments','Balloon Decorations','Bamboo Flooring','Bangles','Banks','Banquet Halls','Baptist Churches','Bar Coding Machine Dealer','Bars','Bathroom Linen','Battery Dealers','BDS Colleges','Bean Bags','Beautician Training Institutes','Beauty & Wellness','Beauty And Cosmetic Products','Beauty Parlours','Bed Linen','Bed Room Furniture','Beef Shops','Belts & Wallets','Bicycle Stores','Bike Rentals','Billing Machine Dealers','Binding','Binoculars & Telescope','Birth Certificate Offices','Blocks Material','Blood Donation Centres','Blow Moulding Machine Dealer','Body Massage Parlours','Boilers','Book Publishers','Books Stores','Bore Well Drilling','Boutiques','Bowling','Brick Materials','Bridal Makeup','Budget Hotels','Building and Construction','Building Demolition','Building Materials','Bulk SMS Modems','Bulk Sms Services','Burqa Retailers','Business Cards','Business Consultants','Business Hotels','CA & ICWA Training Institutes','Cable Manufacturers','Cable Tv Operators','Cabs Services','Cafes','Cake Shops','Calvary Chapel Churches','Camera Accessories','Camera Lens','Cameras','Candles','Caps & Hats','Car Ac Repairs','Car Accessories','Car Dealers','Car Rentals','Car Repairs & Services','Carbon Dioxide Gas Dealers','Cargo & Logistics','Cargo Agents','Carpenters','Carpet & Rugs','Carpet And Carpet Tiles','Casual Dining','Catering Services','Catholic Churches','CBSC Schools','Cement Materials','Central Government Offices','Centreing Materials','Chairs','Chandeliers','Charitable Trusts','Chartered Accountants','Chartered Bus','Chat & Snacks','Chicken Shops','Children Wear','Childrens Hospitals','Chimneys','Snacks','Chit Funds','Chocolate Shops','Churches','Cinema Theaters','Citric Acid Dealers','City Clerk Offices','City Government Offices','Civil Contractors','Cleaning Tools & Accessories','Clinics','Clocks','Cloud Software','Clubs','CNG Pump Stations','Coarse Aggregates','Commercial Kitchen Equipment Dealers','Communication','Competitive Exams','Computer Accessories & Peripherals','Computers','Computers, Tablets & Mobiles','Conference Hall','Construction & Renovation','Construction Companies','Consultants','Contact Lenses','Content Writers','Contractors','Convention Centres','Cooking Classes','Cooks On Hire','Cooktops','Cookware','Corporate Catering Services','Corporate Gifts','Cosmetic Surgery','Couriers','Courts','CPAP & BIPAP Systems','Crackers','Crane Services','Cremation Grounds','Cremation Services','Curtain Accessories','Cushion & Cushion Covers','Cutlery','Dance Academies','Dead Body Freezer Box On Hire','Decor & Lightings','Decor & Show Pieces','Decoration Materials','Degree Colleges','Dental Clinics','Designing & Wood Carving','Detective Agencies','Dhaba','Diagnostic Centres','Diesel Gas Stations','Dietician','Digital Cameras','Digital Printers','Digital Weighing Scale Dealers','Dining','Dining Room Furniture','Dining Sets','Disc Jockey Training Institutes','Dishwasher','Diwan Sets','Doctors','Dog Training','Doors, Windows & Partitions','Drama Theaters','Dress Materials','Drilling Equipments','Driver Service Agents','Dry Fruits','Dry Ice Dealer','DSLR Cameras','DTP Services','Dvd & Vcd','Eastern Orthodox Churches','Education','Education Colleges','Education Consultants','Education Councils & Board Offices','Education Schools','Egg Shops','Electrical Contractors','Electrical Sub-Stations','Electrical Suppliers','Electricians','Electronic Accessories','Electronic Display Boards Manufacturer','Electronic Weighing Scale Dealers','Electronics','Elevators','Email Marketing','Embroidery Works','Emergency Services','Engineering Colleges','ENT Hospitals','Entrance Exams Coaching Centres','Establishments','Ethnic Wear','Evangelical Churches','Event Decorators','Event Management','Event Organizers','Event Venues','Events Catering Services','Excavation','Eye Hospitals','Eyeglasses','Fabrication & Welding Works','False Ceiling','Family Clubs','Fans','Farm Houses','Fashion Designers','Fashion Designing Training Institutes','Fast Food Centre','Fertility & Infertility Clinics','Fertilizer & Soil','Film And Television Institute Of India','Film Studios','Financial Planners','Financial Services','Fine Dining','Fire Alarms','Fire And Safety Course Training','Fire Extinguishers','Fire Protection Systems','Fire Safety Equipments','Fire Stations','Fish & Sea Food Shops','Fitness Centres','Flex Printing Services','Flooring','Flooring Installations','Flooring Tools & Materials','Florists','Flower Decorations','Food & Beverage Outlets','Food & Beverages','Food Courts','Food Machinery Manufacturer','Food Processing Equipment Manufacturer','Food Stores','Footwear','Foreign Exchange','Foursquare Churches','Frames','Fruit Juice Processing Machine Manufacture','Fruits','Full Gospel Churches','Function Halls','Funeral Band','Funeral Materials','Furnishings','Furniture','Furniture on Hire','Furniture Storage','Gaming Centres','Gardening Tools','Garments','Gas Dealers','Gas Stations','Gemological Institute Of India','General Hospitals','General order suppliers','General Pharmacies','GI Pipe Dealer','Gifts And Novelties','Glass Fitting Hardware','Glasswares','Go Karting','Goldsmiths','Gospel Churches','Government Hospitals','Government Offices','Graphic Designers','GRE & TOEFL Coaching Centres','Greek Orthodox Churches','Groceries','Groundwater Surveyors','Guest Houses','Gurudwaras','Water Heater Repair','Gymnasium','Gymnasium Equipments','Hair Fall Treatments','Hair Stylists','Hair Transplantation','Hair Treatments','Hall Decorations','Handicraft Items','Handlooms','Hardware And Network Training Institutes','Hardware And Networking','Hardware Stores','Hardware Tools','Hardwood Flooring','HD Cameras','Health','Health Clubs','Hearse Services','Heavy Vehicle Dealers','Helmet Dealers','Hispanic Churches','Home Appliances','Home Builders','Home Delivery Restaurants','Home Furniture','Home Needs','Home Theater Systems','Homeopathy Clinics','Homeopathy Medicines','Hosiery Store','Hospitals','Hotels','House Painters','Housekeeping Services','Hr Consultancies','Hydraulic & Pulley Equipment Dealers','Hydrochloric Acid Dealers','Hypermarkets','IB Schools','Ice Cream & Dessert Parlors','ICSE Schools','IGCSE Schools','Immigration Consultants','Income Tax Offices','Industrial Bearing Dealers','Industrial Belt Dealers','Industrial Burner Dealers','Industrial Chemical Dealers','Industrial Electronic Components Dealers','Industrial Equipments','Industrial Fan Dealers','Industrial Fire Extinguisher Dealers','industrial machine dealers','Industrial Safety Equipment Dealers','Industrial Spring Dealers','Industrial Trolleys Manufacturer','Innerwear And Loungewear','Institute Of Hotel Management','Insurance Agents','Interior Design Courses','Interior Designers','Internet Service Providers','Inverters','Investment Advisors','Irrigation Equipment Dealers','ITI Training','Jain Temples','Jeans','Jewellery','Jewellery Box Manufacturers','Journalism Training Institutes','Juice Centre','Junior Colleges','Kalyana Mandapam','Kennels','Kitchen & Dining','Kitchen Storage Containers','Lab Equipment And Chemical Suppliers','Labor Contractors','Laboratories','Ladies Bags & Purses','Ladies Dresses','Laminate Flooring','Language Training Institutes','Laptop Repair','Laptops','Lathe Machine Dealers','Laundry Services','Law Colleges','Lawn & Garden','Leather Goods Manufacturer','Legal & Financial Services','Legal Services','Libraries','Lifestyle Accessories','Lightings','Living Room Furniture','Loan Agencies','Loan Agents','Local Government Offices','Locks','Lodges','Logistic Companies','Logistics Services','Lounges','Luxury Hotels','Maggam Job Works','Makeup Artists','Manufacturer of Power Generators','Marriage Bureaus','Marriage Halls','Mass Communication & Journalism Colleges','Matching Centres','Maternity Hospitals','Mattresses','Meat & Poultry Shops','Media Advertising','Medical Coding Training Institutes','Medical Colleges','Medical Equipments','Medical Stockings','Meditation Centres','Mehandi Artists','Mennonite Churches','Mens Hostels','Mesh Dealers','Metal Industries','Methodist Churches','Metro Rail Stations','Microbreweries','Microwave Repairs','Military Recruiting Offices','Milk & Milk Products','Mineral Water Suppliers','Mobile Phones','Mobile Repairs','Mobile Repairs','Modular Furniture','Modular Kitchen Dealers','Money Transfer Agencies','Montessori Training Institutes','Moravian Churches','Morgues Services','Mormon Churches','Mosques','Motor Driving Schools','Mould Dies Manufacturer','Moving Media Ads','Mp3 Players','MS Pipe Dealer','Multispecialty Hospitals','Museums','Music Academies','Musical Instruments','Mutton Shops','Natural Flooring','Nature Cure Centers','Naturopathy','Network Securities','Networking Devices','New Age Churches','Newspaper Ads','NGO Clubs','NGOs & Social Service Organisations','Night Clubs','Night Life','Night Wears','Nitric Acid Dealers','Notary Services','Number Plate Manufacturers','Nursing Colleges','Nutritional Supplement Dealers','Office Furniture','Offices','Offset Printers','Old Age Homes','Old Cut Notes Exchange Services','Online Classes','Optics & Eyewear','Organ Donation Centres','Orphanages & Shelters','Orthodox Churches','Other Vehicles','Outdoor Advertising','Outdoor Catering Services','Outdoor Furniture','Overseas Education Consultants','Oxygen Concentrators','Oxygen Gas Dealers','P R P Hair Treatments','Packers And Movers','Packing Machine Manufacturers','Painters','Painting Suppliers','Pan Shops','Pants','Paper Rolls Manufacturers','Paper Stores','Parks','Part Time Jobs Consultancies','Party Halls','Passport Offices','Pawn Brokers','Pcs & Desktops','Pedicure & Manicure','Pen Stores','Pentecostal Churches','Perforated Sheet Manufacturers','Perfumes','Personal Fitness Trainers','Personality Development Training Institutes','Pest Control Services','Pet Shops','Pets','PG Colleges','Pharmaceutical Companies','Pharmaceutical Packaging Material Dealers','Pharmacies','Pharmacy Colleges','Photo Frames','Photo Studios','Photocopiers','Photographers','Photography Training Institutes','physiotherapist','Physiotherapy Clinics','Piercing','Pilot Training Institutes','Pipe Dealers','Pizza Restaurants','Placement Consultants','Plants','Plastic & Disposable Items','Plastic Injection Moulding Machine Dealer','Plastic Products Manufacturers','Play Schools','Play Stations','Playground Equipments','Playgrounds','Plumbers','Plumbing','Plywood & Laminates','Police Stations','Political Party Offices','Pollution Inspection Stations','Polymers & Asbestos Products Dealer','Polytechnic Colleges','Pork Shops','Post Offices','Power Generator Suppliers','Power Stations','Power Tools Dealers','Presbyterian Churches','Printed Circuit Board Dealers','Printers','Printing & Stationaries','Printing Machines','Printing Materials','Printing Press','Professional Services','Professionals','Project Management Training Institutes','Projectors','Promotional Products','Property Consultants','Property Dealers','Protestant Churches','Public Safety Offices','Pubs','Pumps & Controllers','Pundits','PVC Pipe Dealer','Quaker Churches','Quick Bites','Radio Jockey Training Institutes','Radio Stations','Radium Works','Railings','Railway Cargo Agents','Railway Stations','Ready Made Garments','Ready Mix Concrete','Real Estate','Real Estate Agents','Real Estate Developers','Real Estate Loans & Mortgages','Recording Studios','Reformed Churches','Refrigerator Repair','Refrigerators','Registry Offices','Rehabilitation Centres','Religion','Research Institutes','Residential Designers','Resins & Chemicals Manufacturer','Resorts','Restaurant Test','Restaurants','RO Water Purifier','Road Cargo Agents','Robotics Engineering','Robotics Training Institutes','Roofing Sheets','RTA Offices','Rubber Oil Seals Dealer','Rubber Product Dealer','Rubber Product Manufacturers','Rubber Stamps','Rudraksha','Russian Orthodox Churches','Sand Materials','Sandals & Floaters','Sanitaryware & Bathroom Accessories','Sarees & Blouses','Scalp Treatments','School District Offices','School For Mentally Challenged','Scrap Dealers','Screen Printers','Sea Cargo Agents','Seat Cover & Rexine Works','Security Guard Services','Security Services','Security Systems','Seeds','SelfDefence Training Services','Servers','Service Centres','Serviced Apartments','Seventh-Day Adventist Churches','Sewing Machine Dealers','Share Brokers','Shipping Companies','Shirts','Shoes','Shopping Malls','Shorts & Cargo','Sign Boards','Signage','Singing Classes','Skin Care Clinics','Snooker Parlours','Socks','Sofa Sets','Software & IT Services','Software Certifications','Software Dealers','Software Development','Software Training Institutes','Solar Products Manufacturers','Sound And Lighting On Hire','Sound Systems','Spa & Saloon','Spare Part Dealers','Spare Parts & Accessories','Speakers','Spiritual And Pooja Accessories','Spiritual Centres','Spoken English Institutes','Sports','Sports Academies','Sports Clubs','Sports Equipments','Sports Stores','Sports Wear','Sports, Entertainment & Hobbies','Stadiums','Stage Decorations','Stainless Steel Pipe Dealer','Stamp Papers','Standees & Demo Tents','State Board Schools','State Government Offices','Stationaries','Stationary Stores','Stations','Steel Wires & Ropes Manufacturers','Stem Cell Banking','Stock Brokers','Studios','Study Hall Centre','Sub-Registrar Offices','Suitings & Shirtings','Suits And Blazers','Sulphuric Acid Dealers','Sunglasses','Super Specialty Hospitals','Supermarkets','Surgical Instruments','Sweet Shops','Swimming Pools','Table Accessories','Tailoring Materials','Tailors','Tailors & Designers','Take Away Restaurants','Tattoo Makers','Telecommunications','Television Installation','Televisions','Temples','Tent Houses','Textiles','Theaters','Theme Parks','Thermocol Dealers','Ticketing','Tiles','Timber Depot','Tmt Iron & Steel Bars','Tours And Travels','Toy Shops','Trading Consultants','Training Institutes','Transportation','Travel Agencies','Travel Goods','Travel Services','Trophy & Momento Dealers','Trousers','T-Shirts','Tuitions','Tv Accessories','TV Studio','Two Wheelers Dealers','Two Wheelers Service Centres','Typing Institutes','Tyre Dealers','Unani Treatment','Underground Stations','Uniforms','Unitarian Universalist Churches','United Churches Of Christ','Unity Churches','Universities','UPS','UPSC & IAS Coaching Centres','Used Auto Dealers','Used Bike Dealers','Used Cars Dealers','Utensils','UV Water Purifier','Valve Dealer','Vegetables','Vehicle Glass Dealers','Vehicle On Hire','Vending Machine Manufacturer','Veterinary Hospitals','Veterinary Medicines','Video Editing Studios','Video Gaming Centres','Videographers','Vineyard Churches','Vinyl Flooring','Vocational Colleges','Wall Papers','Washing Machine Repair','Washing Machines','Water Cooler Suppliers','Water Parks','Water Purifier Dealers','Water Purifier Repairs','Water Softeners','Water Suppliers','Water Tank Suppliers','Waterproofing','Waterproofing Materials','Weather Stations','Web Designing Companies','Web Hosting Companies','Wedding & Events','Wedding Bands','Wedding Cards','Wedding Catering Services','Wedding Decorations','Wedding Planners','Weight Loss & Gain Centres','Welding Equipment','Welfare Offices','Wesleyan Churches','Wet Grinder Dealers','Wine Shops','Winter Wear','Wire Mesh Dealers','Womens Hostels','Wooden Flooring','Wrist Watch Repairs and Services','Wrist Watches','Xerox Shops','Yoga Centres','Zoo Parks','Zumba Fitness']

cities = ["Alachua","Alford","Altamonte Springs","Altha","Altoona","Alva","Andover","Andrews","Anna Maria","Apalachicola","Apollo Beach","Apopka","Arcadia","Archer","Asbury Lake","Astatula","Astor","Atlantic Beach","Atlantis","Auburndale","Aventura","Avon Park","Azalea Park","Babson Park","Bagdad","Baldwin","Bal Harbour village","Bartow","Bascom","Bay Harbor Islands","Bay Hill","Bay Lake","Bayonet Point","Bay Pines","Bayport","Bayshore Gardens","Beacon Square","Bee Ridge","Bell","Bellair-Meadowbrook Terrace","Belleair","Belleair Beach","Belleair Bluffs","Belleair Shore","Belle Glade","Belle Glade Camp","Belle Isle","Belleview","Bellview","Beverly Beach","Beverly Hills","Big Coppitt Key","Big Pine Key","Biscayne Park village","Bithlo","Black Diamond","Bloomingdale","Blountstown","Boca Del Mar","Boca Pointe","Boca Raton","Bokeelia","Bonifay","Bonita Springs","Bonnie Lock-Woodsetter North","Boulevard Gardens","Bowling Green","Boyette","Boynton Beach","Bradenton","Bradenton Beach","Brandon","Branford","Brent","Briny Breezes","Bristol","Broadview Park","Broadview-Pompano Park","Bronson","Brooker","Brookridge","Brooksville","Broward Estates","Brownsville","Buckhead Ridge","Buckingham","Bunche Park","Bunnell","Burnt Store Marina","Bushnell","Butler Beach","Callahan","Callaway","Campbell","Campbellton","Canal Point","Cape Canaveral","Cape Coral","Captiva","Carol City","Carrabelle","Carver Ranches","Caryville","Casselberry","Cedar Grove","Cedar Key","Celebration","Center Hill","Century","Century Village","Chambers Estates","Charleston Park","Charlotte Harbor","Charlotte Park","Chattahoochee","Cheval","Chiefland","Chipley","Chokoloskee","Christmas","Chula Vista","Chuluota","Cinco Bayou","Citrus Hills","Citrus Park","Citrus Ridge","Citrus Springs","Clearwater","Clermont","Cleveland","Clewiston","Cloud Lake","Cocoa","Cocoa Beach","Cocoa West","Coconut Creek","Coleman","Collier Manor-Cresthaven","Combee Settlement","Conway","Cooper City","Coral Gables","Coral Springs","Coral Terrace","Cortez","Cottondale","Country Club","Country Estates","Country Walk","Crescent Beach","Crescent City","Crestview","Crooked Lake Park","Cross City","Crystal Lake CDP (Broward County)","Crystal Lake CDP (Polk County)","Crystal River","Crystal Springs","Cudjoe Key","Cutler","Cutler Ridge","Cypress Gardens","Cypress Lake","Cypress Lakes","Cypress Quarters","Dade City","Dade City North","Dania Beach","Davenport","Davie","Daytona Beach","Daytona Beach Shores","De Bary","Deerfield Beach","De Funiak Springs","De Land","De Land Southwest","De Leon Springs","Delray Beach","Deltona","Desoto Lakes","Destin","Doctor Phillips","Doral","Dover","Duck Key","Dundee","Dunedin","Dunes Road","Dunnellon","Eagle Lake","East Bronson","East Dunbar","East Lake","East Lake-Orient Park","East Palatka","East Perrine","Eastpoint","East Williston","Eatonville","Ebro","Edgewater","Edgewater","Edgewood","Eglin AFB","Egypt Lake-Leto","Elfers","Ellenton","El Portal village","Englewood","Ensley","Estates of Fort Lauderdale","Estero","Esto","Eustis","Everglades","Fairview Shores","Fanning Springs","Feather Sound","Fellsmere","Fernandina Beach","Ferndale","Fern Park","Ferry Pass","Fisher Island","Fish Hawk","Five Points","Flagler Beach","Floral City","Florida City","Florida Ridge","Forest City","Fort Lauderdale","Fort Meade","Fort Myers","Fort Myers Beach","Fort Myers Shores","Fort Pierce","Fort Pierce North","Fort Pierce South","Fort Walton Beach","Fort White","Fountainbleau","Franklin Park","Freeport","Fremd Village-Padgett Island","Frostproof","Fruit Cove","Fruitland Park","Fruitville","Fussels Corner","Gainesville","Gandy","Gateway","Geneva","Gibsonia","Gibsonton","Gifford","Gladeview","Glencoe","Glen Ridge","Glen St. Mary","Glenvar Heights","Godfrey Road","Golden Beach","Golden Gate","Golden Glades","Golden Heights","Golden Lakes","Goldenrod","Golf village","Gonzalez","Goodland","Gotha","Goulding","Goulds","Graceville","Grand Ridge","Greater Carrollwood","Greater Northdale","Greater Sun Center","Greenacres","Green Cove Springs","Green Meadow","Greensboro","Greenville","Greenwood","Gretna","Grove City","Groveland","Gulf Breeze","Gulf Gate Estates","Gulfport","Gulf Stream","Gun Club Estates","Haines City","Hallandale","Hampton","Hamptons at Boca Raton","Harbor Bluffs","Harbour Heights","Harlem","Harlem Heights","Hastings","Havana","Haverhill","Hawthorne","Heathrow","Hernando","Hernando Beach","Hialeah","Hialeah Gardens","Highland Beach","Highland City","Highland Park village","High Point CDP (Hernando County)","High Point CDP (Palm Beach County)","High Springs","Hiland Park","Hillcrest Heights","Hilliard","Hill 'n Dale","Hillsboro Beach","Hillsboro Pines","Hillsboro Ranches","Hobe Sound","Holden Heights","Holiday","Holly Hill","Hollywood","Holmes Beach","Homestead","Homestead Base","Homosassa","Homosassa Springs","Horseshoe Beach","Howey-in-the-Hills","Hudson","Hunters Creek","Hutchinson Island South","Hypoluxo","Immokalee","Indialantic","Indian Creek village","Indian Harbour Beach","Indian River Estates","Indian River Shores","Indian Rocks Beach","Indian Shores","Indiantown","Inglis","Interlachen","Inverness","Inverness Highlands North","Inverness Highlands South","Inwood","Iona","Islamorada","Islandia","Istachatta","Ivanhoe Estates","Ives Estates","Jacksonville","Jacksonville Beach","Jacob City","Jan Phyl Village","Jasmine Estates","Jasper","Jay","Jennings","Jensen Beach","June Park","Juno Beach","Juno Ridge","Jupiter","Jupiter Inlet Colony","Jupiter Island","Kathleen","Kendale Lakes","Kendall","Kendall Green","Kendall West","Kenneth City","Kensington Park","Key Biscayne village","Key Colony Beach","Key Largo","Keystone","Keystone Heights","Key West","Kings Point","Kissimmee","Labelle","Lacoochee","La Crosse","Lady Lake","Laguna Beach","Lake Alfred","Lake Belvedere Estates","Lake Buena Vista","Lake Butler","Lake Butter","Lake City","Lake Clarke Shores","Lake Forest","Lake Hamilton","Lake Harbor","Lake Hart","Lake Helen","Lake Kathryn","Lakeland","Lakeland Highlands","Lake Lindsey","Lake Lorraine","Lake Lucerne","Lake Mack-Forest Hills","Lake Magdalene","Lake Mary","Lake Panasoffkee","Lake Park","Lake Placid","Lake Sarasota","Lakes by the Bay","Lakeside","Lakeside Green","Lake Wales","Lakewood Park","Lake Worth","Lake Worth Corridor","Land O' Lakes","Lantana","Largo","Lauderdale-by-the-Sea","Lauderdale Lakes","Lauderhill","Laurel","Laurel Hill","Lawtey","Layton","Lazy Lake village","Lecanto","Lee","Leesburg","Lehigh Acres","Leisure City","Leisureville","Lely","Lely Resort","Lighthouse Point","Limestone Creek","Lisbon","Live Oak","Loch Lomond","Lochmoor Waterway Estates","Lockhart","Longboat Key","Longwood","Loughman","Lower Grand Lagoon","Lutz","Lynn Haven","Macclenny","McGregor","McIntosh","Madeira Beach","Madison","Maitland","Malabar","Malone","Manalapan","Manasota Key","Manattee Road","Mango","Mangonia Park","Marathon","Marco Island","Margate","Marianna","Marineland","Mary Esther","Masaryktown","Mascotte","Matlacha","Matlacha Isles-Matlacha Shores","Mayo","Meadow Woods","Medley","Medulla","Melbourne","Melbourne Beach","Melbourne Village","Melrose Park","Memphis","Merritt Island","Mexico Beach","Miami","Miami Beach","Miami Gardens","Miami Lakes","Miami Shores village","Miami Springs","Micanopy","Micco","Middleburg","Midway","Midway","Milton","Mims","Minneola","Miramar","Miramar Beach","Mission Bay","Molino","Monticello","Montverde","Moore Haven","Mount Dora","Mount Plymouth","Mulberry","Myrtle Grove","Naples","Naples Manor","Naples Park","Naranja","Nassau Village-Ratliff","Neptune Beach","Newberry","New Port Richey","New Port Richey East","New Smyrna Beach","Niceville","Nobleton","Nokomis","Noma","Norland","North Andrews Gardens","North Bay Village","North Beach","North Brooksville","North De Land","North Fort Myers","North Key Largo","North Lauderdale","North Miami","North Miami Beach","North Palm Beach village","North Port","North Redington Beach","North River Shores","North Sarasota","North Weeki Wachee","Oak Hill","Oakland","Oakland Park","Oak Point","Oak Ridge","Ocala","Ocean Breeze Park","Ocean City","Ocean Ridge","Ocoee","Odessa","Ojus","Okahumpka","Okeechobee","Oldsmar","Olga","Olympia Heights","Opa-locka","Opa-locka North","Orange City","Orange Park","Orangetree","Orchid","Orlando","Orlovista","Ormond Beach","Ormond-By-The-Sea","Osprey","Otter Creek","Oviedo","Pace","Page Park","Pahokee","Paisley","Palatka","Palm Aire","Palm Bay","Palm Beach","Palm Beach Gardens","Palm Beach Shores","Palm City","Palm Coast","Palmetto","Palmetto Estates","Palm Harbor","Palmona Park","Palm River-Clair Mel","Palm Shores","Palm Springs village","Palm Springs North","Palm Valley","Panama City","Panama City Beach","Paradise Heights","Parker","Parkland","Paxton","Pebble Creek","Pelican Bay","Pembroke Park","Pembroke Pines","Penney Farms","Pensacola","Perry","Pierson","Pine Castle","Pinecrest village","Pine Hills","Pine Island","Pine Island Center","Pine Island Ridge","Pine Lakes","Pineland","Pinellas Park","Pine Manor","Pine Ridge CDP (Citrus County)","Pine Ridge CDP (Collier County)","Pinewood","Pittman","Placid Lakes","Plantation","Plantation","Plantation Island","Plantation Mobile Home Park","Plant City","Poinciana","Polk City","Pomona Park","Pompano Beach","Pompano Beach Highlands","Pompano Estates","Ponce de Leon","Ponce Inlet","Port Charlotte","Port La Belle","Port Orange","Port Richey","Port St. Joe","Port St. John","Port St. Lucie","Port St. Lucie-River Park","Port Salerno","Pretty Bayou","Princeton","Progress Village","Punta Gorda","Punta Rassa","Quincy","Raiford","Ramblewood East","Ravenswood Estates","Reddick","Redington Beach","Redington Shores","Richmond Heights","Richmond West","Ridgecrest","Ridge Manor","Ridge Wood Heights","Rio","Riverland Village","Riverview","Riviera Beach","Rock Island","Rockledge","Rolling Oaks","Roosevelt Gardens","Roseland","Rotonda","Royal Palm Beach village","Royal Palm Estates","Royal Palm Ranches","Ruskin","Safety Harbor","St. Augustine","St. Augustine Beach","St. Augustine Shores","St. Augustine South","St. Cloud","St. George","St. James City","St. Leo","St. Lucie village","St. Marks","St. Pete Beach","St. Petersburg","Samoset","Samsula-Spruce Creek","San Antonio","San Carlos Park","Sandalfoot Cove","Sanford","Sanibel","Sarasota","Sarasota Springs","Satellite Beach","Sawgrass","Schall Circle","Scott Lake","Sea Ranch Lakes village","Sebastian","Sebring","Seffner","Seminole","Seminole Manor","Sewall's Point","Shady Hills","Shalimar","Sharpes","Siesta Key","Silver Lake","Silver Springs Shores","Sky Lake","Sneads","Solana","Sopchoppy","Sorrento","South Apopka","South Bay","South Beach","South Bradenton","South Brooksville","Southchase","South Daytona","Southeast Arcadia","Southgate","South Gate Ridge","South Highpoint","South Miami","South Miami Heights","South Palm Beach","South Pasadena","South Patrick Shores","South Sarasota","South Venice","Springfield","Spring Hill","Spring Lake","Stacey Street","Starke","Stock Island","Stuart","Sugarmill Woods","Suncoast Estates","Sunny Isles Beach","Sunrise","Sunset","Sunshine Acres","Sunshine Ranches","Surfside","Sweetwater","Sylvan Shores","Taft","Tallahassee","Tamarac","Tamiami","Tampa","Tangelo Park","Tangerine","Tarpon Springs","Tavares","Tavernier","Taylor Creek","Tedder","Temple Terrace","Tequesta village","Terra Mar","The Crossings","The Hammocks","The Meadows","The Villages","Thonotosassa","Three Lakes","Three Oaks","Tice","Tierra Verde","Tildenville","Timber Pines","Titusville","Town 'n' Country","Treasure Island","Trenton","Trinity","Twin Lakes","Tyndall AFB","Umatilla","Union Park","University","University Park","Upper Grand Lagoon","Utopia","Valparaiso","Valrico","Vamo","Venice","Venice Gardens","Vernon","Vero Beach","Vero Beach South","Village Park","Villages of Oriole","Villano Beach","Villas","Vineyards","Virginia Gardens village","Wabasso","Wabasso Beach","Wahneta","Waldo","Warm Mineral Springs","Warrington","Washington Park","Watertown","Wauchula","Wausau","Waverly","Webster","Wedgefield","Weeki Wachee","Weeki Wachee Gardens","Wekiwa Springs","Welaka","Wellington village","Wesley Chapel","Wesley Chapel South","West and East Lealman","West Bradenton","Westchase","Westchester","West De Land","Westgate-Belvedere Homes","West Ken-Lark","West Little River","West Melbourne","West Miami","Weston","West Palm Beach","West Pensacola","West Perrine","West Samoset","West Vero Corridor","Westview","Westville","Westwood Lakes","Wewahitchka","Whiskey Creek","Whisper Walk","White City","White Springs","Whitfield","Wildwood","Williamsburg","Williston","Williston Highlands","Willow Oak","Wilton Manors","Wimauma","Windermere","Winston","Winter Beach","Winter Garden","Winter Haven","Winter Park","Winter Springs","Woodville","Worthington Springs","Wright","Yalaha","Yankeetown","Yeehaw Junction","Yulee","Zellwood","Zephyrhills","Zephyrhills North","Zephyrhills South","Zephyrhills West","Zolfo Springs"]

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

                                        'state': 'FL'


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
