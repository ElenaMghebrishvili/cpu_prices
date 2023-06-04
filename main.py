import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
from random import randint

url = 'https://www.newegg.com/tools/custom-pc-builder/pl/ID-147/Page-{page}?diywishlist=0'
file = open('cpu.csv', mode='w', newline='\n')
csv_obj = csv.writer(file)
csv_obj.writerow(['Model', 'Price'])

for page in range(1, 6):
    url1 = url.format(page=page)
    r = requests.get(url1)
    print(r)
    content = r.text
    soup = BeautifulSoup(content, 'html.parser')
    cpus_soup = soup.find('table', class_='table-vertical')
    all_cpus = cpus_soup.find_all('td', class_='td-item')
    all_cpus_price = cpus_soup.find_all('li', class_='price-current')

    for cpu, cpu_price in zip(all_cpus, all_cpus_price):
        model = cpu.span.text
        # print(model)
        price = f'{cpu_price.strong.text}{cpu_price.sup.text} $'
        # print(price)
        csv_obj.writerow([model, price])

    sleep(randint(10, 15))