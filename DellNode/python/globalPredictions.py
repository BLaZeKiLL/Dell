import sys
import pickle
import json

def main():
    with open('D:/Projects/Hackathon/Dell/python/globalPredictions.pkl','rb') as f:
        predictions=pickle.load(f)
    
    print(json.dumps(predictions))
    sys.stdout.flush()
    

if __name__=="__main__":
    main()
        