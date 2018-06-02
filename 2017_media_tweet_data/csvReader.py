import csv
import sys
import json
import codecs
import itertools

url_name = {}
# f = open('./Taiwan_long_17_1_join_media_tweets.csv', 'r')
reader_url = csv.DictReader(codecs.open('./Taiwan_long_17_1_join_media_tweets.csv', 'rb', 'utf-8'))
# reader_url = csv.DictReader((line.replace('0x00', '')for line in f))

count = 0
# for row in reader_url:
for row in itertools.islice(reader_url, 0, 1):
    count = count + 1
    print(row)
    # if row['id'] == "817611011721043968": 
    #    print(row)
print(count)