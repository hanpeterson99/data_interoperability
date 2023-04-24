#HANNAH PETERSON
#Project 1 Part 2

#Import regex
import re

#Write todo.txt to Tasks.txt
with open("Tasks.txt", "w") as t:
    todo = open("todo.txt","r")
    t.write(todo.read())
    todo.close()

#Open and read Tasks.txt
with open("Tasks.txt","r+") as f:
    text = f.read()

    #Attempted to reorder here in many ways but couldn't get it to work :(
    #Date: Task \n\t Name, Phone or Email
    #1=Date 2=Name 3=Phone 4=Email 5=Task
    #text = re.sub('(\d{1,2}[/-]\d{1,2}[/-]\d{4})|([A-Z]\D[^@]{1,10}[A-Z]\D{1,18}(?=,))|([\d-]{14,20}|[\d\s]{14,16}|[\d\(\)-]{12,20}|\([\d\(\-\s)]{10,13})([a-zA-Z0-9-_.]+@[a-zA-Z0-9-_.]+)|([^<1><2><3><4>].*[^<1><2><3><4>])','\\1:\\5\n\t\\2\\3\\4',text)

    #Change date format
    text = re.sub('(\d{1,2})[/-](\d{1,2})[/-](\d{4})','\\3-\\1-\\2',text)
    #Change phone format
    text = re.sub('(\(1-)?(1-)?\(?(\d{3})\)?[ -.]?(\d{3})[ -.]?(\d{4})','(\\3)-\\4-\\5',text)
    #Go to beginning of file, write the re.subs, close
    f.seek(0)
    f.write(text)
    f.truncate()
    f.close()

    #Regexes below for reference 
    #Name: ([A-Z]\D[^@]{1,10}[A-Z]\D{1,18}(?=,))
    #Phone: ([\d-]{14,20}|[\d\s]{14,16}|[\d\(\)-]{12,20}|\([\d\(\-\s)]{10,13})
    #Email: ([a-zA-Z0-9-_.]+@[a-zA-Z0-9-_.]+)
    #Date: (\d{1,2}[/-]\d{1,2}[/-]\d{4})
    #Task: ([^<1><2><3><4>].*[^<1><2><3><4>])