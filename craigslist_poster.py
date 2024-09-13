import pyautogui as pya
import time

# Global Data
item_conditions = [
	'new',
	'like new',
	'excellent',
	'good',
	'fair',
	'salvage'
]

# Table Specs (Import from Google Sheets)
table_make = 'Brunswick'
table_model = 'AE1235F'
table_length = '14\' x '
table_width = '4\' x '
table_height = '6\''
table_condition = item_conditions[0]

# Declare Data
form_entries = [
	{
		'title': 'posting',
		'content': 'Cool Pool Table for Sale',
		'last_field': False,
		'is_dropdown': False
	},
	{
		'title': 'price',
		'content': '$696',
		'last_field': False,
		'is_dropdown': False
	},
	{
		'title': 'city',
		'content': 'Winter Park',
		'last_field': False,
		'is_dropdown': False
	},
	{
		'title': 'zip',
		'content': '32792',
		'last_field': False,
		'is_dropdown': False
	},
	{
		'title': 'description',
		'content': 'This sleek, Oakwood table is sure to impress. Don\'t miss out on the chance to take home a professional quality table today.',
		'last_field': False,
		'is_dropdown': False
	},
	{
		'title': 'make',
		'content': table_make,
		'last_field': False,
		'is_dropdown': False
	},
	{
		'title': 'model',
		'content': table_model,
		'last_field': False,
		'is_dropdown': False
	},
	{
		'title': 'dimensions',
		'content': table_length + table_width + table_height,
		'last_field': False,
		'is_dropdown': False
	},
	{
		'title': 'condition',
		'content': table_condition,
		'last_field': False,
		'is_dropdown': True
	},
	{
		'title': 'language',
		'content': 'english',
		'last_field': False,
		'is_dropdown': True
	},
	{
		'title': 'email',
		'content': 'info@pooltablestore.com',
		'last_field': False,
		'is_dropdown': False
	}
]

# 5s Delay
time.sleep(3)

# Move mouse to sporting goods, click 
def move_and_click(x_val, y_val):
	pya.moveTo(x_val, y_val, duration=0.5)
	pya.click()

# Check if dropdown, write something, press tab
def write_and_tab(content, last_field, is_dropdown):
	if (is_dropdown):
		pya.typewrite(content[0])
	else:
		pya.typewrite(content)
	time.sleep(0.5)
	if(not last_field):
		pya.typewrite('\t')
	time.sleep(0.5)

# Call on By Owner, click continue?
move_and_click(607, 436)
move_and_click(554, 705)

time.sleep(0.75)

# Call on Sporting Goods
move_and_click(1236, 464)

time.sleep(0.75)

# Write in all the boxes
for item in form_entries:
	print(item['title'] + ' : ' + item['content'])
	write_and_tab(item['content'], item['last_field'], item['is_dropdown'])

# Table Spec Writing
# write_and_tab(table_make, False, False)
# write_and_tab(table_model, False, False)

# write_and_tab(table_length, True, False)
# write_and_tab(table_width, True, False)
# write_and_tab(table_height, True, False)
# write_and_tab()

# while True:
# 	print(pya.position())
#	pya.displayMousePosition()