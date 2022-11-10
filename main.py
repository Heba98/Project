import math
import pandas as pd
from sklearn.model_selection import train_test_split


dataset = pd.read_csv(r'C:\Users\hebam\Desktop\cancerdata.csv')
df = pd.DataFrame(data=dataset) # read rows and columns

X = dataset.iloc[:,:-1]

y = dataset.iloc[:,-1]
X_train,X_test,y_train,y_test = train_test_split(X,y, test_size=0.2, random_state=0)

with open('data.txt', 'w') as f:
    print(dataset, file=f)

with open('X_train.txt', 'w') as f:
    print(X_train, file=f)

with open('X_test.txt', 'w') as f:
    print(X_test, file=f)

with open('y_train.txt', 'w') as f:
    print(y_train, file=f)

with open('y_test.txt', 'w') as f:
    print(y_test, file=f)


    X_t = pd.DataFrame(data=X_train)
    Y_t=pd.DataFrame(data=X_test)
    index=0

    smoking = X_t.iloc[:, 2]
    yellow_fingers = X_t.iloc[:, 3]
    anxiety = X_t.iloc[:, 4]
    deep_pressure = X_t.iloc[:, 5]
    chronic_diase = X_t.iloc[:, 6]
    fatigue = X_t.iloc[:, 7]
    allergy = X_t.iloc[:, 8]
    wheezing = X_t.iloc[:, 9]
    alcohol_consumption = X_t.iloc[:, 10]
    coughing = X_t.iloc[:, 11]
    shortness_of_breath = X_t.iloc[:, 12]
    swallow_difficulty = X_t.iloc[:, 13]
    chest_pain = X_t.iloc[:, 14]

#print(df.iloc[0,0:15])
# #print(df.loc[2,3])
variables= dataset.columns[0:15] # to get all variables
# Get entropy
def calc_entropy(p_value, n_value):
   tot= p_value+ n_value
   s=-(p_value/tot)* math.log(p_value/tot, 2) - (n_value/tot)*math.log(n_value/tot, 2)
   print(s)

def get_Yes():
    yes_num = 0
    for x in y_train:
       if x == "YES":
           yes_num = yes_num+1
    return yes_num


def get_No():
    no_num = len(y_train)- get_Yes()
    return no_num

def get_variable(var_list,y_train):
    var_1=0
    var_yes=0
    for x in range(5):
        if var_list[x]==1:
            print("ll")
            var_1=var_1+1
           # if y_train[x] == "YES":
            #    var_yes=var_yes+1
    print(var_yes)
    print(var_1)


   # no_num=len(y_train)- yes_num
calc_entropy(get_Yes(),get_No())
print(smoking[0])
get_variable(chest_pain,y_train)

















