import psycopg2
import csv
import re
import sys
#Aufgabe2 komplett, und Aufgabe 3 teilweise, denn import psycopg2 hat nicht richtig geladen
#verbindet mit der Datei "american-election"
def getConnection():
    con = psycopg2.connect("dbname='election' user='postgres' password='postgres' host='localhost'")
    return con

def importCVS():
    add_hasttag = ("INSERT INTO hashtag "
              "(h_text) "
              "VALUES (%(h_text)s)")
    with open('C:/Users/Yasemin Savranoglu/Desktop/american-election-tweets.csv') as electionFile:
        electionFileReader = csv.DictReader(electionFile,delimiter=';')
        electionList = []
        nrow = {};
        ##store list of hastags and later insert in hastags table
        hashtags = [];#hasttags per text 
        hasttagsList = [];
        con = getConnection();
        cur = con.cursor()
        for row in electionFileReader:
            if len (row) != 0:
                h = findHashtags(row["text"])
                hashtags.append(h);
                if len(hashtags)!=0:
                    hasttagsList+=findHashtags(h);
                row["date"] = dated(row["time"]);
                row["time"] = onlytime(row["time"]);
                sql="INSERT INTO text(retweet_count, favorite_count, date, time) VALUES ("+row["retweet_count"]+","+row["retweet_count"]+","+row["date"]+","+row["time"]+");";     
              
               cur.execute(sql);
    con.commit();
    con.close();
    #to get rid of mutiple hashtags
    #
    hasttagsSet= set(hasttagsList);
    print(hashtags);
    electionFile.close()
    

# Seperate time into newtime and date. Give out onlytime:
def onlytime(x):
    i=0
    while (x[i] != 'T'):
            i=i+1
    return x[i+1:]



# Seperate time into newtime and date. Give out date:
def dated(x):
    i=0
    while (x[i] != 'T'):
            i=i+1
    return x[:i]
             
def findHashtags(x):
   return re.findall(r"#(\w+)", x);
importCVS();
