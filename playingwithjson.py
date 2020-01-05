json_data = """{ "office": 
    {"medical": [
      { "room-number": 100,
        "use": "reception",
        "sq-ft": 50,
        "price": 75
      },
      { "room-number": 101,
        "use": "waiting",
        "sq-ft": 250,
        "price": 75
      },
      { "room-number": 102,
        "use": "examination",
        "sq-ft": 125,
        "price": 150
      },
      { "room-number": 103,
        "use": "examination",
        "sq-ft": 125,
        "price": 150
      },
      { "room-number": 104,
        "use": "office",
        "sq-ft": 150,
        "price": 100
      }
    ]},
    "parking": {
      "location": "premium",
      "style": "covered",
      "price": 750
    }
}"""

import json

# Not only can the json.dumps() function convert a Python datastructure to a JSON string,
# but it can also dump a JSON string directly into a file. Here is an example of writing
# a structure above to a JSON file:

# json_string = json.dumps(json_data)
datastore = json.loads(json_data)
print(datastore)
print(type(datastore))  # python store json data as a dictionary

# now you can access elements of json data using below for loop
for i in datastore['office']['medical']:
    print(i['room-number'])

# lets delete sq-ft from json and store new json in a variable

for i in datastore['office']['medical']:
    del i['sq-ft']

new_string = json.dumps(datastore, indent=2, sort_keys=True)  # put some indentation to look better and sort_keys for
# sorting it with key
print(new_string)

with open('example.json') as f:
    data = json.load(f)


for i in data['quiz']:
    print(i)


with open('storejson.json', 'w') as f:
    json.dump(data, f, indent=2)

################################################
import json
from urllib.request import urlopen

with urlopen("http://api.zippopotam.us/us/ma/belmont") as response:
    source = response.read()

data = json.loads(source)
print(data)

print(data['state'])
print(data['places'][1]['post code'])
print(len(data['places']))