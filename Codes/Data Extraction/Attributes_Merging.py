import pandas as pd

AthletesDF = pd.read_csv('New_Athletes_With_Attributes_0-30k_edu_res_pob_thumb_origin_coach_club_caption.csv')
pobDF = pd.read_csv('./Cleaned_Data_With_POB_0-10k.csv')
thumbDF = pd.read_csv('./Cleaned_Data_With_Thumbail_0-10k.csv')
DF = pd.read_csv('./Data_With_DOB_1-10k.csv')

for ind in AthletesDF.index[:10000]:
    print(ind)
    AthletesDF['Date_Of_Birth'][ind] = DF['Date_Of_Birth'][ind]
    AthletesDF['Birth_Place'][ind] = pobDF['Birth_Place'][ind]
    AthletesDF['StateOfOrigin'][ind] = soODF['StateOfOrigin'][ind]
    AthletesDF['Thumbnail'][ind] = thumbDF['Thumbnail'][ind]
    AthletesDF['Club'][ind] = DF['Club'][ind]
    AthletesDF['Coach'][ind] = DF['Coach'][ind]
    AthletesDF['Education'][ind] = eduDF['Education'][ind]
    AthletesDF['Residence'][ind] = resDF['Residence'][ind]
    AthletesDF['Caption'][ind] = DF['Caption'][ind]
AthletesDF.to_csv('./New_Athletes_With_Attributes.csv')
