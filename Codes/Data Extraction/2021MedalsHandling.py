import pandas as pd

medalsDF = pd.read_csv('./medals.csv')
UniqueAthleteMedals = []
for ind in medalsDF.index:
    athleteMedalsList = medalsDF.loc[medalsDF['athlete_link'] == medalsDF['athlete_link'][ind]]
    AthleteMedalDetails = {
        'Medal_Type': [],
        'Medal_Code': [],
        'Medal_Date': [],
        'Short_Name': '',
        'Name': '',
        'Gender': '',
        'URL': '',
        'NOC': '',
        'Discipline': [],
        'Discipline_Code': [],
        'Event': [],
        'Country': '',

    }
    for i in athleteMedalsList.index:
        AthleteMedalDetails['Medal_Type'].append(athleteMedalsList['medal_type'][i])
        AthleteMedalDetails['Medal_Code'].append(athleteMedalsList['medal_code'][i])
        AthleteMedalDetails['Medal_Date'].append(athleteMedalsList['medal_date'][i])
        AthleteMedalDetails['Short_Name'] = athleteMedalsList['athlete_short_name'][i]
        AthleteMedalDetails['Name'] = athleteMedalsList['athlete_name'][i]
        AthleteMedalDetails['Gender'] = athleteMedalsList['athlete_sex'][i]
        AthleteMedalDetails['URL'] = athleteMedalsList['athlete_link'][i]
        AthleteMedalDetails['NOC'] = athleteMedalsList['country_code'][i]
        AthleteMedalDetails['Discipline'].append(athleteMedalsList['discipline'][i])
        AthleteMedalDetails['Discipline_Code'].append(athleteMedalsList['discipline_code'][i])
        AthleteMedalDetails['Event'].append(athleteMedalsList['event'][i])
        AthleteMedalDetails['Country'] = athleteMedalsList['country'][i]
    UniqueAthleteMedals.append(AthleteMedalDetails)
    print(AthleteMedalDetails)
    print(ind)

DF = pd.DataFrame(UniqueAthleteMedals)
print(DF.head())
DF.to_csv('Medals_Unique.csv')
