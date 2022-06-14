import pandas as pd

# -----------------------
# To clean Club Attribute
# -----------------------

DF = pd.read_csv('./10clb.csv')
for ind in DF.index[:10000]:
    print(ind)
    if pd.isna(DF['Club'][ind]):
        DF['Club'][ind] = 'None'
    if DF['Club'][ind] is None:
        continue
    elif 'http://dbpedia.org/resource/' in DF['Club'][ind]:
        DF['Club'][ind] = DF['Club'][ind].split('/')[-1]
DF.to_csv('Cleaned_Data_With_Club_0-10k.csv')

# ------------------------------
# To clean Birth Place Attribute
# ------------------------------

DF = pd.read_csv('./Data_With_POB_0-10k.csv')
for ind in DF.index[:10000]:
    print(ind)
    if pd.isna(DF['Birth_Place'][ind]):
        DF['Birth_Place'][ind] = 'None'
    if DF['Birth_Place'][ind] is None:
        continue
    elif 'http://dbpedia.org/resource/' in DF['Birth_Place'][ind]:
        DF['Birth_Place'][ind] = DF['Birth_Place'][ind].split('/')[-1]
DF.to_csv('Cleaned_Data_With_POB_0-10k.csv')

# ----------------------------------
# To clean State of Origin Attribute
# ----------------------------------

DF = pd.read_csv('./Data_With_StateOfOrigin_0-10k.csv')
for ind in DF.index[:10000]:
    print(ind)
    if DF['StateOfOrigin'][ind] is None:
        continue
    elif 'http://dbpedia.org/resource/' in DF['StateOfOrigin'][ind]:
        DF['StateOfOrigin'][ind] = DF['StateOfOrigin'][ind].split('/')[-1]
DF.to_csv('Cleaned_Data_With_StateOfOrigin_0-10k.csv')

# ----------------------------------
# To clean State of Coach Attribute
# ----------------------------------

DF = pd.read_csv('./Data_With_Coach_1-10k.csv')
for ind in DF.index[:10000]:
    print(ind)
    # print(DF['Coach'][ind], type(DF['Coach'][ind]))
    if pd.isna(DF['Coach'][ind]):
        DF['Coach'][ind] = 'None'
        # print(ind)
    if 'http://dbpedia.org/resource/' in DF['Coach'][ind]:
        DF['Coach'][ind] = DF['Coach'][ind].split('/')[-1]
DF.to_csv('Cleaned_Data_With_Coach_0-10k.csv')


# ----------------------------------
# To clean Residence of Origin Attribute
# ----------------------------------

DF = pd.read_csv('./10res.csv')
for ind in DF.index[:10000]:
    print(ind)
    if DF['Residence'][ind] is None:
        continue
    elif 'http://dbpedia.org/resource/' in DF['Residence'][ind]:
        DF['Residence'][ind] = DF['Residence'][ind].split('/')[-1]
DF.to_csv('Cleaned_Data_With_Residence_0-10k.csv')

# ----------------------------------
# To clean Education Attribute
# ----------------------------------

DF = pd.read_csv('./10edu.csv')
for ind in DF.index[:10000]:
    print(ind)
    # print(DF['Coach'][ind], type(DF['Coach'][ind]))
    if DF['Education'][ind] == 'None':
        continue
    if 'http://dbpedia.org/resource/' in DF['Education'][ind]:
        DF['Education'][ind] = DF['Education'][ind].split('/')[-1]
DF.to_csv('Cleaned_Data_With_Education_0-10k.csv')


# ------------------------
# To clean from 10k to 20k
# ------------------------

DF = pd.read_csv('./New_Athletes_With_Attributes_10-30k.csv')
for ind in DF.index[10000:20000]:
    print(ind)
    if pd.isna(DF['Club'][ind]):
        DF['Club'][ind] = 'None'
    if 'http://dbpedia.org/resource/' in DF['Club'][ind]:
        DF['Club'][ind] = DF['Club'][ind].split('/')[-1]
    if pd.isna(DF['Birth_Place'][ind]):
        DF['Birth_Place'][ind] = 'None'
    if 'http://dbpedia.org/resource/' in DF['Birth_Place'][ind]:
        DF['Birth_Place'][ind] = DF['Birth_Place'][ind].split('/')[-1]
    if pd.isna(DF['StateOfOrigin'][ind]):
        DF['StateOfOrigin'][ind] = 'None'
    if 'http://dbpedia.org/resource/' in DF['StateOfOrigin'][ind]:
        DF['StateOfOrigin'][ind] = DF['StateOfOrigin'][ind].split('/')[-1]
    if pd.isna(DF['Coach'][ind]):
        DF['Coach'][ind] = 'None'
    if 'http://dbpedia.org/resource/' in DF['Coach'][ind]:
        DF['Coach'][ind] = DF['Coach'][ind].split('/')[-1]
    if pd.isna(DF['Residence'][ind]):
        DF['Residence'][ind] = 'None'
    if 'http://dbpedia.org/resource/' in DF['Residence'][ind]:
        DF['Residence'][ind] = DF['Residence'][ind].split('/')[-1]
    if pd.isna(DF['Education'][ind]):
        DF['Education'][ind] = 'None'
    if 'http://dbpedia.org/resource/' in DF['Education'][ind]:
        DF['Education'][ind] = DF['Education'][ind].split('/')[-1]
DF.to_csv('Cleaned_New_Athletes_With_Attributes_10-30k.csv')
