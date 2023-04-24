#HANNAH PETERSON
#Project 1 Part 1

#Import regex
import re

#Copy HTML to text file
with open('HenryV.html','r') as html, open('HenryV.txt','a') as text:
    for line in html:
             text.write(line)

#Open HenryV text file
filename = 'HenryV.txt'
with open(filename,'r+') as f:
    text = f.read()
    #Get rid of head
    text = re.sub('<head>(?:.|\n|\r)+?</head>', '',text)
    #Change ACT
    text = re.sub('<h3>ACT', '==ACT',text)
    text = re.sub('(?<=[IVX])</h3>', '==',text)
    #Change SCENE
    text = re.sub('((?<=SCENE).*(?=</h3))', '\\1}',text)
    text = re.sub('(SCENE.[IVX.]+)', '\\1=\n{',text)
    text = re.sub('<h3>SCENE', '=SCENE',text)
    #Change stage directions
    text = re.sub('<i>', '[', text)
    text = re.sub('</i>', ']', text)
    #Change announcements
    text = re.sub('(<a name="speech\d+"><b>)(.*)(</b></a>)','\\2:',text)
    #Get rid of HTML and indent
    text = re.sub('[<].*?[>]', '\t', text)
    #Go to beginning of file, write re.subs, close
    f.seek(0)
    f.write(text)
    f.truncate()
    f.close()

