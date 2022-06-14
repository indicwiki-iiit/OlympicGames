import requests
import pandas as pd
from bs4 import BeautifulSoup
import time

DF = pd.read_csv('./Athletes.csv')
print(DF.head())
AthleteName = DF['Name']
AthleteCountry = DF['Country']
urls = []
for i in range(len(AthleteName))[30001:]:
    if AthleteCountry[i] == "None":
        query = AthleteName[i] + " site:wikipedia.org"
    else:
        query = AthleteName[i] + " " + AthleteCountry[i] + " site:wikipedia.org"
    l1 = []
    print(i + 1, AthleteName[i])
    response = requests.get("https://in.search.yahoo.com/search;?p=" + query + "&fr=sfp&iscqry=&fr2=sb-top-search")
    soupObject = BeautifulSoup(response.text, 'html.parser')
    a_tag = soupObject.find_all('a', attrs={'class': ['d-ib', 'ls-05', 'fz-20', 'lh-26', 'td-hu', 'tc', 'va-bot', 'mxw-100p']})
    check = 0
    for a in a_tag:
        if 'en.wikipedia.org' in a['href']:
            urls.append(a['href'])
            print(a['href'])
            check = 1
            break
    if not check:
        urls.append('None')
        print('None')
    Links = pd.DataFrame(urls, columns=['Links'])
    Links.to_csv('./AthleteLinks30.csv')
    time.sleep(1)
    if (i + 1) % 100 == 0:
        time.sleep(300)
print(len(urls))
for u in urls:
    print(u)
