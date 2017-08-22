# -*- coding: utf-8 -*-

from googleapiclient.discovery import build

def main():
    service = build('translate', 'v2', developerKey='AIzaSyDRRpR3GS1F1_jKNNM9HCNd2wJQyPG3oN0')
    print(service.translations().list(
          source='en',
          target='zh',
          q=['flower', 'car']
        ).execute())

if __name__ == '__main__':
    main()
