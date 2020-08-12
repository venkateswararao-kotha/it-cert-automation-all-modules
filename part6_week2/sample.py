import json

with open('people.json', 'w') as people_json:
    json.dump(people, people_json, indent=2)

import yaml

with open('people.yaml', 'w') as people_yaml:
    yaml.safe_dump(people, people_yaml)

'''
The json library will help us turn Python objects into JSON, and turn JSON strings into Python objects! 
The dump() method serializes basic Python objects, writing them to a file. Like in this example:
'''

import json

people = [
  {
    "name": "Sabrina Green",
    "username": "sgreen",
    "phone": {
      "office": "802-867-5309",
      "cell": "802-867-5310"
    },
    "department": "IT Infrastructure",
    "role": "Systems Administrator"
  },
  {
    "name": "Eli Jones",
    "username": "ejones",
    "phone": {
      "office": "684-348-1127"
    },
    "department": "IT Infrastructure",
    "role": "IT Specialist"
  }
]

with open('people.json', 'w') as people_json:
    json.dump(people, people_json)

#That gives us a file with a single line that looks like this:
'''
[{"name": "Sabrina Green", "username": "sgreen", "phone": {"office": "802-867-5309", "cell": "802-867-5310"}, "department": "IT Infrastructure", "role": "Systems Administrator"}, {"name": "Eli Jones", "username": "ejones", "phone": {"office": "684-348-1127"}, "department": "IT Infrastructure", "role": "IT Specialist"}]

JSON doesn't need to contain multiple lines, but it sure can be hard to read the result 
if it's formatted this way! Let's use the indent parameter for json.dump() to make it a bit easier to read.

'''

with open('people.json', 'w') as people_json:
    json.dump(people, people_json, indent=2)


import requests

response = requests.get('https://www.google.com')
print(response.text[:300])
<!doctype html><html itemscope="" itemtype="http://schema.org/WebPage" lang="de"><head><meta content="text/html; charset=UTF-8" http-equiv="Content-Type"><meta content="/images/branding/googleg/1x/googleg_standard_color_128dp.png" itemprop="image"><title>Google</title><script nonce="dZfbIAn803LDGXS9


response = requests.get('https://www.google.com', stream=True)
>>> print(response.raw.read()[:100])

response.request.headers['Accept-Encoding']
'gzip, deflate'

response.headers['Content-Encoding']
'gzip'

response.ok
True

response.status_code
200

response = requests.get(url)
if not response.ok:
    raise Exception("GET failed with status code {}".format(response.status_code))

'''
But you don't really need to do that. Requests has us covered here, too! We can use the Response.raise_for_status() method, 
which will raise an HTTPError exception only if the response wasn’t successful.
'''

response = requests.get(url)
response.raise_for_status()

'''
The question mark separates the URL resource from the resource's parameters. 
These parameters are one or more key-value pairs, formatted as a query string.
 In the example above, the search parameter is set to "grey+kitten", and the 
 max_results parameter is set to 15.

But you don't have to write your own code to create an URL like that one. 
With requests.get(), you can provide a dictionary of parameters, and the 
Requests module will construct the correct URL for you!
'''

>>> p = {"search": "grey kitten",
...      "max_results": 15}
>>> response = requests.get("https://example.com/path/to/api", params=p)
>>> response.request.url
'https://example.com/path/to/api?search=grey+kitten&max_results=15'

'''
You might notice that using parameters in Requests is yet another form of data serialization. Query strings are handy when we want to send small bits of information, but as our data becomes more complex, it can get hard to represent it using query strings. 

An alternative in that case is using the HTTP POST method. This method sends, or posts, data to a web service. Whenever you fill a web form and press a button to submit, you're using the POST method to send that data back to the web server. This method tends to be used when there's a bunch of data to transmit.

In our scripts, a POST request looks very similar to a GET request. Instead of setting the params attribute, which gets turned into a query string and appended to the URL, we use the data attribute, which contains the data that will be sent as part of the POST request.
'''
p = {"description": "white kitten",
...      "name": "Snowball",
...      "age_months": 6}
>>> response = requests.post("https://example.com/path/to/api", data=p)

response.request.url
'https://example.com/path/to/api'

# See how much simpler the URL is on this POST now? Where did all of the parameters go? They’re part of the body of the HTTP message. We can see them by checking out the body attribute.

response.request.body
'description=white+kitten&name=Snowball&age_months=6'

'''
Today, it's super common to send and receive data specifically in JSON format, so the Requests 
module can do the conversion directly for us, using the json parameter.
'''
response = requests.post("https://example.com/path/to/api", json=p)
>>> response.request.url
'https://example.com/path/to/api'
>>> response.request.body
b'{"description": "white kitten", "name": "Snowball", "age_months": 6}'


