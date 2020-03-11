
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('master.csv')
X = dataset.drop(['suicides/100k pop','suicides_no','country-year'],axis =1)
y = dataset['suicides/100k pop']


#corellation checking
import seaborn as sns
corr = X.corr()
sns.heatmap(corr, xticklabels = corr.columns.values, yticklabels= corr.columns.values)
print(len(X))

plt.figure(figsize= (10,10))
plt.scatter(X['gdp_per_capita ($)'], X[' gdp_for_year ($) '],c='red')

plt.scatter(X['population'], X[' gdp_for_year ($) '],c='green')

plt.scatter(X['gdp_per_capita ($)'], X['HDI for year'],c='yellow')

plt.scatter( X[' gdp_for_year ($) '], y,c='blue')
plt.show()

# Data preprocessing  pyuic5 -x prediction_GUI.ui -o prediction_gui.py

X[' gdp_for_year ($) '] = X[' gdp_for_year ($) '].str.replace(',','').astype(float)
numeric_features = ['year','HDI for year',' gdp_for_year ($) ','population','gdp_per_capita ($)']

categorical_features = ['country','sex','age','generation']

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import Imputer, OneHotEncoder, StandardScaler

numeric_transformer = Pipeline(steps =[
        ('imputer',Imputer(missing_values = 'NaN', strategy = 'mean')),
        ('scaler', StandardScaler())
        ])

categorical_transformer = Pipeline(steps =[
        ('onehot', OneHotEncoder())
        ])

preprocessor = ColumnTransformer(
        transformers = [
                ('num',numeric_transformer, numeric_features),
                ('cat', categorical_transformer, categorical_features)
                ])

clf = Pipeline(steps = [('preprocessor',preprocessor)])
X = clf.fit_transform(X)

#splitting the dataset

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
print(X_test)
#linear regression

from sklearn.linear_model import LinearRegression
regressor = LinearRegression(fit_intercept=False)
regressor.fit(X_train, y_train)


y_pred_test = regressor.predict(X_test)
y_pred_train = regressor.predict(X_train)

# performance evaluation
        
from sklearn.metrics import mean_squared_error
rms_test = np.sqrt(mean_squared_error(y_test, y_pred_test))
rms_train = np.sqrt(mean_squared_error(y_train, y_pred_train))

print('RMS for train data:' + rms_train.astype(str))
print('RMS for test data:' + rms_test.astype(str))

#SVM

from sklearn.svm import SVR
regressor = SVR(kernel = 'rbf')
regressor.fit(X_train, y_train)
y_pred_test = regressor.predict(X_test)
y_pred_train = regressor.predict(X_train)


#decision TRee 

from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor()
regressor.fit(X_train, y_train)
y_pred_test = regressor.predict(X_test)
y_pred_train = regressor.predict(X_train)


#Random Forest 

from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators=30)
regressor.fit(X_train, y_train)
y_pred_test = regressor.predict(X_test)
y_pred_train = regressor.predict(X_train)


