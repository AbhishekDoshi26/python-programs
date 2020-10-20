>>> from sklearn.cross_validation import train_test_split
>>> from sklearn.tree import DecisionTreeClassifier
>>> from sklearn.metrics import accuracy_score
>>> from sklearn.metrics import classification_report
>>> def importdata(): #Importing data
 balance_data=pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-'+
'databases/balance-scale/balance-scale.data',
   sep= ',', header = None)
          print(len(balance_data))
          print(balance_data.shape)
          print(balance_data.head())
          return balance_data
>>> def splitdataset(balance_data): #Splitting data
          x=balance_data.values[:,1:5]
          y=balance_data.values[:,0]
          x_train,x_test,y_train,y_test=train_test_split(
              x,y,test_size=0.3,random_state=100)
          return x,y,x_train,x_test,y_train,y_test
>>> def train_using_gini(x_train,x_test,y_train): #Training with giniIndex
          clf_gini = DecisionTreeClassifier(criterion = "gini",
          random_state = 100,max_depth=3, min_samples_leaf=5)
          clf_gini.fit(x_train,y_train)
          return clf_gini
>>> def train_using_entropy(x_train,x_test,y_train): #Training with entropy
          clf_entropy=DecisionTreeClassifier(
          criterion = "entropy", random_state = 100,
          max_depth = 3, min_samples_leaf = 5)
          clf_entropy.fit(x_train,y_train)
          return clf_entropy
>>> def prediction(x_test,clf_object): #Making predictions
          y_pred=clf_object.predict(x_test)
          print(f"Predicted values: {y_pred}")
          return y_pred
>>> def cal_accuracy(y_test,y_pred): #Calculating accuracy
          print(confusion_matrix(y_test,y_pred))
          print(accuracy_score(y_test,y_pred)*100)
          print(classification_report(y_test,y_pred))
>>> data=importdata()
