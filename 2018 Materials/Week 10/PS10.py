import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn import neighbors, datasets
from sklearn.metrics import confusion_matrix

def get_metrics(actual_targets, predicted_targets, labels):
    con_matrix = confusion_matrix(actual_targets, predicted_targets,labels)
    total_length = len(actual_targets)
    accuracy = round((con_matrix[0][0] + con_matrix[1][1])/len(actual_targets),3)
    sensitivity = round(con_matrix[1][1]/(con_matrix[1][0] + con_matrix[1][1]),3)
    false_positive = round(con_matrix[0][1]/sum(con_matrix[0]),3)
    output = {'confusion matrix': con_matrix, 'total records': total_length,'accuracy': accuracy, 'sensitivity':sensitivity, 'false positive rate': false_positive} 
    return output

#C1a
def display_box_plots(data, feature_name,title_name = 'default'):
    plt.boxplot(data)
    plt.title(title_name)
    plt.xticks([i+1 for i in range(len(feature_name))], [feature_name[i] for i in range(len(feature_name))]) 
    #plots the x axis using a list of positions and feature strings
    plt.show()

bunchobject = datasets.load_breast_cancer()
feature_range = [0,1]
data_subset = bunchobject.data[:,feature_range]
feature_names_subset = bunchobject.feature_names[feature_range]

# display_box_plots(data_subset,feature_names_subset)


#C1b
def display_histogram(data, nbins, feature_name, title = 'default'):
    plt.hist(data, bins = nbins)
    plt.title(title)
    plt.xlabel(feature_name)
    plt.show()

#test script 1b
feature_col = 0
one_col_data = data_subset[:,feature_col]
feature_name_selected = bunchobject.feature_names[feature_col]
number_of_bins = 50
#please specify a suitable value
title_string = ' '
#please provide a suitable title string

# display_histogram(one_col_data, number_of_bins,feature_name_selected, title_string)

#C1c
def display_scatter(x,y, xlabel='x', ylabel='y',title_name ='default'): 
    plt.scatter(x,y,)
    plt.xlabel (xlabel)
    plt.ylabel (ylabel)
    plt.title (title_name)
    plt.show()

#test script 1c
x_index = 0
y_index = 3
x = bunchobject.data[:,x_index]
y = bunchobject.data[:,y_index]
x_label = bunchobject.feature_names[x_index]
y_label = bunchobject.feature_names[y_index]

# display_scatter(x,y,x_label,y_label)


#C1d
def display_bar_chart(positions, counts, names, title_name='default'):
    plt.bar(positions, counts)
    plt.xticks([i for i in range(len(names))], names)
    plt.title (title_name)
    plt.show()

#test script 1d
unique, counts = np.unique(bunchobject.target, return_counts = True)
# display_bar_chart(unique, counts, bunchobject.target_names)

#C2
def five_number_summary(x):
    row, cols = x.shape
    return [{'maximum':np.max(x[:,i]), 
    'minimum':np.min(x[:,i]), 
    'median':np.median(x[:,i]), 
    'first quartile':np.percentile(x[:,i], 25), 
    'third quartile':np.percentile(x[:,i], 75)} for i in range(cols)]

#test script 2
first_column = bunchobject.data[:,np.newaxis,1]
# print( five_number_summary(first_column))
# print('next test========================================')
col_no = [0,1,2]
some_columns = bunchobject.data[:,col_no]
# print( five_number_summary(some_columns))

#C3
def normalize_minmax(data):
    size = data.shape
    # print('size is ', size)
    if len(size) == 1:
        columns = 1
    else:
        columns = size[1]
    for i in range(columns):
        maxx = np.max(data[:,i])
        minn = np.min(data[:,i])
        denominator = maxx - minn
        data[:,i] = (data[:,i] - minn)/denominator
    return data

#test script 3
first_column = bunchobject.data[:,np.newaxis,1]
first_column_norm = normalize_minmax(first_column)
# print(five_number_summary(first_column_norm))


#C4
from sklearn.model_selection import train_test_split 

def knn_classifier(bobj, feature_list, size, seed , k): 
    data = bobj.data[:,feature_list]
    target = bobj.target

    data = normalize_minmax(data)

    data_train, data_test, target_train, target_test = train_test_split(data, target, test_size = size, random_state = seed)
    clf = neighbors.KNeighborsClassifier(k)
    clf.fit(data_train, target_train)

    predicted_target = clf.predict(data_test)

    results = get_metrics(target_test, predicted_target, [0,1])
    return results
  
#C5
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score

def linear_regression(bobj, x_ind, y_ind, size, seed):
    data = bobj.data
    x = data[:,np.newaxis, x_ind]
    y = data[:,np.newaxis, y_ind]
    
    x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=size, random_state=seed)
    regr = linear_model.LinearRegression()
    regr.fit(x_train, y_train)
    y_pred = regr.predict(x_test)
    merror=mean_squared_error(y_test,y_pred)
    r2=r2_score(y_test,y_pred)
    
    results = {'coefficients' : regr.coef_, 'intercept' : regr.intercept_, 'mean squared error' : merror, 'r2 score': r2}
    
    return x_train,y_train,x_test,y_pred,results

#test script 5
# x_train, y_train, x_test, y_pred, results =linear_regression(bunchobject,0,3,0.4,2752)
# print(results)

#C6
def multiple_linear_regression(bobj, x_index, y_index, order, size, seed):
    data=bobj.data
    x=data[:,np.newaxis,x_index]
    y=data[:,np.newaxis,y_index]
    c=x
    for i in range(2,order+1):
        c=np.concatenate((c,x**i),axis=1)
    poly=PolynomialFeatures(order,include_bias=False)
    c=poly.fit_transform(x)
    c_train,c_test,y_train,y_test=train_test_split(c,y,test_size=size,random_state=seed)
    regr=linear_model.LinearRegression()
    regr.fit(c_train,y_train)
    y_pred=regr.predict(c_test)
    merror=mean_squared_error(y_test,y_pred)
    r2=r2_score(y_test,y_pred)
    
    results = {'coefficients' : regr.coef_, 'intercept' : regr.intercept_, 'mean squared error' : merror, 'r2 score': r2}
    
    return c_train[:,0],y_train,c_test[:,0],y_pred,results



#C7
def knn_classifier_full(bunchobject, feature_list, size, seed): 
    data1 = bunchobject.data[:,feature_list]
    target = bunchobject.target

    data = normalize_minmax(data1)

    data_train, data_part2, target_train, target_part2 = train_test_split(data, target,test_size = 0.4, random_state = seed)
    data_validation, data_test, target_validation, target_test = train_test_split(data_part2, target_part2, test_size = 0.5, random_state = seed)

    results_k = {}

    for k in range(1,20):
        clf = neighbors.KNeighborsClassifier(k)
        clf.fit(data_train, target_train)
        predicted_targets = clf.predict(data_validation)
        results = get_metrics(target_validation, predicted_targets, [0,1])
        results_k[k] = results
    return data_train, data_test, target_train, target_test, results_k