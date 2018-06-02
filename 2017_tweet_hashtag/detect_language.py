import csv
import langid
import itertools
from tqdm import tqdm
import time



def main():
    hashtag_list = [[] for i in range(5)]
    lang = ['zh', 'en', 'pl', 'ja', 'ko']
    count = 0

    # Read csv file
    f = open('./Taiwan_long_17_1_clean_hashtags.csv', 'r')
    reader_url = csv.reader(f)
    # data = list(itertools.islice(reader_url, 1, 501))
    data = list(reader_url) # Why using list(): Let tqdm knows the length.
    print("tags count: ", len(data))

    # Detect language of each line
    # for row in reader_url:
    for row in tqdm(data):
        language = langid.classify(row[5])
        for i in range(5):
            if language[0] == lang[i]:
                hashtag_list[i].append(row[5])
    
    print("-" * 105)
    f.close()

    # Write csv files
    for i in range(5):
        print("%s hashtags:" % lang[i])
        write_csv_file(hashtag_list[i], lang[i])


# Write each language of text to each csv file
def write_csv_file(hashtags, language):
    with open('./hashtags_%s.csv' % language, 'w') as g:
        writer = csv.writer(g)
        for text in tqdm(hashtags):
            writer.writerows([[text]])
    g.close()

if __name__ == '__main__':
	main()
