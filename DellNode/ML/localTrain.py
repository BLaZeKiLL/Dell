import numpy as np
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

dataset=pd.read_csv('AssetsDellData.csv')

regressorlist=[]
Predictions=[]
dateOfLaunch={"Inspiron":{1:'1/1/2007',2:'1/1/2010',3:'1/1/2013'},
             "XPS":{1:'1/1/2008',2:'1/1/2011',3:'1/1/2014'},
             "AlienWare":{1:'1/1/2009',2:'1/1/2012',3:'1/1/2015'}}

#----------------------------------
location="USC"
#----------------------------------

#-------------Inspiron-------------
model="Inspiron"
dataset_I=dataset[dataset['Location']==location]
dataset_I=dataset_I[dataset_I['Model']==model].iloc[:,[3,5,6]]
dataset_I.head(5)

sales=np.zeros(12)
quarters=[1,2,3,4,5,6,7,8,9,10,11,12]
for i in dataset_I.iterrows():
    if i[1]['Generation']==1:
        dol=dateOfLaunch[model][1]
    elif i[1]['Generation']==2:
        dol=dateOfLaunch[model][2]
    elif i[1]['Generation']==3:
        dol=dateOfLaunch[model][3]
        
    dop=i[1]['Date Of Purchase']        
    dop=datetime.strptime(dop,'%d-%m-%Y')
    dol=datetime.strptime(dol,'%d/%m/%Y')
    delta=abs((dop-dol).days)//91
    if delta >=11:
        sales[11]+=1
    else:
        sales[delta]+=1
            

