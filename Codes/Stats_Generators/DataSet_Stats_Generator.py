import pandas as pd

DF = pd.read_csv('./New_Athletes_With_Labels.csv')
AthletesInEachCountry = {}
MedalWinners = 0
NonMedalWinners = 0
for ind in DF.index:
    if DF['Country'][ind] in AthletesInEachCountry.keys():
        AthletesInEachCountry[DF['Country'][ind]] += 1
    else:
        AthletesInEachCountry[DF['Country'][ind]] = 1
    if 'Gold' in DF['Medals'][ind]:
        MedalWinners += 1
    elif 'Silver' in DF['Medals'][ind]:
        MedalWinners += 1
    elif 'Bronze' in DF['Medals'][ind]:
        MedalWinners += 1
    else:
        NonMedalWinners += 1

print('Medal Winners :', MedalWinners)
print('Non Medal Winners :', NonMedalWinners)
Total = 0
totalKeys = 0
for key in AthletesInEachCountry.keys():
    totalKeys += 1
    Total += AthletesInEachCountry[key]
    print(key, ":", AthletesInEachCountry[key])
print(Total, totalKeys)
