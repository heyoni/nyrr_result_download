import requests
import json
import csv

page_index = 1



fieldnames = ['runnerId', 'firstName', 'lastName', 'bib', 'age', 'currentAge', 'gender', 'city', 'countryCode', 'stateProvince', 'iaaf',
                  'overallPlace', 'overallTime', 'pace', 'genderPlace', 'ageGradeTime', 'ageGradePlace', 'ageGradePercent', 'racesCount']

try:
    f = open('results.csv', 'x+')
    reswriter = csv.DictWriter(f, fieldnames=fieldnames)
except FileExistsError:
    f = open('results.csv', 'r+')
    reswriter = csv.DictWriter(f, fieldnames=fieldnames)

while True:
    s = """{{"eventCode":"a71104",
    "runnerId":null,
    "searchString":null,
    "gender":"M",
    "handicap":null,
    "ageGroup":null,
    "sortColumn":"overallTime"
    ,"sortDescending":false,
    "city":null,
    "pageIndex":{},
    "pageSize":51}}
    """.format(page_index)

    PAYLOAD = json.loads(s)

    r = requests.post('https://results.nyrr.org/api/runners/finishers', data=PAYLOAD)
    for runner in r.json()['response']['items']:
        reswriter.writerow(runner)
    print(r.json()['response']['items'].__len__())
    if r.json()['response']['items'].__len__() == 0:
        break
    page_index += 1
f.close()
