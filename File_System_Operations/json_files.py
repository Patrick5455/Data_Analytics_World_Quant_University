# json stands for Javascript Object Notation and it is a very common format for data shared on the web json tends to
# be very portable between different webApps and relatively light weight and can be easily sent over the interent.
# When we talk about interacting with APIs such as google maps or twitter APIs, we often recieve those data frome
# those APIs in fomr of JSON. Just like CSV, json files are text but STRUCTURED AS A SET OF NESTED DICTIONARIES AND
# LISTS. One advantage of JSON is that it does not have to conform to a tabular data. Hence we do not need to worry
# about the data having a repetitive strucutre or well structured.

# The format of JSON files - nested dioctionaries and lists allows for efficiency by reducing the amount of duplicated data.

import pandas as pd
import json
import numpy as np

book1 = {'title': 'The Prophet',
         'author': 'Khalil Gibran',
         'genre': 'poetry',
         'tags': ['religion', 'spirituality', 'philosophy', 'Lebanon', 'Arabic', 'Middle East'],
         'book_id': '811.19',
         'copies': [{'edition_year': 1996,
                     'checkouts': 486,
                     'borrowed': False},
                    {'edition_year': 1996,
                     'checkouts': 443,
                     'borrowed': False}]
         }

book2 = {'title': 'The Little Prince',
         'author': 'Antoine de Saint-Exupery',
         'genre': 'children',
         'tags': ['fantasy', 'France', 'philosophy', 'illustrated', 'fable'],
         'id': '843.912',
         'copies': [{'edition_year': 1983,
                     'checkouts': 634,
                     'borrowed': True,
                     'due_date': '2017/02/02'},
                    {'edition_year': 2015,
                     'checkouts': 41,
                     'borrowed': False}]
         }

library = [book1, book2]

##this is how to read into a json fiile.
with open('./Data/library.json','r') as f:
    reloaded_library = json.load(f)
print(reloaded_library)
print(reloaded_library==library)

## if we simply read a json file like below, we end up with a bunch of strings and unwanted output
with open('./Data/library.json','r') as f:
    library_string = f.read()
print(library_string)

#a better output
print(json.loads(library_string))


#reading a json file with pandas. Pandas tries to pass a json format into a tabular format.
# json files are not well represented in tabular format. notice the output
panda = pd.read_json('./Data/library.json')
print('Panda Tabular JSON', end='\n')
print(panda)

#notice how it is printed with numpy arrays
print(np.array(panda))


#dowloading a json file
# We can download JSON files many ways. Sometimes we will download it manually, but we can also use '!wget' like we did for CSV example. Often we'll connect to a website's API which will respond using JSON.

# Pandas read_json method is capable of connecting directly to a URL (whether it's the address of a JSON file or an API conection) and reading the JSON without saving the file to our computer.

print(pd.read_json('https://api.github.com/repos/pydata/pandas/issues?per_page=5'))



#dumping a JSON file

# with open('./Data/library.json','r') as f:
#    x =  json.dump(library, f, indent= 2)