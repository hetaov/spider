# -*- coding: utf-8 -*-

import pandas as pds
import json


def main():

	'''
	df = pds.read_json('data/word/components_word_new.json', encoding='utf-8', orient='records')

	for index, row in df.iterrows():
		print row
	'''

	f = open('data/word/components_word_new.json')

	s = f.read()

	o = json.loads(s)

	#print o
	
if __name__ == '__main__':
    main()
