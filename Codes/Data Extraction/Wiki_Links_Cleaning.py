# Comment Remaining section while running for one section

# ------------------------------
# To scrape links
# ------------------------------

import time
import pandas as pd
import requests
from bs4 import BeautifulSoup

AthletesDF = pd.read_csv('./Final_Cleaned1.csv')
count = 0
for ind in AthletesDF.index:
    if ind < 20000:
        continue
    if AthletesDF['Wiki_Links'][ind] == 'None' or AthletesDF['Wiki_Links'][ind] == 'AOL':
        count += 1
        query = AthletesDF['Name'][ind] + ' Wiki'
        response = requests.get("https://in.search.yahoo.com/search;?p=" + query + "&fr=sfp&iscqry=&fr2=sb-top-search")
        soupObject = BeautifulSoup(response.text, 'html.parser')
        a_tag = soupObject.find_all('a', attrs={
            'class': ['d-ib', 'ls-05', 'fz-20', 'lh-26', 'td-hu', 'tc', 'va-bot', 'mxw-100p']})
        check = 0
        for a in a_tag:
            if 'en.wikipedia.org' in a['href']:
                print(ind, AthletesDF['Name'][ind], a['href'])
                if input() == '1':
                    AthletesDF['Wiki_Links'][ind] = a['href']
                    check = 1
                else:
                    AthletesDF['Wiki_Links'][ind] = 'None'
                    check = 1
                break
            elif 'wikipedia.org' in a['href']:
                AthletesDF['Wiki_Links'][ind] = 'AOL'
                print(ind, AthletesDF['Name'][ind], 'AOL')
                check = 1
                break
        if not check:
            AthletesDF['Wiki_Links'][ind] = 'None'
            print(ind, AthletesDF['Name'][ind], 'None')
        AthletesDF.to_csv('Final_Cleaned.csv')
        time.sleep(1)
        if (ind + 1) % 100 == 0:
            time.sleep(60)
# print(count)


# -----------------------------
# To clean the Links
# -----------------------------

import time
import pandas as pd
import requests
from bs4 import BeautifulSoup

AthletesDF = pd.read_csv('./Final_Cleaned.csv')
count = 0
for ind in AthletesDF.index[20000:]:
    if AthletesDF['Wiki_Links'][ind] == 'AOL':
        continue
    Names = AthletesDF['Name'][ind].split()
    check = 0
    for name in Names:
        if name in AthletesDF['Wiki_Links'][ind]:
            check = 1
            break
    if not check:
        AthletesDF['Wiki_Links'][ind] = 'None'

print(count)
AthletesDF.to_csv('Final_Cleaned1.csv')


# -----------------------------------
# To find the count of None and AOL
# -----------------------------------

import pandas as pd

AthletesDF = pd.read_csv('./Final_Cleaned_10k-30k.csv')
count = 0
for ind in AthletesDF.index[10000:]:
    if AthletesDF['Wiki_Links'][ind] == 'None':
        count += 1
print(count)

# ----------------------------------------
# To merge the files
# ----------------------------------------
import pandas as pd
DF_0_10 = pd.read_csv('Final_1-30k_With_Labels2.csv')
DF_20_30 = pd.read_csv('New_Athletes_With_Labels_20-30k_.csv')
for ind in DF_0_10.index[:10000]:
    DF_20_30['Label'][ind] = DF_0_10['Label'][ind]
    print(ind, DF_0_10['Name'][ind])
DF_20_30.to_csv('./New_Athletes_With_Labels.csv')

# ---------------------------------------------
# To add Column
# ---------------------------------------------
import pandas as pd
AthletesDF = pd.read_csv('./Athletes_With_Labels_20-30k.csv')
values = ['' for ind in AthletesDF.index]
AthletesDF['Date_Of_Birth'] = values
AthletesDF['Birth_Place'] = values
AthletesDF['StateOfOrigin'] = values
AthletesDF['Thumbnail'] = values
AthletesDF['Club'] = values
AthletesDF['Coach'] = values
AthletesDF['Education'] = values
AthletesDF['Residence'] = values
AthletesDF['Caption'] = values
AthletesDF['Gold_Medals'] = values
AthletesDF['Silver_Medals'] = values
AthletesDF['Bronze_Medals'] = values
AthletesDF['FlagBearer'] = values
AthletesDF.to_csv('./New_Athletes_With_Labels_20-30k_.csv')

# -------------------------------------------------
# To get the Labels
# -------------------------------------------------

import pandas as pd
import requests
from bs4 import BeautifulSoup
import time
import wikipediaapi

wiki_wiki = wikipediaapi.Wikipedia('en')

df = pd.read_csv('./Final_1-30k_With_Labels1.csv')
# urls = df['Wiki_Links']
i = 8262
# labels = []
# links = []
s_time = time.time()
for ind in df.index[9680:10000]:
    if df['Wiki_Links'][ind] == 'None' or df['Wiki_Links'][ind] == 'AOL':
        continue
    try:
        response = requests.get(df['Wiki_Links'][ind])
        soup = BeautifulSoup(response.text, 'html.parser')
        header = soup.findAll('h1')
        label = header[0].text
        # print(label)
        page_py = wiki_wiki.page(label)
        link = page_py.canonicalurl
        # labels.append(label)
        df['Label'][ind] = label
        print(label)
        # links.append(link)
    except:
        # labels.append("None")
        df['Label'][ind] = label
        # links.append("None")
        print('None')
    i += 1
    print(i)
    # time.sleep(0.5)
    df.to_csv('./Final_1-30k_With_Labels2.csv')
e_time = time.time()
