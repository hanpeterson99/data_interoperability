#Hannah Peterson
#Lab 9, Step 1 Part 2 

import xml.etree.ElementTree as ET
from collections import Counter
import pandas as pd

#Counter help here:
#https://docs.python.org/3/library/collections.html#collections.Counter
myfile = 'simmons_programming_books.xml'
my_tags = []
for event, element in ET.iterparse(myfile):
    my_tags.append(element.tag)
    my_keys = Counter(my_tags).keys()
    my_values = Counter(my_tags).values()
    my_dict = dict(zip(my_keys, my_values))

cols = ['Tag Count']
#from_dict help here:
#https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.from_dict.html#
df = pd.DataFrame.from_dict(my_dict, orient='index', columns=cols)
df.to_csv('tagcount.csv')
    




