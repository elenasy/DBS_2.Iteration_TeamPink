
# We would like to work with the table. For that reason, Python must be able to read the csv file.
with open ('C:/Users/Elena/Documents/american-election-tweets.csv') as csvfile:
    reader = csv.DictReader(csvfile.read().splitlines(), delimiter=';')
    for row in reader:
        print( row['handle'], row['text'], row['is_retweet'], row['original_author'], row['time'], row[
            'in_reply_to_screen_name'], row['is_quote_status'], row['retweet_count'], row['favorite_count'], row[
            'source_url'],row['truncated'])
# print(csvfile)



# In order to work with the hashtags to acomplish our goals of the project, they need to be separated from the text.
def hashtag(x):
    result=""
    i=0
    while (i != len(x)):
        if(x[i]=='#'):
            while(x[i]!=' '):
                result=result+x[i];
                i=i+1;
        i=i+1;
    return result# DBS_2.Iteration_TeamPink
Data cleaning and data import

# Seperate time into only the time and the date, the text was posted. Give out only the time:
def onlytime(x):
    i=0
    while (x[i] != 'T'):
            i=i+1
    return x[i+1:]

# Seperate time into only the time and the date, the text was posted. Give out date:
def date(x):
    i=0
    while (x[i] != 'T'):
            i=i+1
    return x[:i]
