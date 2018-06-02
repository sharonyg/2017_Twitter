import csv
from collections import Counter


def main():
	f = open('./hashtags_pl.csv', 'r')
	hashtags = list(csv.reader(f))
	print(hashtags)



if __name__ == '__main__':
	main()