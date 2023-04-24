#Hannah Peterson
#Project 2 Part 3

import pandas as pd
import re
from lxml import etree

#Convert CSV to dataframe
df = pd.read_csv('XML_project.csv')

#Convert to XML
#https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_xml.html
xml = df.to_xml()

#Make changes to work with budgets.xsd
xml = re.sub('<index>.+</index>','',xml)
xml = re.sub('Name','name',xml)
xml = re.sub('Email','email',xml)
xml = re.sub('Amount','amount',xml)
xml = re.sub('Category','category',xml)
xml = re.sub('Date','date',xml)
xml = re.sub('data','budget',xml)
xml = re.sub('row','budget_item',xml)
xml = re.sub('(<name>)(\w+)()','\\1<firstname>\\2\\3</firstname>',xml)
xml = re.sub('()(\w+)()(</name>)','\\1<lastname>\\2\\3</lastname>\\4',xml)
xml = re.sub('\$','',xml)
xml = re.sub('(?<=>)\s(?=<)','',xml)
xml = re.sub('(<category>.*</category>)\s*(<amount>.*</amount>)','\\2\n\t\t\\1',xml)
xml = re.sub('<budget(?=>)','<budget xmlns:xs="http://www.w3.org/2001/XMLSchema"',xml)

#Write to xml file
f = open('csvToXml.xml','w')
for line in xml:
    f.write(line)
f.close()

#Validate against budgets.xsd
#read in the schema, parse it, and save as a variable
xmlschema_doc = etree.parse("budgets.xsd")
#use the parsed data to create an XMLSchema object
xmlschema = etree.XMLSchema(xmlschema_doc)
#read in the XML file you want to validate
doc = etree.parse("csvToXml.xml")
#check to make sure the file adheres to the schema
print(xmlschema.validate(doc))
#if invalid, show where/why
xmlschema.assertValid(doc)
#Kept getting this error:
#Element 'name': Character content other than whitespace is not allowed because the content type is 'element-only'
#Not sure how to fix it but the XML looks good to me

