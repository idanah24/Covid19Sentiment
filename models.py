from keras import Sequential
from keras.layers import Dense

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

import pandas as pd
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_colwidth', 40)

data = pd.read_csv('ready_data.csv', index_col=[0])



data['location'] = LabelEncoder().fit(data['location'].unique()).transform(data['location'])


x = data[['location', 'cases_by_pop', 'deaths_by_pop', 'inf_neg_avg', 'inf_neu_avg', 'inf_pos_avg', 'inf_amount']].to_numpy()
y = data[['pop_neg_avg', 'pop_neu_avg', 'pop_pos_avg']].to_numpy()



X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.1)


def neural_network_model():

    model = Sequential()
    model.add(Dense(50, input_dim=x.shape[1], activation='relu'))
    model.add(Dense(25, activation='relu'))
    model.add(Dense(12, activation='relu'))
    model.add(Dense(3, activation='softmax'))

    metrics_names = ['mse', 'mae', 'mape', 'cosine']
    model.compile(loss='mse', optimizer='adam', metrics=metrics_names)
    model.fit(X_train, Y_train, validation_data=(X_test, Y_test), epochs=1000, batch_size=1, verbose=2)

    metrics = model.evaluate(X_test, Y_test)
    metrics.pop(0)


    return dict(zip(metrics_names, metrics))


nn = neural_network_model()

from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.multioutput import MultiOutputRegressor
from sklearn.svm import LinearSVR

lr = LinearRegression()
lr.fit(x, y)


knn = KNeighborsRegressor()
knn.fit(x, y)


rfr = RandomForestRegressor()
rfr.fit(x, y)




lsvr = LinearSVR()
mor = MultiOutputRegressor(lsvr)
mor.fit(x, y)



models = [('Linear Regression', lr), ('K-Neighbors Regressor', knn), ('Random Forest Regressor', rfr), ('MultiOutput Regressor', mor)]

from numpy import absolute
from numpy import mean
from numpy import std
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RepeatedKFold

cv = RepeatedKFold(n_splits=10, n_repeats=3, random_state=1)

scores = dict()

for model in models:
    mae_n_scores = cross_val_score(model[1], x, y, scoring='neg_mean_absolute_error', cv=cv, n_jobs=-1, error_score='raise')
    # summarize performance
    mae_n_scores = absolute(mae_n_scores)

    mse_n_scores = cross_val_score(model[1], x, y, scoring='neg_mean_squared_error', cv=cv, n_jobs=-1,
                                   error_score='raise')
    # summarize performance
    mse_n_scores = absolute(mse_n_scores)

    scores[model[0]] = {'MAE': (round(mean(mae_n_scores), 3), round(std(mae_n_scores), 3)),
                        'MSE': (round(mean(mse_n_scores), 3), round(std(mse_n_scores), 3))
                        }









