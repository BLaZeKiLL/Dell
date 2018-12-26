# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 00:29:46 2018

@author: Ayush
"""

# Import the libraries
import sys
import os
import pickle

# Function to return JSON String containing
# global level distribution sales data of each laptop model's sold percentage
def getGlobalLevelSalesData_json() :
    file_name = os.getcwd() + "\\GlobalLevel_json.pickle"
    with open(file_name, "rb") as pickle_file :
        sales_json = pickle.load(pickle_file)
    
    return sales_json

# Function to return JSON string containing
# region wise sales data of each laptop model's sold percentage
def getRegionWiseSalesData_json() :
    file_name = os.getcwd() + "\\RegionWise_json.pickle"
    with open(file_name, "rb") as pickle_file :
        sales_json = pickle.load(pickle_file)
    
    return sales_json

# Function to return JSON string containing
# generation wise sales data
def getRegion_generationWiseSalesData_json() :
    file_name = os.getcwd() + "\\RegionGenerationWise_json.pickle"
    with open(file_name, "rb") as pickle_file :
        sales_json = pickle.load(pickle_file)
    
    return sales_json

# Function to return JSON string containing
# generation sales data at Global level
def getGlobal_generationWiseSalesData_json() :
    file_name = os.getcwd() + "\\GlobalGenerationWise_json.pickle"
    with open(file_name, "rb") as pickle_file :
        sales_json = pickle.load(pickle_file)
    
    return sales_json

# Function to return JSON string containing
# customer occupation wise sales data region wise
def getRegion_occupationWiseSalesData_json() :
    file_name = os.getcwd() + "\\RegionOccupationWise_json.pickle"
    with open(file_name, "rb") as pickle_file :
        sales_json = pickle.load(pickle_file)
    
    return sales_json

# Function to return JSON string containing
# customer occupation wise sales data globally
def getGlobal_occupationWiseSalesData_json() :
    file_name = os.getcwd() + "\\GlobalOccupationWise_json.pickle"
    with open(file_name, "rb") as pickle_file :
        sales_json = pickle.load(pickle_file)
    
    return sales_json

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
        elif (perform_task == "generation") :
            sales_json = getRegion_generationWiseSalesData_json()
        elif (perform_task == "global_generation") :
            sales_json = getGlobal_generationWiseSalesData_json()
        elif (perform_task == "occupation") :
            sales_json = getRegion_occupationWiseSalesData_json()
        elif (perform_task == "global_occupation") :
            sales_json = getGlobal_occupationWiseSalesData_json()
        else :
            print("Invalid Arguement!")
            
        print(sales_json)

if __name__ == "__main__" :
    main()