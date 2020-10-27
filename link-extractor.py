#link-extractor.py
import csv
import time
import requests
from bs4 import BeautifulSoup

def extract_all_links(url):
    html = requests.get(url)
    content = html.text
    soup = BeautifulSoup(content,'html.parser').find_all('a')
    links = [link.get('href') for link in soup]
    return links

def pretty_print_links(link_lst):
    for link in link_lst:
        print(link)

def write_to_csv(web_links):
    user_input = input('Please enter a save name for the file (basename excluding extension) > ')
    with open(user_input+'.csv','w') as csv_file:
        csv_writer = csv.writer(csv_file)
        for link in web_links:
            csv_writer.writerow([link])

user_provided_url = input('Please paste in your url here: \n')
print('Thank you. Creating list now...')
time.sleep(5)
web_links = extract_all_links(user_provided_url)
pretty_print_links(web_links)
write_to_csv(web_links)
