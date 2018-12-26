import pickle
import json
import sys
def main():
    with open('D:/Projects/Dell/python/serviceReasons.pkl','rb') as f:
        serviceReasons=pickle.load(f)
    with open('D:/Projects/Dell/python/regionalServices.pkl','rb') as f:
        regionalServices=pickle.load(f)
    
    print(json.dumps(serviceReasons))
    print(json.dumps(regionalServices))
    sys.stdout.flush()
    
if __name__=='__main__'    :
    main()

