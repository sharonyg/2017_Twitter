import csv
from collections import Counter


def main():
	words = []

	# Open the hashtags csv file.
	f = open('./hashtags_zh.csv', 'r')
	hashtags = csv.reader(f)
	for row in hashtags:
	 	words.append(row[0])
	# print(words)
	f.close()

	# Count each word appear how many times.
	word_count = Counter(words).most_common()
	# print(word_count[0])

	# Write csv file.
	with open('./count_zh.csv', 'w') as g:
		writer = csv.writer(g)
		for row in word_count:
			writer.writerow(row)
	g.close()



if __name__ == '__main__':
	main()