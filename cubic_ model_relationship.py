mydf_final = pd.read_csv('final_data_nums.csv')
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

# countdata = mydf_final.copy()
# countdata['playtime'] = traindata['playtime']
mydf_final = mydf_final.fillna(0).head(50)
# print(mydf_final.shape)
X = mydf_final.values
y = results['score'].head(50).values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30)

print_X_test = X
print_y_test = y

from sklearn.preprocessing import PolynomialFeatures
poly_data = PolynomialFeatures(3, include_bias=False).fit_transform(X_train)
poly_data_test = PolynomialFeatures(3, include_bias=False).fit_transform(X_test)
# print(poly_data[0:3])

cubic_model = LinearRegression()
cubic_model.fit(X=poly_data, y=y_train)

test_predict = cubic_model.predict(poly_data_test)

from sklearn.metrics import mean_absolute_error
print(test_predict)

print("MSE: ", mean_squared_error(y_test, test_predict), 
        "r^2: ", r2_score(y_test, test_predict), "RMSE: ", mean_squared_error(y_test, test_predict, squared=False), 'MAE: ',mean_absolute_error(y_test, test_predict))

print(print_X_test[13], print_y_test[13], test_predict[13])
