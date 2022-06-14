import pandas as pd

athletesDF = pd.read_csv('./Athletes_Unique.csv')
medalsDF = pd.read_csv('./Medals_Unique.csv')

Medal_Type = []
Medal_Code = []
Medal_Date = []
Event = []

for ind in athletesDF.index:
    medalDetails = medalsDF.loc[medalsDF['URL'] == athletesDF['URL'][ind]]
    if not len(medalDetails.index):
        Medal_Type.append([])
        Medal_Code.append([])
        Medal_Date.append([])
        Event.append([])
    else:
        for i in medalDetails.index:
            Medal_Type.append(medalDetails['Medal_Type'][i])
            Medal_Code.append(medalDetails['Medal_Code'][i])
            Medal_Date.append(medalDetails['Medal_Date'][i])
            Event.append(medalDetails['Event'][i])
    print(ind)
athletesDF['Medal_Type'] = Medal_Type
athletesDF['Medal_Code'] = Medal_Code
athletesDF['Medal_Date'] = Medal_Date
athletesDF['Event'] = Event
athletesDF.to_csv('Athletes-2021.csv')
