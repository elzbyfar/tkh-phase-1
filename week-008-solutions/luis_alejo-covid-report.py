from bs4 import BeautifulSoup
import requests
import csv

def rate_of(category, cases):
    case_count = int(cases.replace(',',''))
    category_count = int(category.replace(',',''))
    percentage = (category_count / case_count) * 100
    return str(round(percentage, 1)) + "%"

def parser(data):
    counts = []
    for category in data:
        value = list(category.strings)[0][:-1]
        counts.append(None if value == 'No dat' else value)
    return counts

def covid_report():
    response = requests.get('https://en.wikipedia.org/wiki/Template:COVID-19_pandemic_data')
    soup = BeautifulSoup(response.text)
    
    headings = ['Country', 'Cases', 'Deaths', 'Recoveries', 'Death Rate', 'Recovery Rate']
    matrix = [headings]
    
    table_rows = soup.findAll('tr')[2:]
    
    for tr in table_rows:
        try:
            location = list(tr.findAll('th')[1].strings)[0]
            data = tr.findAll('td')[: -1]
            counts = parser(data)

            cases = counts[0]
            deaths = counts[1]
            recovery = counts[2]
            
            death_rate = rate_of(deaths, cases) if deaths and cases else None
            recovery_rate = rate_of(recovery, cases) if recovery and cases else None

            matrix_row = [location, cases, deaths, recovery, death_rate, recovery_rate]
            matrix.append(matrix_row)
        except:
            break

    return matrix

if __name__ == '__main__':
    output_to_file = open('luis_alejo-covid-report.csv', 'w')
    writefile = csv.writer(output_to_file)
    writefile.writerows(covid_report())
    output_to_file.close()