import pickle
from sklearn.preprocessing import PolynomialFeatures
import sys
import json

def main(quarter):

    with open('D:/Projects/Dell/python/globalModels.pkl','rb') as f:
        newlist=pickle.load(f)
        predictions=[]
        for i in range(3):
            poly_reg=PolynomialFeatures(degree=newlist[i]['degree'])
            prediction=newlist[i]['model'].predict(poly_reg.fit_transform([[quarter]])).tolist()[0]
            if prediction<0:
                predictions.append(0)
            else:
                predictions.append(prediction)
        
    print(json.dumps(predictions))
    sys.stdout.flush()
        
if __name__=="__main__":
    args=sys.argv[1:]
    main(int(args[0]))
            
