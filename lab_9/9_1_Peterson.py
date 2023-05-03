#Hannah Peterson
#Lab 9, Step 1 Part 1

from xml.etree import ElementTree
import pandas as pd

tree = ElementTree.parse('simmons_programming_books.xml')
root = tree.getroot()

#Initiate lists
cols = ["Year Published", "Book Title"]
rows = {}
books = []
years = []

#Get book titles
for child in root.iter('btl'):
    books.append(child.text)
#Get years
for child in root.iter('dt'):
    years.append(child.get('year'))
#Add to list of tuples
rows = list(zip(years,books))

#Dataframe & CSV for book titles and their years
df = pd.DataFrame(rows, columns=cols)
df.to_csv('booksAndYear.csv')

#Rename column, count years, & output to CSV
#This helped me with renaming a specific column:
#https://stackoverflow.com/questions/11346283/renaming-column-names-in-pandas 
df.rename(columns={'Year Published':'# of Books Published'},inplace=True)
yearcount = df['# of Books Published'].value_counts()
yearcount.to_csv('booksPerYear.csv')