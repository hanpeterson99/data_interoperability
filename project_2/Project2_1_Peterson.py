#Hannah Peterson
#Project 2 Part 1

import pandas as pd
import csv

#Create header row and insert it at row of index 0
#****Other parts of my project will use this header****
#      (so be sure to run this program first) 
row = ['Name','Email','Category','Amount','Date']
with open('XML_project.csv', 'r') as readfile:
    reader = csv.reader(readfile)
    lines = list(reader)
    lines.insert(0, row)

with open('XML_project.csv', 'w') as writefile:
    writer = csv.writer(writefile)
    writer.writerows(lines)

readfile.close()
writefile.close()

#Convert CSV to dataframe using pandas 
#https://www.geeksforgeeks.org/convert-csv-to-html-table-in-python/ helped me with this
mycsv = pd.read_csv('XML_project.csv')
#Write to HTML using pandas
mycsv.to_html('Project2_1_Peterson.html')
html_file = mycsv.to_html()