#Hannah Peterson
#Project 2 Part 2

import pandas as pd

#Open csv that now has proper headers from part 1
mycsv = pd.read_csv('XML_project.csv')
df = pd.DataFrame(mycsv)

#Get rid of dollar sign in amount
df['Amount'] = df['Amount'].str.replace('$', '')
df['Amount'] = df['Amount'].astype(float)

#1: Tally the total amounts for each budget category
maxByCategory = df.groupby(['Category']).sum()
print('The total amounts for each budget category are:')
print(maxByCategory)

#2: Determine which budget category people spent the most money in
maxCategoryAmount = float(maxByCategory.max())
maxCategory = maxByCategory.loc[maxByCategory['Amount'] == maxCategoryAmount]
print('People spent the most money in this category: ')
print(maxCategory)

#3: Tally the total amounts for each year-month
#Got help converting dates to datetime from here:
#https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html
#And using Grouper here:
#https://pandas.pydata.org/docs/reference/api/pandas.Grouper.html
df['Date'] = pd.to_datetime(df['Date'])
maxByDate = df.groupby(pd.Grouper(key='Date',freq='M')).sum()
print('The total amount for each end-of-month are: ')
print(maxByDate)

#4: Determine which person spent the most money on a single item
maxAmount = df['Amount'].max()
maxPerson = df.loc[df['Amount'] == maxAmount]
print('The person who spent the most money on a single item is: ')
print(maxPerson)