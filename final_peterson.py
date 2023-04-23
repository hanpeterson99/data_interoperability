#Hannah Peterson
#Final Project

#This documentation was helpful for a lot of this:
#https://pandas.pydata.org/pandas-docs/stable/reference/frame.html

import pandas as pd
import matplotlib.pyplot as plt

#Ignore warnings about using copies of a Dataframe as it doesn't effect anything here
pd.options.mode.chained_assignment = None 

def part1():
    #CSV to dataframe
    df = pd.read_csv('netflix_titles.csv')
    #CSV to XML
    df.to_xml('netflix_titles.xml')
    #CSV to HTML
    df.to_html('netflix.html')
    html_file = df.to_html()


def part2():
    #This website was helpful for plots:
    #https://queirozf.com/entries/pandas-dataframe-plot-examples-with-matplotlib-pyplot 

    #Load to dataframe
    df = pd.read_csv('netflix_titles.csv')

    #Bar chart for count of movies vs tv shows with their ratings
    #After I ran this the first time, I saw that there were some errors in the CSV-
    #Whoever wrote the csv accidentally put some durations in the rating column, so I manually fixed it in my copy of the CSV
    df.groupby(['rating','type']).size().unstack().plot(kind='bar',stacked=True,figsize=(13,7),title='Ratings for Movies and TV Shows')
    plt.show()

    #Bar chart for count of years
    df['release_year'].value_counts().sort_index().plot(kind='bar',figsize=(13,7),title='Amount of Titles per Release Year')
    plt.show()

    #Find number of titles each country has and show top 20
    #Remove space before values that are in a list
    df = df.replace(to_replace ='(?<=,)\s', value = '', regex = True)
    #Split list of countries into list of individual countries
    df['country'] = df['country'].apply(lambda x: str(x).split(","))
    #Explode so that each country is in its own row
    #Help with exploding from here:
    #https://www.kdnuggets.com/2021/05/applying-pythons-explode-function-pandas-dataframes.html
    countries = df.explode('country')
    #Count titles for each country, plot the top 20
    countries['country'].value_counts().sort_index().nlargest(20).plot(kind='barh',figsize=(13,7),title='20 Countries With the Most Titles')
    plt.show()

    #Find 20 most popular actors in US titles
    #Create new dataframe with just US titles
    us = countries.loc[countries['country'] == 'United States']
    #Split list of actors into list of individual actors
    us['cast'] = us['cast'].apply(lambda x: str(x).split(","))
    #Explode so that each actor is in their own row
    actors = us.explode('cast')
    #Count actors and plot the top 20
    actors['cast'].value_counts().sort_index().nlargest(20).plot(kind='barh',figsize=(13,7),title='20 Most Popular Actors in Titles from the US')
    plt.show()

def part3():
    #Load to dataframe
    df = pd.read_csv('netflix_titles.csv')

    #Find top 5 most common first words in titles
    #Split on spaces to get and store the first word of each title
    df['title'] = df['title'].str.split(' ').str[0]
    #Count the number of occurences for first words
    firstCount = df['title'].value_counts().sort_index().nlargest(5)#.plot(kind='bar',figsize=(13,7))
    print("\nThe most popular starting words and their counts:")
    print(firstCount)

    #Find top 10 genres
    #Remove space before items in list
    df = df.replace(to_replace ='(?<=,)\s', value = '', regex = True)
    #Split list of "listed_in" into list of individual categories
    df['listed_in'] = df['listed_in'].apply(lambda x: str(x).split(","))
    #Explode so each category is in its own row
    genres = df.explode('listed_in')
    #Count occurences of each category
    count = genres['listed_in'].value_counts().nlargest(10)
    print('\nThe top 10 categories and their counts:')
    print(count)

    #Find average length of title
    #Reload csv to dataframe 
    df = pd.read_csv('netflix_titles.csv')
    #Split titles by spaces and count number of words
    titleLengthCount = df['title'].str.split(' ').apply(len)
    #Calculate average length
    avgLength = sum(titleLengthCount)/len(titleLengthCount)
    print("\nThe average title length is " +str(avgLength)+" words")

    #Find average movie length
    #Create new dataframe with just movies
    movies = df.loc[df['type'] == 'Movie']
    #Split on space to get rid of "mins" and store number as integer 
    durationLengthCount = movies['duration'].str.split(' ').str[0].astype(int)
    #Calculate average duration
    avgDuration = sum(durationLengthCount)/len(durationLengthCount)
    print("\nThe average movie length is "+str(avgDuration)+" minutes")

    #Find average TV show length
    #Create new dataframe with just TV shows
    shows = df.loc[df['type'] == 'TV Show']
    #Split on space to get rid of "seasons" and store number as integer
    seasonLengthCount = shows['duration'].str.split(' ').str[0].astype(int)
    #Calculate average seasons
    avgSeasons = sum(seasonLengthCount)/len(seasonLengthCount)
    print("\nThe average TV show length is "+str(avgSeasons)+" seasons")


part1()    
part2()
part3()