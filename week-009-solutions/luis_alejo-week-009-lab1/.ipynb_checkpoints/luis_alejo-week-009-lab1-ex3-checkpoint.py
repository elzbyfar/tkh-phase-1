from bs4 import BeautifulSoup
import requests
import csv

def language_timeline():
    res = requests.get('https://en.wikipedia.org/wiki/Timeline_of_programming_languages')
    soup = BeautifulSoup(res.text)
    
    headers = ['Year', 'Name', 'Chief Developer / Company', 'Predecessor(s)']
    matrix = [headers]
    
    table_rows = soup.findAll('tr')[7:]
    for tr in table_rows:
        try:
            test_row = [s.strip() for s in list(tr.strings) if s != '\n']
            year = test_row[0]
            if year != 'Year':
                tds = tr.findAll('td')
                row = [s.text.strip() for s in tds]
                matrix.append(row)
            if year == '2019':
                break
        except:
            break
    return matrix

if __name__ == '__main__':
    file = open('luis_alejo-language-timeline.csv', 'w')
    writer = csv.writer(file)
    writer.writerows(language_timeline())
    file.close()