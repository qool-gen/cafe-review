import pandas as pd

df_country = pd.read_csv('country.csv')
lst_country = sorted(list(df_country['Country']))

df_aux = pd.read_csv('aux.csv')
lst_aux = sorted(list(df_aux['Aux']))

def get_codes_countries(countries):
    codes = []
    for k in range(len(lst_country)):
        if lst_country[k] in countries:
            codes.append('1')
        else:
            codes.append('0')
    return ''.join(codes)
    
def get_codes_auxes(auxes):
    codes = []
    for k in range(len(lst_aux)):
        if lst_aux[k] in auxes:
            codes.append('1')
        else:
            codes.append('0')
    return ''.join(codes)

def app_countries(s):
    items = s.split(',') if ',' in s else [s]
    countries = []
    auxes = []
    for item in items:
        item = item.strip().replace('-',' ')
        if item in lst_country:
            countries.append(item)
        else:
            auxes.append(item)
    cuntries = sorted(countries)
    countries_codes = get_codes_countries(countries)
    return countries_codes
    

def app_auxes(s):
    items = s.split(',') if ',' in s else [s]
    countries = []
    auxes = []
    for item in items:
        item = item.strip().replace('-',' ')
        if item in lst_country:
            countries.append(item)
        else:
            auxes.append(item)
    auxes = sorted(auxes)
    auxes_codes = get_codes_auxes(auxes)
    return auxes_codes


df = pd.read_csv('dat/data.csv')

dat = df['Cuisine'].apply(app_countries)
df.insert(7, 'Cuisine_countries', dat)

dat2 = df['Cuisine'].apply(app_auxes)
df.insert(8, 'Cuisine_auxes', dat2)

idx = 8

for i in range(4):
    start = i*25
    stop = ((i+1)*25)+1
    name = 'Cuisine_countries_'+str(i)
    dat = df['Cuisine_countries'].apply(lambda x: x[start:stop])
    df.insert(idx, name, dat)
    df[name] = df[name].astype('category')
    idx += 1

df['Cuisine_countries'] = df['Cuisine_countries'].astype('category')
df['Cuisine_auxes'] = df['Cuisine_auxes'].astype('category')

df.to_csv('dat/data_coded.csv', index=False)





