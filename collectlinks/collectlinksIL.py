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

state = 'IL'

categories = ['Abrasive Dealers','Abundant Life Churches','AC Repairs','Accommodation','Acupuncture','Adhesive','Adoption Centres','Adventure Clubs','Advertising','Advertising Agencies','Advocates','Aerobics','Aeronautical Engineering Colleges','Air And Train Ambulance Services','Air Cargo Agents','Air Conditioners','Air Coolers','Air Hostess Training Institutes','Air Pollution Control Equipment Dealers','Alliance Churches','Alloy, Iron & Steel Industries','Alternative Fuels Stations','Alternative Medicines','Aluminium Extrusion Industry','Ambulance Services','Ammonia Gas Dealers','Amusement Parks','Anglican Churches','Animation Training Institutes','Apostolic Churches','Apparels & Accessories','Apple Product Repair','Aquarium','Architects','Area Rugs & Mats','Armenian Churches','Arms & Ammunition Dealer','Arms And Ammunitions','Art Gallery','Art Paintings','Artificial Grass','Artificial Turf','Arts & Craft Classes','Astrologers','ATM Centres','Audio Video Systems','Auditoriums','Auto Dealers','Auto Service Centres','Automobile Engine Oil Dealers','Automobiles','Aviation Academies','Ayurvedic Food','Ayurvedic Medicines','Ayurvedic Treatment','B 2 B','B Pharmacy Colleges','B.Ed. Colleges','Baby Foods','Baby Store','Bakeries','Bakery Equipments','Balloon Decorations','Bamboo Flooring','Bangles','Banks','Banquet Halls','Baptist Churches','Bar Coding Machine Dealer','Bars','Bathroom Linen','Battery Dealers','BDS Colleges','Bean Bags','Beautician Training Institutes','Beauty & Wellness','Beauty And Cosmetic Products','Beauty Parlours','Bed Linen','Bed Room Furniture','Beef Shops','Belts & Wallets','Bicycle Stores','Bike Rentals','Billing Machine Dealers','Binding','Binoculars & Telescope','Birth Certificate Offices','Blocks Material','Blood Donation Centres','Blow Moulding Machine Dealer','Body Massage Parlours','Boilers','Book Publishers','Books Stores','Bore Well Drilling','Boutiques','Bowling','Brick Materials','Bridal Makeup','Budget Hotels','Building and Construction','Building Demolition','Building Materials','Bulk SMS Modems','Bulk Sms Services','Burqa Retailers','Business Cards','Business Consultants','Business Hotels','CA & ICWA Training Institutes','Cable Manufacturers','Cable Tv Operators','Cabs Services','Cafes','Cake Shops','Calvary Chapel Churches','Camera Accessories','Camera Lens','Cameras','Candles','Caps & Hats','Car Ac Repairs','Car Accessories','Car Dealers','Car Rentals','Car Repairs & Services','Carbon Dioxide Gas Dealers','Cargo & Logistics','Cargo Agents','Carpenters','Carpet & Rugs','Carpet And Carpet Tiles','Casual Dining','Catering Services','Catholic Churches','CBSC Schools','Cement Materials','Central Government Offices','Centreing Materials','Chairs','Chandeliers','Charitable Trusts','Chartered Accountants','Chartered Bus','Chat & Snacks','Chicken Shops','Children Wear','Childrens Hospitals','Chimneys','Snacks','Chit Funds','Chocolate Shops','Churches','Cinema Theaters','Citric Acid Dealers','City Clerk Offices','City Government Offices','Civil Contractors','Cleaning Tools & Accessories','Clinics','Clocks','Cloud Software','Clubs','CNG Pump Stations','Coarse Aggregates','Commercial Kitchen Equipment Dealers','Communication','Competitive Exams','Computer Accessories & Peripherals','Computers','Computers, Tablets & Mobiles','Conference Hall','Construction & Renovation','Construction Companies','Consultants','Contact Lenses','Content Writers','Contractors','Convention Centres','Cooking Classes','Cooks On Hire','Cooktops','Cookware','Corporate Catering Services','Corporate Gifts','Cosmetic Surgery','Couriers','Courts','CPAP & BIPAP Systems','Crackers','Crane Services','Cremation Grounds','Cremation Services','Curtain Accessories','Cushion & Cushion Covers','Cutlery','Dance Academies','Dead Body Freezer Box On Hire','Decor & Lightings','Decor & Show Pieces','Decoration Materials','Degree Colleges','Dental Clinics','Designing & Wood Carving','Detective Agencies','Dhaba','Diagnostic Centres','Diesel Gas Stations','Dietician','Digital Cameras','Digital Printers','Digital Weighing Scale Dealers','Dining','Dining Room Furniture','Dining Sets','Disc Jockey Training Institutes','Dishwasher','Diwan Sets','Doctors','Dog Training','Doors, Windows & Partitions','Drama Theaters','Dress Materials','Drilling Equipments','Driver Service Agents','Dry Fruits','Dry Ice Dealer','DSLR Cameras','DTP Services','Dvd & Vcd','Eastern Orthodox Churches','Education','Education Colleges','Education Consultants','Education Councils & Board Offices','Education Schools','Egg Shops','Electrical Contractors','Electrical Sub-Stations','Electrical Suppliers','Electricians','Electronic Accessories','Electronic Display Boards Manufacturer','Electronic Weighing Scale Dealers','Electronics','Elevators','Email Marketing','Embroidery Works','Emergency Services','Engineering Colleges','ENT Hospitals','Entrance Exams Coaching Centres','Establishments','Ethnic Wear','Evangelical Churches','Event Decorators','Event Management','Event Organizers','Event Venues','Events Catering Services','Excavation','Eye Hospitals','Eyeglasses','Fabrication & Welding Works','False Ceiling','Family Clubs','Fans','Farm Houses','Fashion Designers','Fashion Designing Training Institutes','Fast Food Centre','Fertility & Infertility Clinics','Fertilizer & Soil','Film And Television Institute Of India','Film Studios','Financial Planners','Financial Services','Fine Dining','Fire Alarms','Fire And Safety Course Training','Fire Extinguishers','Fire Protection Systems','Fire Safety Equipments','Fire Stations','Fish & Sea Food Shops','Fitness Centres','Flex Printing Services','Flooring','Flooring Installations','Flooring Tools & Materials','Florists','Flower Decorations','Food & Beverage Outlets','Food & Beverages','Food Courts','Food Machinery Manufacturer','Food Processing Equipment Manufacturer','Food Stores','Footwear','Foreign Exchange','Foursquare Churches','Frames','Fruit Juice Processing Machine Manufacture','Fruits','Full Gospel Churches','Function Halls','Funeral Band','Funeral Materials','Furnishings','Furniture','Furniture on Hire','Furniture Storage','Gaming Centres','Gardening Tools','Garments','Gas Dealers','Gas Stations','Gemological Institute Of India','General Hospitals','General order suppliers','General Pharmacies','GI Pipe Dealer','Gifts And Novelties','Glass Fitting Hardware','Glasswares','Go Karting','Goldsmiths','Gospel Churches','Government Hospitals','Government Offices','Graphic Designers','GRE & TOEFL Coaching Centres','Greek Orthodox Churches','Groceries','Groundwater Surveyors','Guest Houses','Gurudwaras','Water Heater Repair','Gymnasium','Gymnasium Equipments','Hair Fall Treatments','Hair Stylists','Hair Transplantation','Hair Treatments','Hall Decorations','Handicraft Items','Handlooms','Hardware And Network Training Institutes','Hardware And Networking','Hardware Stores','Hardware Tools','Hardwood Flooring','HD Cameras','Health','Health Clubs','Hearse Services','Heavy Vehicle Dealers','Helmet Dealers','Hispanic Churches','Home Appliances','Home Builders','Home Delivery Restaurants','Home Furniture','Home Needs','Home Theater Systems','Homeopathy Clinics','Homeopathy Medicines','Hosiery Store','Hospitals','Hotels','House Painters','Housekeeping Services','Hr Consultancies','Hydraulic & Pulley Equipment Dealers','Hydrochloric Acid Dealers','Hypermarkets','IB Schools','Ice Cream & Dessert Parlors','ICSE Schools','IGCSE Schools','Immigration Consultants','Income Tax Offices','Industrial Bearing Dealers','Industrial Belt Dealers','Industrial Burner Dealers','Industrial Chemical Dealers','Industrial Electronic Components Dealers','Industrial Equipments','Industrial Fan Dealers','Industrial Fire Extinguisher Dealers','industrial machine dealers','Industrial Safety Equipment Dealers','Industrial Spring Dealers','Industrial Trolleys Manufacturer','Innerwear And Loungewear','Institute Of Hotel Management','Insurance Agents','Interior Design Courses','Interior Designers','Internet Service Providers','Inverters','Investment Advisors','Irrigation Equipment Dealers','ITI Training','Jain Temples','Jeans','Jewellery','Jewellery Box Manufacturers','Journalism Training Institutes','Juice Centre','Junior Colleges','Kalyana Mandapam','Kennels','Kitchen & Dining','Kitchen Storage Containers','Lab Equipment And Chemical Suppliers','Labor Contractors','Laboratories','Ladies Bags & Purses','Ladies Dresses','Laminate Flooring','Language Training Institutes','Laptop Repair','Laptops','Lathe Machine Dealers','Laundry Services','Law Colleges','Lawn & Garden','Leather Goods Manufacturer','Legal & Financial Services','Legal Services','Libraries','Lifestyle Accessories','Lightings','Living Room Furniture','Loan Agencies','Loan Agents','Local Government Offices','Locks','Lodges','Logistic Companies','Logistics Services','Lounges','Luxury Hotels','Maggam Job Works','Makeup Artists','Manufacturer of Power Generators','Marriage Bureaus','Marriage Halls','Mass Communication & Journalism Colleges','Matching Centres','Maternity Hospitals','Mattresses','Meat & Poultry Shops','Media Advertising','Medical Coding Training Institutes','Medical Colleges','Medical Equipments','Medical Stockings','Meditation Centres','Mehandi Artists','Mennonite Churches','Mens Hostels','Mesh Dealers','Metal Industries','Methodist Churches','Metro Rail Stations','Microbreweries','Microwave Repairs','Military Recruiting Offices','Milk & Milk Products','Mineral Water Suppliers','Mobile Phones','Mobile Repairs','Mobile Repairs','Modular Furniture','Modular Kitchen Dealers','Money Transfer Agencies','Montessori Training Institutes','Moravian Churches','Morgues Services','Mormon Churches','Mosques','Motor Driving Schools','Mould Dies Manufacturer','Moving Media Ads','Mp3 Players','MS Pipe Dealer','Multispecialty Hospitals','Museums','Music Academies','Musical Instruments','Mutton Shops','Natural Flooring','Nature Cure Centers','Naturopathy','Network Securities','Networking Devices','New Age Churches','Newspaper Ads','NGO Clubs','NGOs & Social Service Organisations','Night Clubs','Night Life','Night Wears','Nitric Acid Dealers','Notary Services','Number Plate Manufacturers','Nursing Colleges','Nutritional Supplement Dealers','Office Furniture','Offices','Offset Printers','Old Age Homes','Old Cut Notes Exchange Services','Online Classes','Optics & Eyewear','Organ Donation Centres','Orphanages & Shelters','Orthodox Churches','Other Vehicles','Outdoor Advertising','Outdoor Catering Services','Outdoor Furniture','Overseas Education Consultants','Oxygen Concentrators','Oxygen Gas Dealers','P R P Hair Treatments','Packers And Movers','Packing Machine Manufacturers','Painters','Painting Suppliers','Pan Shops','Pants','Paper Rolls Manufacturers','Paper Stores','Parks','Part Time Jobs Consultancies','Party Halls','Passport Offices','Pawn Brokers','Pcs & Desktops','Pedicure & Manicure','Pen Stores','Pentecostal Churches','Perforated Sheet Manufacturers','Perfumes','Personal Fitness Trainers','Personality Development Training Institutes','Pest Control Services','Pet Shops','Pets','PG Colleges','Pharmaceutical Companies','Pharmaceutical Packaging Material Dealers','Pharmacies','Pharmacy Colleges','Photo Frames','Photo Studios','Photocopiers','Photographers','Photography Training Institutes','physiotherapist','Physiotherapy Clinics','Piercing','Pilot Training Institutes','Pipe Dealers','Pizza Restaurants','Placement Consultants','Plants','Plastic & Disposable Items','Plastic Injection Moulding Machine Dealer','Plastic Products Manufacturers','Play Schools','Play Stations','Playground Equipments','Playgrounds','Plumbers','Plumbing','Plywood & Laminates','Police Stations','Political Party Offices','Pollution Inspection Stations','Polymers & Asbestos Products Dealer','Polytechnic Colleges','Pork Shops','Post Offices','Power Generator Suppliers','Power Stations','Power Tools Dealers','Presbyterian Churches','Printed Circuit Board Dealers','Printers','Printing & Stationaries','Printing Machines','Printing Materials','Printing Press','Professional Services','Professionals','Project Management Training Institutes','Projectors','Promotional Products','Property Consultants','Property Dealers','Protestant Churches','Public Safety Offices','Pubs','Pumps & Controllers','Pundits','PVC Pipe Dealer','Quaker Churches','Quick Bites','Radio Jockey Training Institutes','Radio Stations','Radium Works','Railings','Railway Cargo Agents','Railway Stations','Ready Made Garments','Ready Mix Concrete','Real Estate','Real Estate Agents','Real Estate Developers','Real Estate Loans & Mortgages','Recording Studios','Reformed Churches','Refrigerator Repair','Refrigerators','Registry Offices','Rehabilitation Centres','Religion','Research Institutes','Residential Designers','Resins & Chemicals Manufacturer','Resorts','Restaurant Test','Restaurants','RO Water Purifier','Road Cargo Agents','Robotics Engineering','Robotics Training Institutes','Roofing Sheets','RTA Offices','Rubber Oil Seals Dealer','Rubber Product Dealer','Rubber Product Manufacturers','Rubber Stamps','Rudraksha','Russian Orthodox Churches','Sand Materials','Sandals & Floaters','Sanitaryware & Bathroom Accessories','Sarees & Blouses','Scalp Treatments','School District Offices','School For Mentally Challenged','Scrap Dealers','Screen Printers','Sea Cargo Agents','Seat Cover & Rexine Works','Security Guard Services','Security Services','Security Systems','Seeds','SelfDefence Training Services','Servers','Service Centres','Serviced Apartments','Seventh-Day Adventist Churches','Sewing Machine Dealers','Share Brokers','Shipping Companies','Shirts','Shoes','Shopping Malls','Shorts & Cargo','Sign Boards','Signage','Singing Classes','Skin Care Clinics','Snooker Parlours','Socks','Sofa Sets','Software & IT Services','Software Certifications','Software Dealers','Software Development','Software Training Institutes','Solar Products Manufacturers','Sound And Lighting On Hire','Sound Systems','Spa & Saloon','Spare Part Dealers','Spare Parts & Accessories','Speakers','Spiritual And Pooja Accessories','Spiritual Centres','Spoken English Institutes','Sports','Sports Academies','Sports Clubs','Sports Equipments','Sports Stores','Sports Wear','Sports, Entertainment & Hobbies','Stadiums','Stage Decorations','Stainless Steel Pipe Dealer','Stamp Papers','Standees & Demo Tents','State Board Schools','State Government Offices','Stationaries','Stationary Stores','Stations','Steel Wires & Ropes Manufacturers','Stem Cell Banking','Stock Brokers','Studios','Study Hall Centre','Sub-Registrar Offices','Suitings & Shirtings','Suits And Blazers','Sulphuric Acid Dealers','Sunglasses','Super Specialty Hospitals','Supermarkets','Surgical Instruments','Sweet Shops','Swimming Pools','Table Accessories','Tailoring Materials','Tailors','Tailors & Designers','Take Away Restaurants','Tattoo Makers','Telecommunications','Television Installation','Televisions','Temples','Tent Houses','Textiles','Theaters','Theme Parks','Thermocol Dealers','Ticketing','Tiles','Timber Depot','Tmt Iron & Steel Bars','Tours And Travels','Toy Shops','Trading Consultants','Training Institutes','Transportation','Travel Agencies','Travel Goods','Travel Services','Trophy & Momento Dealers','Trousers','T-Shirts','Tuitions','Tv Accessories','TV Studio','Two Wheelers Dealers','Two Wheelers Service Centres','Typing Institutes','Tyre Dealers','Unani Treatment','Underground Stations','Uniforms','Unitarian Universalist Churches','United Churches Of Christ','Unity Churches','Universities','UPS','UPSC & IAS Coaching Centres','Used Auto Dealers','Used Bike Dealers','Used Cars Dealers','Utensils','UV Water Purifier','Valve Dealer','Vegetables','Vehicle Glass Dealers','Vehicle On Hire','Vending Machine Manufacturer','Veterinary Hospitals','Veterinary Medicines','Video Editing Studios','Video Gaming Centres','Videographers','Vineyard Churches','Vinyl Flooring','Vocational Colleges','Wall Papers','Washing Machine Repair','Washing Machines','Water Cooler Suppliers','Water Parks','Water Purifier Dealers','Water Purifier Repairs','Water Softeners','Water Suppliers','Water Tank Suppliers','Waterproofing','Waterproofing Materials','Weather Stations','Web Designing Companies','Web Hosting Companies','Wedding & Events','Wedding Bands','Wedding Cards','Wedding Catering Services','Wedding Decorations','Wedding Planners','Weight Loss & Gain Centres','Welding Equipment','Welfare Offices','Wesleyan Churches','Wet Grinder Dealers','Wine Shops','Winter Wear','Wire Mesh Dealers','Womens Hostels','Wooden Flooring','Wrist Watch Repairs and Services','Wrist Watches','Xerox Shops','Yoga Centres','Zoo Parks','Zumba Fitness']

