import psycopg2 as p
import re

def getConnection():
    con = p.connect("dbname='postgres' user='postgres' password='123' host='localhost'")
    return con

# this table assumes that we are throwing away some of the columns in the original xlsx file
def createTweetsTable(con):
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS hashtag")
    cur.close()
    con.commit()
    cur = con.cursor()
    cur.execute("CREATE TABLE tweets ( ID_text SERIAL PRIMARY KEY, handle  VARCHAR(64) NOT NULL,  text    VARCHAR(256),  is_retweet  BOOLEAN,  time    DATE,  retweet_count  INTEGER NOT NULL DEFAULT 0,  favorite_count INTEGER NOT NULL DEFAULT 0 );")
    cur.close()
    con.commit()

# Use postgresql COPY command to automatically import csv file.
# If we export the xlsx file to csv, it will be well formated with predictable escape characters.
# If we export from excel directly, we have to use windows-1251 encoding.
# If we export from google sheets, then it seems to be in UTF-8, which is better.
def copyTweetsToDb(con, csvFile):
    cur = con.cursor()
    cur.execute("COPY tweet (handle, text, is_retweet, time, retweet_count, favorite_count) FROM '"+csvFile+"' DELIMITER ',' ESCAPE '\"' CSV HEADER ENCODING 'windows-1251';")
    #cur.execute("COPY tweets(handle,text,is_retweet,time,retweet_count,favorite_count) FROM '"+csvFile+"' DELIMITER ',' ESCAPE '\"' CSV HEADER;")
    cur.close()
    con.commit()

# create a table to hold all hashtags (with duplicates)
def createHashtagTable(con):
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS hashtags")
    cur.close()
    con.commit()
    cur = con.cursor()
    cur.execute("CREATE TABLE hashtag( ID_hashtag SERIAL PRIMARY KEY, tag VARCHAR(140) NOT NULL, ID_text INTEGER);")
    cur.close()
    con.commit()

# parse all the tweets loaded in the tweets table for hashtags and
# insert the hashtags into the hashtag table.
def extractHashtagsFromTweets(con):
    cur = con.cursor()
    cur.execute("SELECT ID_text,text FROM tweets;")
    rows = cur.fetchall()
    for i in rows:
        # for each tweet, check it for hashtags
        tags = re.findall(r"#(\w+)", i[1])
        if len(tags) > 0:
            for t in tags:
                cur.execute("INSERT INTO  hashtag(tag,ID_text) VALUES ('"+t+"', "+ str(i[0])+");")
    cur.close()
    con.commit()

# ########################

con = getConnection()
createTweetsTable(con)
copyTweetsToDb(con, "/home/michelle/election/american-election-tweets.csv")
createHashtagTable(con)
extractHashtagsFromTweets(con)



