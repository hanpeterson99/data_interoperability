#Hannah Peterson
#Lab 9, Step 3 Part 1

from xml.etree import ElementTree
import pandas as pd

tree = ElementTree.parse('simmons_programming_books.xml')
root = tree.getroot()

#Initiate lists
cols = ["Doctype", "Book Published"]
rows = {}
books = []
doctype = []

#Get book titles
for child in root.iter('btl'):
    books.append(child.text)
#Get doc type
for child in root.iter('doctype'):
    doctype.append(child.text)
#Add to list of tuples
rows = list(zip(doctype,books))

#Create dataframe for book titles and their doctypes
df = pd.DataFrame(rows, columns=cols)

#Count doctypes & output to CSV
df.rename(columns={'Doctype':'Doctype Count'},inplace=True)
doctypecount = df['Doctype Count'].value_counts()
doctypecount.to_csv('doctypesCount.csv')
