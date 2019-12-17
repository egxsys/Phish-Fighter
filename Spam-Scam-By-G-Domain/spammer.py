import json
import requests
import os
import random
import string

chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))

# This is the URL we will be spamming
url = 'http://craigslist.pottsfam.com/index872dijasydu2iuad27aysdu2yytaus6d2ajsdhasdasd2.php'

names = json.loads(open('names.json').read())

for name in names:
    # Joins some random number to the names to throw them off
    name_addition = ''.join(random.choice(string.digits))

    # Defining username and passwords
    username = name.lower() + name_addition + '@gmail.com'
    password = ''.join(random.choice(chars) for i in range(10))

    # Handles sending the request to the webpage
    requests.post(url,allow_redirects=False, data= {
        'auid2yjauysd2uasdasdasd': username,
        'kjauysd6sAJSDhyui2yasd': password
    })

    # Prints out what it is sending
    print("sending " + str(username) + "and " + str(password))
