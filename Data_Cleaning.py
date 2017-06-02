# -*- coding: utf-8 -*-
"""
Created on Mon May 29 11:31:56 2017

@author: Elena
"""

import csv

# In the first step we decided on the columns that are important for our task and decided on the attributes "text, "is_retweet", 
# "original_author", "time", "retweet_count" and "favorite_count". As we deleted those columns directly in the csv file and 
# imported the file into our database, no errors were shown. This shows us, that the data had no data type errors. 
# In the second step we thought about doing 

# To be able to work with the csv file, Python has to read it first.
with open ('C:/Users/Elena/Documents/american-election-tweets.csv') as csvfile:
    reader = csv.DictReader(csvfile.read().splitlines(), delimiter=';')
    for row in reader:
        print( row['handle'], row['text'], row['is_retweet'], row['original_author'], row['time'], row[
            'in_reply_to_screen_name'], row['is_quote_status'], row['retweet_count'], row['favorite_count'], row[
            'source_url'],row['truncated'])
print(csvfile)

# In order to achieve some of the defined goals of the project, such as counting the hashtags, we seperated the
# hashtags from the text.
def hashtag(x):
    result=""
    i=0
    while (i != len(x)):
        if(x[i]=='#'):
            while(x[i]!=' '):
                result=result+x[i];
                i=i+1;
        i=i+1;
    return result

# Seperate time into only the time and the date. Give out only the time:
def onlytime(x):
    i=0
    while (x[i] != 'T'):
            i=i+1
    return x[i+1:]



# Seperate time into only the time and the date. Give out date:
def date(x):
    i=0
    while (x[i] != 'T'):
            i=i+1
    return x[:i]




