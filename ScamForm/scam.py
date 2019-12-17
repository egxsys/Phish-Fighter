import requests
import os
import random
import string
import json

random.seed = (os.urandom(1024))

url = "(insert url here - PHP)"

names = json.loads(open('names.json').read())

for name in names:
	name_extra = ''.join(random.choice(string.digits))
	name1 = (random.choice(names))
	name2 = (random.choice(names))
	d1 = (random.choice(names))
	d2 = (random.choice(names))
	d3 = (random.choice(names))
	a1 = (random.choice(names))
	a2 = (random.choice(names))
	town = (random.choice(names))
	postcode = (random.choice(names))
	phone = (random.choice(names))
	mom = (random.choice(names))
	#Passwords? = ''.join(random.choice(chars) for i in range (9))

requests.post(url, allow_redirects = False, data = {
	'name1': name1,
	'name2': name2,
	'd1': d1,
	'd2': d2,
	'd3': d3,
	'a1': a1,
	'a2': a2,
	'town': town,
	'postcode': postcode,
	'phone': phone,
	'mom': mom
})

print (name1, name2, d1, d2, d3, a1, a2, town, postcode, phone, mom )