sales=[x//len(dateOfLaunch[model]) for x in sales]
print(sales)
print(quarters)



X=np.array(quarters)
X=np.reshape(X,(-1,1))
poly_reg=PolynomialFeatures(degree=3)
X_poly=poly_reg.fit_transform(X)

regressor=LinearRegression()
regressor.fit(X_poly,sales)
y_pred=regressor.predict(X_poly)
Predictions.append(y_pred.tolist())
'''
plt.scatter(X,sales,color='red')
plt.plot(X,regressor.predict(X_poly),color='blue')
plt.title('Sales over different quarters')
plt.xlabel('Quarters')
plt.ylabel('Sales')
plt.show()
'''
regressorlist.append(regressor)

#--------------XPS------------------
model='XPS'
dataset_X=dataset[dataset['Location']==location]
dataset_X=dataset_X[dataset_X['Model']==model].iloc[:,[3,5,6]]
dataset_X.head(5)

sales=np.zeros(12)
quarters=[1,2,3,4,5,6,7,8,9,10,11,12]
for i in dataset_X.iterrows():
    if i[1]['Generation']==1:
        dol=dateOfLaunch[model][1]
    elif i[1]['Generation']==2:
        dol=dateOfLaunch[model][2]
    elif i[1]['Generation']==3:
        dol=dateOfLaunch[model][3]
        
    dop=i[1]['Date Of Purchase']        
    dop=datetime.strptime(dop,'%d-%m-%Y')
    dol=datetime.strptime(dol,'%d/%m/%Y')
    delta=abs((dop-dol).days)//91
    if delta >=11:
        sales[11]+=1
    else:
        sales[delta]+=1
            

sales=[x//len(dateOfLaunch[model]) for x in sales]
print(sales)
print(quarters)


X=np.array(quarters)
X=np.reshape(X,(-1,1))
poly_reg=PolynomialFeatures(degree=3)
X_poly=poly_reg.fit_transform(X)

regressor=LinearRegression()
regressor.fit(X_poly,sales)
y_pred=regressor.predict(X_poly)
Predictions.append(y_pred.tolist())
'''
plt.scatter(X,sales,color='red')
plt.plot(X,regressor.predict(X_poly),color='blue')
plt.title('Sales over different quarters')
plt.xlabel('Quarters')
plt.ylabel('Sales')
plt.show()
'''

regressorlist.append(regressor)


#--------------Alienware----------------------
model='AlienWare'
dataset_A=dataset[dataset['Location']==location]
dataset_A=dataset_A[dataset_A['Model']==model].iloc[:,[3,5,6]]
dataset_A.head(5)

sales=np.zeros(12)
quarters=[1,2,3,4,5,6,7,8,9,10,11,12]
for i in dataset_A.iterrows():
    if i[1]['Generation']==1:
        dol=dateOfLaunch[model][1]
    elif i[1]['Generation']==2:
        dol=dateOfLaunch[model][2]
    elif i[1]['Generation']==3:
        dol=dateOfLaunch[model][3]
        
    dop=i[1]['Date Of Purchase']        
    dop=datetime.strptime(dop,'%d-%m-%Y')
    dol=datetime.strptime(dol,'%d/%m/%Y')
    delta=abs((dop-dol).days)//91
    if delta >=11:
        sales[11]+=1
    else:
        sales[delta]+=1
            

sales=[x//len(dateOfLaunch[model]) for x in sales]
print(sales)
print(quarters)


X=np.array(quarters)
X=np.reshape(X,(-1,1))
poly_reg=PolynomialFeatures(degree=4)
X_poly=poly_reg.fit_transform(X)

regressor=LinearRegression()
regressor.fit(X_poly,sales)
y_pred=regressor.predict(X_poly)
Predictions.append(y_pred.tolist())
'''
plt.scatter(X,sales,color='red')
plt.plot(X,regressor.predict(X_poly),color='blue')
plt.title('Sales over different quarters')
plt.xlabel('Quarters')
plt.ylabel('Sales')
plt.show()
'''
regressorlist.append(regressor)


#--------------------------------------
location='WSE'
#--------------------------------------

#-------------Inspiron-------------
model="Inspiron"
dataset_I=dataset[dataset['Location']==location]
dataset_I=dataset_I[dataset_I['Model']==model].iloc[:,[3,5,6]]
dataset_I.head(5)

sales=np.zeros(12)
quarters=[1,2,3,4,5,6,7,8,9,10,11,12]
for i in dataset_I.iterrows():
    if i[1]['Generation']==1:
        dol=dateOfLaunch[model][1]
    elif i[1]['Generation']==2:
        dol=dateOfLaunch[model][2]
    elif i[1]['Generation']==3:
        dol=dateOfLaunch[model][3]
        
    dop=i[1]['Date Of Purchase']        
    dop=datetime.strptime(dop,'%d-%m-%Y')
    dol=datetime.strptime(dol,'%d/%m/%Y')
    delta=abs((dop-dol).days)//91
    if delta >=11:
        sales[11]+=1
    else:
        sales[delta]+=1
            

sales=[x//len(dateOfLaunch[model]) for x in sales]
print(sales)
print(quarters)


X=np.array(quarters)
X=np.reshape(X,(-1,1))
poly_reg=PolynomialFeatures(degree=4)
X_poly=poly_reg.fit_transform(X)

regressor=LinearRegression()
regressor.fit(X_poly,sales)
y_pred=regressor.predict(X_poly)
Predictions.append(y_pred.tolist())
'''
plt.scatter(X,sales,color='red')
plt.plot(X,regressor.predict(X_poly),color='blue')
plt.title('Sales over different quarters')
plt.xlabel('Quarters')
plt.ylabel('Sales')
plt.show()
'''

regressorlist.append(regressor)


#--------------XPS------------------
model='XPS'
dataset_X=dataset[dataset['Location']==location]
dataset_X=dataset_X[dataset_X['Model']==model].iloc[:,[3,5,6]]
dataset_X.head(5)

sales=np.zeros(12)
quarters=[1,2,3,4,5,6,7,8,9,10,11,12]
for i in dataset_X.iterrows():
    if i[1]['Generation']==1:
        dol=dateOfLaunch[model][1]
    elif i[1]['Generation']==2:
        dol=dateOfLaunch[model][2]
    elif i[1]['Generation']==3:
        dol=dateOfLaunch[model][3]
        
    dop=i[1]['Date Of Purchase']        
    dop=datetime.strptime(dop,'%d-%m-%Y')
    dol=datetime.strptime(dol,'%d/%m/%Y')
    delta=abs((dop-dol).days)//91
    if delta >=11:
        sales[11]+=1
    else:
        sales[delta]+=1
            

sales=[x//len(dateOfLaunch[model]) for x in sales]
print(sales)
print(quarters)


X=np.array(quarters)
X=np.reshape(X,(-1,1))
poly_reg=PolynomialFeatures(degree=4)
X_poly=poly_reg.fit_transform(X)

regressor=LinearRegression()
regressor.fit(X_poly,sales)
y_pred=regressor.predict(X_poly)
Predictions.append(y_pred.tolist())
'''
plt.scatter(X,sales,color='red')
plt.plot(X,regressor.predict(X_poly),color='blue')
plt.title('Sales over different quarters')
plt.xlabel('Quarters')
plt.ylabel('Sales')
plt.show()
'''

regressorlist.append(regressor)

#--------------Alienware----------------------
model='AlienWare'
dataset_A=dataset[dataset['Location']==location]
dataset_A=dataset_A[dataset_A['Model']==model].iloc[:,[3,5,6]]
dataset_A.head(5)

sales=np.zeros(12)
quarters=[1,2,3,4,5,6,7,8,9,10,11,12]
for i in dataset_A.iterrows():
    if i[1]['Generation']==1:
        dol=dateOfLaunch[model][1]
    elif i[1]['Generation']==2:
        dol=dateOfLaunch[model][2]
    elif i[1]['Generation']==3:
        dol=dateOfLaunch[model][3]
        
    dop=i[1]['Date Of Purchase']        
    dop=datetime.strptime(dop,'%d-%m-%Y')
    dol=datetime.strptime(dol,'%d/%m/%Y')
    delta=abs((dop-dol).days)//91
    if delta >=11:
        sales[11]+=1
    else:
        sales[delta]+=1
            

sales=[x//len(dateOfLaunch[model]) for x in sales]
print(sales)
print(quarters)


X=np.array(quarters)
X=np.reshape(X,(-1,1))
poly_reg=PolynomialFeatures(degree=4)
X_poly=poly_reg.fit_transform(X)

regressor=LinearRegression()
regressor.fit(X_poly,sales)
y_pred=regressor.predict(X_poly)
Predictions.append(y_pred.tolist())

'''
plt.scatter(X,sales,color='red')
plt.plot(X,regressor.predict(X_poly),color='blue')
plt.title('Sales over different quarters')
plt.xlabel('Quarters')
plt.ylabel('Sales')
plt.show()
'''

regressorlist.append(regressor)

#--------------------------------------
location='CAJ'
#--------------------------------------

#-------------Inspiron-------------
model="Inspiron"
dataset_I=dataset[dataset['Location']==location]
dataset_I=dataset_I[dataset_I['Model']==model].iloc[:,[3,5,6]]
dataset_I.head(5)

sales=np.zeros(12)
quarters=[1,2,3,4,5,6,7,8,9,10,11,12]
for i in dataset_I.iterrows():
    if i[1]['Generation']==1:
        dol=dateOfLaunch[model][1]
    elif i[1]['Generation']==2:
        dol=dateOfLaunch[model][2]
    elif i[1]['Generation']==3:
        dol=dateOfLaunch[model][3]
        
    dop=i[1]['Date Of Purchase']        
    dop=datetime.strptime(dop,'%d-%m-%Y')
    dol=datetime.strptime(dol,'%d/%m/%Y')
    delta=abs((dop-dol).days)//91
    if delta >=11:
        sales[11]+=1
    else:
        sales[delta]+=1
            

sales=[x//len(dateOfLaunch[model]) for x in sales]
print(sales)
print(quarters)



X=np.array(quarters)
X=np.reshape(X,(-1,1))
poly_reg=PolynomialFeatures(degree=4)
X_poly=poly_reg.fit_transform(X)

regressor=LinearRegression()
regressor.fit(X_poly,sales)
y_pred=regressor.predict(X_poly)
Predictions.append(y_pred.tolist())
'''
plt.scatter(X,sales,color='red')
plt.plot(X,regressor.predict(X_poly),color='blue')
plt.title('Sales over different quarters')
plt.xlabel('Quarters')
plt.ylabel('Sales')
plt.show()
'''

regressorlist.append(regressor)


#--------------XPS------------------
model='XPS'
dataset_X=dataset[dataset['Location']==location]
dataset_X=dataset_X[dataset_X['Model']==model].iloc[:,[3,5,6]]
dataset_X.head(5)

sales=np.zeros(12)
quarters=[1,2,3,4,5,6,7,8,9,10,11,12]
for i in dataset_X.iterrows():
    if i[1]['Generation']==1:
        dol=dateOfLaunch[model][1]
    elif i[1]['Generation']==2:
        dol=dateOfLaunch[model][2]
    elif i[1]['Generation']==3:
        dol=dateOfLaunch[model][3]
        
    dop=i[1]['Date Of Purchase']        
    dop=datetime.strptime(dop,'%d-%m-%Y')
    dol=datetime.strptime(dol,'%d/%m/%Y')
    delta=abs((dop-dol).days)//91
    if delta >=11:
        sales[11]+=1
    else:
        sales[delta]+=1
            

sales=[x//len(dateOfLaunch[model]) for x in sales]
print(sales)
print(quarters)


X=np.array(quarters)
X=np.reshape(X,(-1,1))
poly_reg=PolynomialFeatures(degree=2)
X_poly=poly_reg.fit_transform(X)

regressor=LinearRegression()
regressor.fit(X_poly,sales)
y_pred=regressor.predict(X_poly)
Predictions.append(y_pred.tolist())
'''
plt.scatter(X,sales,color='red')
plt.plot(X,regressor.predict(X_poly),color='blue')
plt.title('Sales over different quarters')
plt.xlabel('Quarters')
plt.ylabel('Sales')
plt.show()
'''
regressorlist.append(regressor)


#--------------Alienware----------------------
model='AlienWare'
dataset_A=dataset[dataset['Location']==location]
dataset_A=dataset_A[dataset_A['Model']==model].iloc[:,[3,5,6]]
dataset_A.head(5)

sales=np.zeros(12)
quarters=[1,2,3,4,5,6,7,8,9,10,11,12]
for i in dataset_A.iterrows():
    if i[1]['Generation']==1:
        dol=dateOfLaunch[model][1]
    elif i[1]['Generation']==2:
        dol=dateOfLaunch[model][2]
    elif i[1]['Generation']==3:
        dol=dateOfLaunch[model][3]
        
    dop=i[1]['Date Of Purchase']        
    dop=datetime.strptime(dop,'%d-%m-%Y')
    dol=datetime.strptime(dol,'%d/%m/%Y')
    delta=abs((dop-dol).days)//91
    if delta >=11:
        sales[11]+=1
    else:
        sales[delta]+=1
            

sales=[x//len(dateOfLaunch[model]) for x in sales]
print(sales)
print(quarters)


X=np.array(quarters)
X=np.reshape(X,(-1,1))
poly_reg=PolynomialFeatures(degree=4)
X_poly=poly_reg.fit_transform(X)

regressor=LinearRegression()
regressor.fit(X_poly,sales)
y_pred=regressor.predict(X_poly)
Predictions.append(y_pred.tolist())
'''
plt.scatter(X,sales,color='red')
plt.plot(X,regressor.predict(X_poly),color='blue')
plt.title('Sales over different quarters')
plt.xlabel('Quarters')
plt.ylabel('Sales')
plt.show()
'''
regressorlist.append(regressor)


#--------------------------------------
location='SEA'
#--------------------------------------

#-------------Inspiron-------------
model="Inspiron"
dataset_I=dataset[dataset['Location']==location]
dataset_I=dataset_I[dataset_I['Model']==model].iloc[:,[3,5,6]]
dataset_I.head(5)

sales=np.zeros(12)
quarters=[1,2,3,4,5,6,7,8,9,10,11,12]
for i in dataset_I.iterrows():
    if i[1]['Generation']==1:
        dol=dateOfLaunch[model][1]
    elif i[1]['Generation']==2:
        dol=dateOfLaunch[model][2]
    elif i[1]['Generation']==3:
        dol=dateOfLaunch[model][3]
        
    dop=i[1]['Date Of Purchase']        
    dop=datetime.strptime(dop,'%d-%m-%Y')
    dol=datetime.strptime(dol,'%d/%m/%Y')
    delta=abs((dop-dol).days)//91
    if delta >=11:
        sales[11]+=1
    else:
        sales[delta]+=1
            

sales=[x//len(dateOfLaunch[model]) for x in sales]
print(sales)
print(quarters)



X=np.array(quarters)
X=np.reshape(X,(-1,1))
poly_reg=PolynomialFeatures(degree=4)
X_poly=poly_reg.fit_transform(X)

regressor=LinearRegression()
regressor.fit(X_poly,sales)
y_pred=regressor.predict(X_poly)
Predictions.append(y_pred.tolist())
'''
plt.scatter(X,sales,color='red')
plt.plot(X,regressor.predict(X_poly),color='blue')
plt.title('Sales over different quarters')
plt.xlabel('Quarters')
plt.ylabel('Sales')
plt.show()
'''

regressorlist.append(regressor)


#--------------XPS------------------
model='XPS'
dataset_X=dataset[dataset['Location']==location]
dataset_X=dataset_X[dataset_X['Model']==model].iloc[:,[3,5,6]]
dataset_X.head(5)

sales=np.zeros(12)
quarters=[1,2,3,4,5,6,7,8,9,10,11,12]
for i in dataset_X.iterrows():
    if i[1]['Generation']==1:
        dol=dateOfLaunch[model][1]
    elif i[1]['Generation']==2:
        dol=dateOfLaunch[model][2]
    elif i[1]['Generation']==3:
        dol=dateOfLaunch[model][3]
        
    dop=i[1]['Date Of Purchase']        
    dop=datetime.strptime(dop,'%d-%m-%Y')
    dol=datetime.strptime(dol,'%d/%m/%Y')
    delta=abs((dop-dol).days)//91
    if delta >=11:
        sales[11]+=1
    else:
        sales[delta]+=1
            

sales=[x//len(dateOfLaunch[model]) for x in sales]
print(sales)
print(quarters)


X=np.array(quarters)
X=np.reshape(X,(-1,1))
poly_reg=PolynomialFeatures(degree=3)
X_poly=poly_reg.fit_transform(X)

regressor=LinearRegression()
regressor.fit(X_poly,sales)
y_pred=regressor.predict(X_poly)
Predictions.append(y_pred.tolist())
'''
plt.scatter(X,sales,color='red')
plt.plot(X,regressor.predict(X_poly),color='blue')
plt.title('Sales over different quarters')
plt.xlabel('Quarters')
plt.ylabel('Sales')
plt.show()
'''
regressorlist.append(regressor)

#--------------Alienware----------------------
model='AlienWare'
dataset_A=dataset[dataset['Location']==location]
dataset_A=dataset_A[dataset_A['Model']==model].iloc[:,[3,5,6]]
dataset_A.head(5)

sales=np.zeros(12)
quarters=[1,2,3,4,5,6,7,8,9,10,11,12]
for i in dataset_A.iterrows():
    if i[1]['Generation']==1:
        dol=dateOfLaunch[model][1]
    elif i[1]['Generation']==2:
        dol=dateOfLaunch[model][2]
    elif i[1]['Generation']==3:
        dol=dateOfLaunch[model][3]
        
    dop=i[1]['Date Of Purchase']        
    dop=datetime.strptime(dop,'%d-%m-%Y')
    dol=datetime.strptime(dol,'%d/%m/%Y')
    delta=abs((dop-dol).days)//91
    if delta >=11:
        sales[11]+=1
    else:
        sales[delta]+=1
            

sales=[x//len(dateOfLaunch[model]) for x in sales]
print(sales)
print(quarters)


X=np.array(quarters)
X=np.reshape(X,(-1,1))
poly_reg=PolynomialFeatures(degree=3)
X_poly=poly_reg.fit_transform(X)

regressor=LinearRegression()
regressor.fit(X_poly,sales)
y_pred=regressor.predict(X_poly)
Predictions.append(y_pred.tolist())
'''
plt.scatter(X,sales,color='red')
plt.plot(X,regressor.predict(X_poly),color='blue')
plt.title('Sales over different quarters')
plt.xlabel('Quarters')
plt.ylabel('Sales')
plt.show()
'''
regressorlist.append(regressor)


#--------------------------------------
location='CA'
#--------------------------------------

#-------------Inspiron-------------
model="Inspiron"
dataset_I=dataset[dataset['Location']==location]
dataset_I=dataset_I[dataset_I['Model']==model].iloc[:,[3,5,6]]
dataset_I.head(5)

sales=np.zeros(12)
quarters=[1,2,3,4,5,6,7,8,9,10,11,12]
for i in dataset_I.iterrows():
    if i[1]['Generation']==1:
        dol=dateOfLaunch[model][1]
    elif i[1]['Generation']==2:
        dol=dateOfLaunch[model][2]
    elif i[1]['Generation']==3:
        dol=dateOfLaunch[model][3]
        
    dop=i[1]['Date Of Purchase']        
    dop=datetime.strptime(dop,'%d-%m-%Y')
    dol=datetime.strptime(dol,'%d/%m/%Y')
    delta=abs((dop-dol).days)//91
    if delta >=11:
        sales[11]+=1
    else:
        sales[delta]+=1
            

sales=[x//len(dateOfLaunch[model]) for x in sales]
print(sales)
print(quarters)



X=np.array(quarters)
X=np.reshape(X,(-1,1))
poly_reg=PolynomialFeatures(degree=3)
X_poly=poly_reg.fit_transform(X)

regressor=LinearRegression()
regressor.fit(X_poly,sales)
y_pred=regressor.predict(X_poly)
Predictions.append(y_pred.tolist())
'''
plt.scatter(X,sales,color='red')
plt.plot(X,regressor.predict(X_poly),color='blue')
plt.title('Sales over different quarters')
plt.xlabel('Quarters')
plt.ylabel('Sales')
plt.show()
'''
regressorlist.append(regressor)

#--------------XPS------------------
model='XPS'
dataset_X=dataset[dataset['Location']==location]
dataset_X=dataset_X[dataset_X['Model']==model].iloc[:,[3,5,6]]
dataset_X.head(5)

sales=np.zeros(12)
quarters=[1,2,3,4,5,6,7,8,9,10,11,12]
for i in dataset_X.iterrows():
    if i[1]['Generation']==1:
        dol=dateOfLaunch[model][1]
    elif i[1]['Generation']==2:
        dol=dateOfLaunch[model][2]
    elif i[1]['Generation']==3:
        dol=dateOfLaunch[model][3]
        
    dop=i[1]['Date Of Purchase']        
    dop=datetime.strptime(dop,'%d-%m-%Y')
    dol=datetime.strptime(dol,'%d/%m/%Y')
    delta=abs((dop-dol).days)//91
    if delta >=11:
        sales[11]+=1
    else:
        sales[delta]+=1
            

sales=[x//len(dateOfLaunch[model]) for x in sales]
print(sales)
print(quarters)


X=np.array(quarters)
X=np.reshape(X,(-1,1))
poly_reg=PolynomialFeatures(degree=3)
X_poly=poly_reg.fit_transform(X)

regressor=LinearRegression()
regressor.fit(X_poly,sales)
y_pred=regressor.predict(X_poly)
Predictions.append(y_pred.tolist())
'''
plt.scatter(X,sales,color='red')
plt.plot(X,regressor.predict(X_poly),color='blue')
plt.title('Sales over different quarters')
plt.xlabel('Quarters')
plt.ylabel('Sales')
plt.show()
'''
regressorlist.append(regressor)

#--------------Alienware----------------------
model='AlienWare'
dataset_A=dataset[dataset['Location']==location]
dataset_A=dataset_A[dataset_A['Model']==model].iloc[:,[3,5,6]]
dataset_A.head(5)

sales=np.zeros(12)
quarters=[1,2,3,4,5,6,7,8,9,10,11,12]
for i in dataset_A.iterrows():
    if i[1]['Generation']==1:
        dol=dateOfLaunch[model][1]
    elif i[1]['Generation']==2:
        dol=dateOfLaunch[model][2]
    elif i[1]['Generation']==3:
        dol=dateOfLaunch[model][3]
        
    dop=i[1]['Date Of Purchase']        
    dop=datetime.strptime(dop,'%d-%m-%Y')
    dol=datetime.strptime(dol,'%d/%m/%Y')
    delta=abs((dop-dol).days)//91
    if delta >=11:
        sales[11]+=1
    else:
        sales[delta]+=1
            

sales=[x//len(dateOfLaunch[model]) for x in sales]
print(sales)
print(quarters)


X=np.array(quarters)
X=np.reshape(X,(-1,1))
poly_reg=PolynomialFeatures(degree=4)
X_poly=poly_reg.fit_transform(X)

regressor=LinearRegression()
regressor.fit(X_poly,sales)
y_pred=regressor.predict(X_poly)
Predictions.append(y_pred.tolist())
'''
plt.scatter(X,sales,color='red')
plt.plot(X,regressor.predict(X_poly),color='blue')
plt.title('Sales over different quarters')
plt.xlabel('Quarters')
plt.ylabel('Sales')
plt.show()
'''
regressorlist.append(regressor)

regressorDictionary={0:{'model':regressorlist[0],
                        'degree':3},
                    1:{'model':regressorlist[1],
                        'degree':3},
                    2:{'model':regressorlist[2],
                        'degree':4},
                    3:{'model':regressorlist[3],
                        'degree':4},
                    4:{'model':regressorlist[4],
                        'degree':4},
                    5:{'model':regressorlist[5],
                        'degree':4},
                    6:{'model':regressorlist[6],
                        'degree':4},
                    7:{'model':regressorlist[7],
                        'degree':2},
                    8:{'model':regressorlist[8],
                        'degree':4},
                    9:{'model':regressorlist[9],
                        'degree':4},
                    10:{'model':regressorlist[10],
                        'degree':3},
                    11:{'model':regressorlist[11],
                        'degree':3},
                    12:{'model':regressorlist[12],
                        'degree':3},
                    13:{'model':regressorlist[13],
                        'degree':3},
                    14:{'model':regressorlist[14],
                        'degree':4}}
import pickle
with open('localModels.pkl','wb') as f:
    pickle.dump(regressorDictionary,f)
with open('localPredictions.pkl','wb') as f:
    pickle.dump(Predictions,f)
