import pickle
from sklearn.preprocessing import PolynomialFeatures
import sys
import json

def main(location,quarter):
    models=["Inspiron","XPS","AlienWare"]
    locationsIndex={"USC":0,"WSE":3,"CAJ":6,"SEA":9,"CA":12}
    
    with open("D:/Projects/Dell/python/localModels.pkl",'rb') as f:
        predictionModels=pickle.load(f)
    with open("D:/Projects/Dell/python/accessoryDict.pickle",'rb') as f:
        accessoryDict=pickle.load(f)
   
    index=locationsIndex[location]
    prediction=[]
    for i in range(len(models)):
        poly_reg=PolynomialFeatures(degree=predictionModels[index+i]['degree'])
        temp=predictionModels[index+i]['model'].predict(poly_reg.fit_transform([[quarter]]))
        if temp<0:
            temp=0
        else:
            temp=temp.tolist()[0]
        prediction.append(temp)
       
    print(json.dumps(prediction))
    
    Sum=sum(prediction)
        
    for i in range(len(prediction)):
        prediction[i]/=Sum
    x=prediction.index(max(prediction))
    acc=accessoryDict[location][models[x]]
    print(json.dumps(acc))
    sys.stdout.flush()
        
if __name__=="__main__":
    args=sys.argv[1:]
    main(args[0],int(args[1]))
            