cities = ['Abingdon','Addieville village','Addison village','Adeline village','Albany village','Albers village','Albion','Aledo','Alexis village','Algonquin village','Alhambra village','Allendale village','Allenville village','Allerton village','Alma village','Alorton village','Alpha village','Alsey village','Alsip village','Altamont','Alton','Altona village','Alto Pass village','Alvin village','Amboy','Anchor village','Andalusia village','Andover village','Anna','Annawan','Antioch village','Apple River village','Arcola','Arenzville village','Argenta village','Arlington village','Arlington Heights village','Armington village','Aroma Park village','Arrowsmith village','Arthur village','Ashkum village','Ashland village','Ashley','Ashmore village','Ashton village','Assumption','Astoria village','Athens','Atkinson','Atlanta','Atwood village','Auburn','Augusta village','Aurora','Ava','Aviston village','Avon village','Baldwin village','Banner village','Bannockburn village','Bardolph village','Barrington village','Barrington Hills village','Barry','Bartelso village','Bartlett village','Bartonville village','Basco village','Batavia','Batchtown village','Bath village','Baylis village','Bay View Gardens village','Beach Park village','Beardstown','Beaverville village','Beckemeyer village','Bedford Park village','Beecher village','Beecher City village','Belgium village','Belknap village','Belle Prairie City','Belle Rive village','Belleville','Bellevue village','Bellflower village','Bellmont village','Bellwood village','Belvidere','Bement village','Benld','Bensenville village','Benson village','Bentley','Benton','Berkeley village','Berlin village','Berwyn','Bethalto village','Bethany village','Biggsville village','Bingham village','Birds village','Bishop Hill village','Bismarck village','Blandinsville village','Bloomingdale village','Bloomington','Blue Island','Blue Mound village','Bluffs village','Bluford village','Bolingbrook village','Bondville village','Bone Gap village','Bonfield village','Bonnie village','Boulder Hill','Bourbonnais village','Bowen village','Braceville village','Bradford village','Bradley village','Braidwood','Breese','Bridgeport','Bridgeview village','Brighton village','Brimfield village','Broadlands village','Broadview village','Broadwell village','Brocton village','Brookfield village','Brooklyn village','Brookport','Broughton village','Browning village','Browns village','Brownstown village','Brussels village','Bryant village','Buckingham village','Buckley village','Buckner village','Buda village','Buffalo village','Buffalo Grove village','Bull Valley village','Bulpitt village','Buncombe village','Bunker Hill','Burbank','Bureau Junction village','Burlington village','Burnham village','Burnt Prairie village','Burr Ridge village','Bush village','Bushnell','Butler village','Byron','Cabery village','Cahokia village','Cairo','Caledonia village','Calhoun village','Calumet City','Calumet Park village','Camargo village','Cambria village','Cambridge village','Camden village','Campbell Hill village','Camp Point village','Campus village','Canton','Cantrall village','Capron village','Carbon Cliff village','Carbondale','Carbon Hill village','Carlinville','Carlock village','Carlyle','Carmi','Carol Stream village','Carpentersville village','Carrier Mills village','Carrollton','Carterville','Carthage','Cary village','Casey','Caseyville village','Catlin village','Cave-In-Rock village','Cedar Point village','Cedarville village','Central City village','Centralia','Centreville','Cerro Gordo village','Chadwick village','Champaign','Chandlerville village','Channahon village','Channel Lake','Chapin village','Charleston','Chatham village','Chatsworth','Chebanse village','Chenoa','Cherry village','Cherry Valley village','Chester','Chesterfield village','Chicago','Chicago Heights','Chicago Ridge village','Chillicothe','Chrisman','Christopher','Cicero','Cisco village','Cisne village','Cissna Park village','Claremont village','Clarendon Hills village','Clay City village','Clayton village','Clear Lake village','Cleveland village','Clifton village','Clinton','Coal City village','Coalton village','Coal Valley village','Coatsburg village','Cobden village','Coffeen','Colchester','Coleta village','Colfax village','Collinsville','Colona','Colp village','Columbia','Columbus village','Compton village','Concord village','Congerville village','Cooksville village','Cordova village','Cornell village','Cortland','Coulterville village','Country Club Hills','Countryside','Cowden village','Coyne Center','Crainville village','Creal Springs','Crescent City village','Crest Hill','Creston village','Crestwood village','Crete village','Creve Coeur village','Crossville village','Crystal Lake','Crystal Lawns','Cuba','Cullom village','Cutler village','Cypress village','Dahlgren village','Dakota village','Dallas City','Dalton City village','Dalzell village','Damiansville village','Dana village','Danforth village','Danvers village','Danville','Darien','Davis village','Davis Junction village','Dawson village','Decatur','Deer Creek village','Deerfield village','Deer Grove village','Deer Park village','DeKalb','De Land village','Delavan','De Pue village','De Soto village','Des Plaines','Detroit village','De Witt village','Diamond village','Dieterich village','Divernon village','Dix village','Dixmoor village','Dixon','Dolton village','Dongola village','Donnellson village','Donovan village','Dorchester village','Dover village','Dowell village','Downers Grove village','Downs village','Du Bois village','Dunfermline village','Dunlap village','Dupo village','Du Quoin','Durand village','Dwight village','Eagarville village','Earlville','East Alton village','East Brooklyn village','East Cape Girardeau village','East Carondelet village','East Dubuque','East Dundee village','East Galesburg village','East Gillespie village','East Hazel Crest village','East Moline','Easton village','East Peoria','East St. Louis','Eddyville village','Edgewood village','Edinburg village','Edwardsville','Effingham','Elburn village','El Dara village','Eldorado','Eldred village','Elgin','Elizabeth village','Elizabethtown village','Elk Grove Village village','Elkhart village','Elkville village','Elliott village','Ellis Grove village','Ellisville village','Ellsworth village','Elmhurst','Elmwood','Elmwood Park village','El Paso','Elsah village','Elvaston village','Elwood village','Emden village','Emington village','Energy village','Enfield village','Equality village','Erie village','Essex village','Eureka','Evanston','Evansville village','Evergreen Park village','Ewing village','Exeter village','Fairbury','Fairfield','Fairmont','Fairmont City village','Fairmount village','Fairview village','Fairview Heights','Farina village','Farmer City','Farmersville village','Farmington','Fayetteville village','Ferris village','Fidelity village','Fieldon village','Fillmore village','Findlay village','Fisher village','Fithian village','Flanagan village','Flat Rock village','Flora','Florence village','Flossmoor village','Foosland village','Ford Heights village','Forest City village','Forest Lake','Forest Park village','Forest View village','Forrest village','Forreston village','Forsyth village','Fox Lake village','Fox Lake Hills','Fox River Grove village','Fox River Valley Gardens village','Frankfort village','Frankfort Square','Franklin village','Franklin Grove village','Franklin Park village','Freeburg village','Freeman Spur village','Freeport','Fulton','Fults village','Gages Lake','Galatia village','Galena','Galesburg','Galva','Gardner village','Garrett village','Gays village','Geneseo','Geneva','Genoa','Georgetown','Germantown village','Germantown Hills village','German Valley village','Gibson','Gifford village','Gilberts village','Gillespie','Gilman','Girard','Gladstone village','Glasford village','Glasgow village','Glen Carbon village','Glencoe village','Glendale Heights village','Glen Ellyn village','Glenview village','Glenwood village','Godfrey village','Godley village','Golconda','Golden village','Golden Gate village','Golf village','Goodfield village','Good Hope village','Goodings Grove','Goreville village','Gorham village','Grafton','Grand Ridge village','Grand Tower','Grandview village','Grandwood Park','Granite City','Grantfork village','Grant Park village','Granville village','Grayslake village','Grayville','Greenfield','Green Oaks village','Greenup village','Green Valley village','Greenview village','Greenville','Greenwood village','Gridley village','Griggsville','Gulf Port village','Gurnee village','Hainesville village','Hamburg village','Hamel village','Hamilton','Hammond village','Hampshire village','Hampton village','Hanaford village','Hanna City village','Hanover village','Hanover Park village','Hardin village','Harmon village','Harrisburg','Harristown village','Hartford village','Hartsburg village','Harvard','Harvel village','Harvey','Harwood Heights village','Havana','Hawthorn Woods village','Hazel Crest village','Hebron village','Hecker village','Henderson village','Hennepin village','Henning village','Henry','Herrick village','Herrin','Herscher village','Hettick village','Heyworth village','Hickory Hills','Hidalgo village','Highland','Highland Park','Highwood','Hillcrest village','Hillsboro','Hillsdale village','Hillside village','Hillview village','Hinckley village','Hindsboro village','Hinsdale village','Hodgkins village','Hoffman village','Hoffman Estates village','Holiday Hills village','Hollowayville village','Homer village','Hometown','Homewood village','Hoopeston','Hooppole village','Hopedale village','Hopewell village','Hopkins Park village','Hoyleton village','Hudson village','Huey village','Hull village','Humboldt village','Hume village','Huntley village','Hurst','Hutsonville village','Illiopolis village','Ina village','Indian Creek village','Indian Head Park village','Indianola village','Industry village','Ingalls Park','Inverness village','Iola village','Ipava village','Iroquois village','Irving village','Irvington village','Irwin village','Island Lake village','Itasca village','Iuka village','Ivesdale village','Jacksonville','Jeffersonville village','Jeisyville village','Jerome village','Jerseyville','Jewett village','Johnsburg village','Johnsonville village','Johnston City','Joliet','Jonesboro','Joppa village','Joy village','Junction village','Junction City village','Justice village','Kampsville village','Kane village','Kangley village','Kankakee','Kansas village','Kappa village','Karnak village','Kaskaskia village','Keenes village','Keensburg village','Keithsburg','Kell village','Kempton village','Kenilworth village','Kenney village','Kewanee','Keyesport village','Kilbourne village','Kildeer village','Kincaid village','Kinderhook village','Kingston village','Kingston Mines village','Kinmundy','Kinsman village','Kirkland village','Kirkwood village','Knoxville','Lacon','Ladd village','La Fayette village','La Grange village','La Grange Park village','La Harpe','Lake Barrington village','Lake Bluff village','Lake Catherine','Lake Forest','Lake in the Hills village','Lakemoor village','Lake of the Woods','Lake Summerset','Lake Villa village','Lakewood village','Lakewood Shores','Lake Zurich village','La Moille village','Lanark','Lansing village','La Prairie village','La Rose village','La Salle','Latham village','Lawrenceville','Leaf River village','Lebanon','Lee village','Leland village','Leland Grove','Lemont village','Lena village','Lenzburg village','Leonore village','Lerna village','Le Roy','Lewistown','Lexington','Liberty village','Libertyville village','Lily Lake village','Lima village','Lincoln','Lincolnshire village','Lincolnwood village','Lindenhurst village','Lisbon village','Lisle village','Litchfield','Littleton village','Little York village','Liverpool village','Livingston village','Loami village','Lockport','Loda village','Lomax village','Lombard village','London Mills village','Long Creek village','Long Grove village','Long Lake','Long Point village','Longview village','Loraine village','Lostant village','Louisville village','Loves Park','Lovington village','Ludlow village','Lyndon village','Lynnville village','Lynwood village','Lyons village','McCook village','McCullom Lake village','Macedonia village','McHenry','Machesney Park village','Mackinaw village','McLean village','McLeansboro','McNabb village','Macomb','Macon','Madison','Maeystown village','Magnolia village','Mahomet village','Makanda village','Malden village','Malta village','Manchester village','Manhattan village','Manito village','Manlius village','Mansfield village','Manteno village','Maple Park village','Mapleton village','Maquon village','Marengo','Marietta village','Marine village','Marion','Marissa village','Mark village','Markham','Maroa','Marquette Heights','Marseilles','Marshall','Martinsville','Martinton village','Maryville village','Mascoutah','Mason','Mason City','Matherville village','Matteson village','Mattoon','Maunie village','Maywood village','Mazon village','Mechanicsburg village','Media village','Medora village','Melrose Park village','Melvin village','Mendon village','Mendota','Menominee village','Meredosia village','Merrionette Park village','Metamora village','Metcalf village','Metropolis','Mettawa village','Middletown village','Midlothian village','Milan village','Milford village','Mill Creek village','Milledgeville village','Millington village','Mill Shoals village','Millstadt village','Milton village','Mineral village','Minier village','Minonk','Minooka village','Modesto village','Mokena village','Moline','Momence','Monee village','Monmouth','Montgomery village','Monticello','Montrose village','Morris','Morrison','Morrisonville village','Morton village','Morton Grove village','Mound City','Mounds','Mound Station village','Mount Auburn village','Mount Carmel','Mount Carroll','Mount Clare village','Mount Erie village','Mount Morris village','Mount Olive','Mount Prospect village','Mount Pulaski','Mount Sterling','Mount Vernon','Mount Zion village','Moweaqua village','Muddy village','Mulberry Grove village','Muncie village','Mundelein village','Murphysboro','Murrayville village','Naperville','Naplate village','Naples','Nashville','Nason','Nauvoo','Nebo village','Nelson village','Neoga','Neponset village','Newark village','New Athens village','New Baden village','New Bedford village','New Berlin village','New Boston','New Burnside village','New Canton','New Douglas village','New Grand Chain village','New Haven village','New Holland village','New Lenox village','Newman','New Millford village','New Minden village','New Salem village','Newton','Niantic village','Niles village','Nilwood','Noble village','Nokomis','Nora village','Normal','Norridge village','Norris village','Norris City village','North Aurora village','North Barrington village','Northbrook village','North Chicago','North City village','Northfield village','North Henderson village','Northlake','North Pekin village','North Riverside village','North Utica village','Norwood village','Oak Brook village','Oakbrook Terrace','Oakdale village','Oakford village','Oak Forest','Oak Grove village','Oakland','Oak Lawn village','Oak Park village','Oakwood village','Oakwood Hills village','Oblong village','Oconee village','Odell village','Odin village','OFallon','Ogden village','Oglesby','Ohio village','Ohlman village','Okawville village','Old Mill Creek village','Old Ripley village','Old Shawneetown village','Olmsted village','Olney','Olympia Fields village','Omaha village','Onarga village','Oneida','Oquawka village','Orangeville village','Oreana village','Oregon','Orient','Orion village','Orland Hills village','Orland Park village','Oswego village','Ottawa','Otterville','Owaneco village','Palatine village','Palestine village','Palmer village','Palmyra village','Palos Heights','Palos Hills','Palos Park village','Pana','Panama village','Panola village','Papineau village','Paris','Park City','Parkersburg village','Park Forest village','Park Ridge','Patoka village','Pawnee village','Paw Paw village','Paxton','Payson village','Pearl village','Pearl City village','Pecatonica village','Pekin','Peoria','Peoria Heights village','Peotone village','Percy village','Perry village','Peru','Pesotum village','Petersburg','Phillipstown village','Philo village','Phoenix village','Pierron village','Pinckneyville','Pingree Grove village','Piper City village','Pistakee Highlands','Pittsburg village','Pittsfield','Plainfield village','Plainville village','Plano','Pleasant Hill village','Pleasant Plains village','Plymouth village','Pocahontas village','Polo','Pontiac','Pontoon Beach village','Pontoosuc village','Poplar Grove village','Port Byron village','Posen village','Potomac village','Prairie City village','Prairie du Rocher village','Prairie Grove village','Preston Heights','Princeton','Princeville village','Prophetstown','Prospect Heights','Pulaski village','Quincy','Radom village','Raleigh village','Ramsey village','Rankin village','Ransom village','Rantoul village','Rapids City village','Raritan village','Raymond village','Red Bud','Reddick village','Redmon village','Reynolds village','Richmond village','Richton Park village','Richview village','Ridge Farm village','Ridgway village','Ridott village','Ringwood village','Rio village','Ripley village','Riverdale village','River Forest village','River Grove village','Riverside village','Riverton village','Riverwoods village','Roanoke village','Robbins village','Roberts village','Robinson','Rochelle','Rochester village','Rockbridge village','Rock City village','Rockdale village','Rock Falls','Rockford','Rock Island','Rock Island Arsenal','Rockton village','Rockwood village','Rolling Meadows','Rome','Romeoville village','Roodhouse','Roscoe village','Rose Hill village','Roselle village','Rosemont village','Roseville village','Rosewood Heights','Rosiclare','Rossville village','Round Lake village','Round Lake Beach village','Round Lake Heights village','Round Lake Park village','Roxana village','Royal village','Royal Lakes village','Royalton village','Ruma village','Rushville','Russellville village','Rutland village','Sadorus village','Sailor Springs village','St. Anne village','St. Augustine village','St. Charles','St. David village','St. Elmo','Ste. Marie village','St. Francisville','St. Jacob village','St. Johns village','St. Joseph village','St. Libory village','St. Peter village','Salem','Sandoval village','Sandwich','San Jose village','Sauget village','Sauk Village village','Saunemin village','Savanna','Savoy village','Sawyerville village','Saybrook village','Scales Mound village','Schaumburg village','Schiller Park village','Schram City village','Sciota village','Scott AFB','Scottville village','Seaton village','Seatonville village','Secor village','Seneca village','Sesser','Shabbona village','Shannon village','Shawneetown','Sheffield village','Shelbyville','Sheldon village','Sheridan village','Sherman village','Sherrard village','Shiloh village','Shipman','Shorewood village','Shumway village','Sibley village','Sidell village','Sidney village','Sigel','Silvis','Simpson village','Sims village','Skokie village','Sleepy Hollow village','Smithboro village','Smithfield village','Smithton village','Somonauk village','Sorento village','South Barrington village','South Beloit','South Chicago Heights village','South Elgin village','Southern View village','South Holland village','South Jacksonville village','South Pekin village','South Roxana village','South Wilmington village','Sparland village','Sparta','Spaulding village','Spillertown village','Spring Bay village','Springerton village','Springfield','Spring Grove village','Spring Valley','Standard village','Standard City village','Stanford village','Staunton','Steeleville village','Steger village','Sterling','Steward village','Stewardson village','Stickney village','Stillman Valley village','Stockton village','Stonefort village','Stone Park village','Stonington village','Stoy village','Strasburg village','Strawn village','Streamwood village','Streator','Stronghurst village','Sublette village','Sugar Grove village','Sullivan','Summerfield village','Summit village','Sumner','Sun River Terrace village','Swansea village','Sycamore','Symerton village','Table Grove village','Tallula village','Tamaroa village','Tamms village','Tampico village','Taylor Springs village','Taylorville','Tennessee village','Teutopolis village','Thawville village','Thayer village','Thebes village','Third Lake village','Thomasboro village','Thompsonville village','Thomson village','Thornton village','Tilden village','Tilton village','Timberlane village','Time village','Tinley Park village','Tiskilwa village','Toledo village','Tolono village','Toluca','Tonica village','Topeka village','Toulon','Tovey village','Towanda village','Tower Hill village','Tower Lakes village','Tremont village','Trenton','Trout Valley village','Troy','Troy Grove village','Tuscola','Ullin village','Union village','Union Hill village','University Park village','Urbana','Ursa village','Valier village','Valley City village','Valmeyer village','Vandalia','Varna village','Venedy village','Venetian Village','Venice','Vergennes village','Vermilion village','Vermont village','Vernon village','Vernon Hills village','Verona village','Versailles village','Victoria village','Vienna','Villa Grove','Villa Park village','Viola village','Virden','Virgil village','Virginia','Volo village','Wadsworth village','Waggoner village','Walnut village','Walnut Hill village','Walshville village','Waltonville village','Wamac','Wapella village','Warren village','Warrensburg village','Warrenville','Warsaw','Washburn village','Washington','Washington Park village','Wataga village','Waterloo','Waterman village','Watseka','Watson village','Wauconda village','Waukegan','Waverly','Wayne village','Wayne City village','Waynesville village','Weldon village','Wellington village','Wenona','Wenonah village','West Brooklyn village','Westchester village','West Chicago','West City village','West Dundee village','Western Springs village','Westfield village','West Frankfort','Westmont village','West Peoria','West Point village','West Salem village','Westville village','Wheaton','Wheeler village','Wheeling village','Whiteash village','White City village','White Hall','Williamsfield village','Williamson village','Williamsville village','Willisville village','Willowbrook village','Willowbrook','Willow Hill village','Willow Springs village','Wilmette village','Wilmington village','Wilmington','Wilsonville village','Winchester','Windsor village','Windsor','Winfield village','Winnebago village','Winnetka village','Winslow village','Winthrop Harbor village','Witt','Wonder Lake','Wonder Lake village','Wood Dale','Woodhull village','Woodland village','Woodlawn village','Woodridge village','Wood River','Woodson village','Woodstock','Worden village','Worth village','Wyanet village','Wyoming','Xenia village','Yale village','Yates City village','Yorkville','Zeigler','Zion']

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

                                        'state': 'Illinois'


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
