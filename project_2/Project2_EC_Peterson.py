#Hannah Peterson
#Project 2 Extra Credit

import pandas as pd

#Open CSV and convert to dataframe 
mycsv = pd.read_csv('XML_project.csv')
#Group by category
byCat = mycsv.groupby(['Category'])
#Convert back to dataframe and count occurences of each category
byCat = pd.DataFrame(byCat.size().reset_index(name='count'))
#Generate HTML
byCat.to_html('Project2_EC_Peterson.html')
html_file = byCat.to_html()