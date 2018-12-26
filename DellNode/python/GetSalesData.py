# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 17:04:30 2018

@author: Ayush
"""
# Import the libraries
import sys
import pickle

# Function to get dictionary containing
# global level distribution sales data of each laptop model's sold percentage
def getGlobalLevelSalesData_dict() :
    file_name = "D:/Projects/Hackathon/Dell/python/GlobalLevel_dict.pickle"
    with open(file_name, "rb") as pickle_file :
        sales_dict = pickle.load(pickle_file)
    
    return sales_dict

# Function to return JSON String containing
# global level distribution sales data of each laptop model's sold percentage
def getGlobalLevelSalesData_json() :
    file_name = "D:/Projects/Hackathon/Dell/python/GlobalLevel_json.pickle"
    with open(file_name, "rb") as pickle_file :
        sales_json = pickle.load(pickle_file)
    
    return sales_json

# Function to get dictionary containing 
# region wise sales data of each laptop model's sold percentage
def getRegionWiseSalesData_dict() :
    file_name = "D:/Projects/Hackathon/Dell/python/RegionWise_dict.pickle"
    with open(file_name, "rb") as pickle_file :
        sales_dict = pickle.load(pickle_file)
        
    return sales_dict

# Function to return json string containing
# region wise sales data of each laptop model's sold percentage
def getRegionWiseSalesData_json() :
    file_name = "D:/Projects/Hackathon/Dell/python/RegionWise_json.pickle"
    with open(file_name, "rb") as pickle_file :
        sales_dict = pickle.load(pickle_file)
    
    return sales_dict

# Function to run the script
def main() :
    arguments_valid = False
    
    # Get the argument values from the command line
    args = sys.argv[1:]
    
    if len(args) > 0 :
        arguments_valid = True
    else :
        print("Too Few Arguements")
    
    if arguments_valid :
        perform_task = args[0]
        
        if (perform_task == "global") :
            sales_json = getGlobalLevelSalesData_json()
        elif (perform_task == "region") :
            sales_json = getRegionWiseSalesData_json()
        else :
            print("Invalid Arguement!")
            
        print(sales_json)

if __name__ == "__main__" :
    main()