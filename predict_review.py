import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestRegressor

df = pd.read_csv("dat/data_coded_cuisine.csv")
print(df.columns)
df = df.dropna()

print(df.isnull().sum())

for i in range(4):
    name = 'Cuisine_countries_'+str(i)
    df[name] = df[name].astype('category')
    
df['Cuisine_countries'] = df['Cuisine_countries'].astype('category')
df['Cuisine_auxes'] = df['Cuisine_auxes'].astype('category')

X = df.drop(columns=['Title','Cuisine', 'Reviews'])
X = X.drop(columns=['Cuisine_countries'])
X.dropna(inplace=True)
y= df['Reviews']

print('y.isnull()',y.isnull().sum())

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.25, random_state=42)

# Create RandomForest Regression model
forest_reg = RandomForestRegressor(n_estimators=25, random_state=5)
forest_reg.fit(X_train, y_train)
y_pred = forest_reg.predict(X_test)
rmse= np.sqrt(mean_squared_error(y_test, y_pred))
print('rmse: {:.4}'.format(rmse))

print('\npredict review for Italian?')
df_italian = df[df['Cuisine'].str.contains('Italian')]
X_italian = df_italian.drop(columns=['Title','Cuisine', 'Reviews'])
X_italian = X_italian.drop(columns=['Cuisine_countries'])
# X_italian.dropna(inplace=True)
y_pred = forest_reg.predict(X_italian)
y_actual = df_italian['Reviews']
rmse= np.sqrt(mean_squared_error(y_actual, y_pred))

print('rmse: {:.4}'.format(rmse))
X = df_italian[['restaurant_id','Title','Cuisine']]
X.reset_index()
y = pd.DataFrame(y_pred, columns=['Reviews'])
y.reset_index()
df = X.merge(y, left_index=True, right_index=True)
print(df.head(5))

