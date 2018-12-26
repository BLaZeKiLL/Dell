import sys
import pickle
import json

def main():
    args=sys.argv[1:]
    with open('D:/Projects/Hackathon/Dell/python/localPredictions.pkl','rb') as f:
        predictions=pickle.load(f)
    
    if args[0]=="USC":
        print(json.dumps(predictions[0:3]))
    elif args[0]=="WSE":
        print(json.dumps(predictions[3:6]))
    elif args[0]=="CAJ":
        print(json.dumps(predictions[6:9]))
    elif args[0]=="SEA":
        print(json.dumps(predictions[9:12]))
    elif args[0]=="CA":
        print(json.dumps(predictions[12:15]))
    
    sys.stdout.flush()
    

if __name__=="__main__":
    main()
        