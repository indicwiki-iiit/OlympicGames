import pandas as pd

Data = pd.read_csv('./athlete_events.csv')
print(Data.head())
Unique_Entries = []
for i in range(1, 135572):
    athlete_list = Data.loc[Data['ID'] == i]
    AthleteDetails = {
        'ID': 0,
        'Name': '',
        'Gender': '',
        'Age': 0,
        'Height': 0.0,
        'Weight': 0.0,
        'Country': '',
        'NOC': '',
        'Games': [],
        'Years': [],
        'Seasons': [],
        'Cities': [],
        'Sports': [],
        'Events': [],
        'Medals': [],
    }
    check = 0
    for athlete_index in athlete_list.index:
        # print(athlete_list['Year'][athlete_index], type(athlete_list['Year'][athlete_index]))
        if athlete_list['Year'][athlete_index] in [2004, 2008, 2012, 2016]:
            check = 1
            break
    if check:
        for athlete_index in athlete_list.index:
            AthleteDetails['ID'] = athlete_list['ID'][athlete_index]
            AthleteDetails['Name'] = athlete_list['Name'][athlete_index]
            AthleteDetails['Gender'] = athlete_list['Sex'][athlete_index]
            if AthleteDetails['Age'] == 0:
                AthleteDetails['Age'] = athlete_list['Age'][athlete_index]
            elif athlete_list['Age'][athlete_index] != float('NaN') and AthleteDetails['Age'] != float('NaN'):
                AthleteDetails['Age'] = max((AthleteDetails['Age']), (athlete_list['Age'][athlete_index]))
            else:
                AthleteDetails['Age'] = 'NA'
            AthleteDetails['Height'] = athlete_list['Height'][athlete_index]
            AthleteDetails['Weight'] = athlete_list['Weight'][athlete_index]
            AthleteDetails['Country'] = athlete_list['Team'][athlete_index]
            AthleteDetails['NOC'] = athlete_list['NOC'][athlete_index]
            AthleteDetails['Games'].append(athlete_list['Games'][athlete_index])
            AthleteDetails['Years'].append(athlete_list['Year'][athlete_index])
            AthleteDetails['Seasons'].append(athlete_list['Season'][athlete_index])
            AthleteDetails['Cities'].append(athlete_list['City'][athlete_index])
            AthleteDetails['Sports'].append(athlete_list['Sport'][athlete_index])
            AthleteDetails['Events'].append(athlete_list['Event'][athlete_index])
            AthleteDetails['Medals'].append(athlete_list['Medal'][athlete_index])

        # for key in AthleteDetails.keys():
            # print(key, ":", AthleteDetails[key])
        Unique_Entries.append(AthleteDetails)
        AthleteDetails = {
            'ID': 0,
            'Name': '',
            'Gender': '',
            'Age': 0,
            'Height': 0.0,
            'Weight': 0.0,
            'Country': '',
            'NOC': '',
            'Games': [],
            'Years': [],
            'Seasons': [],
            'Cities': [],
            'Sports': [],
            'Events': [],
            'Medals': [],
        }
        print(i)

AthleteDF = pd.DataFrame(Unique_Entries)
print(AthleteDF.head())
AthleteDF.to_csv('Athletes.csv')
