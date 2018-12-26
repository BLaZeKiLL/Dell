# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 00:08:39 2018

@author: Ayush
"""

# Import the libraries
import pickle

# Function to get dictionary containing
# global level distribution sales data of each laptop model's sold percentage
def getGlobalLevelSalesData_dict() :
    file_name = "GlobalLevel_dict.pickle"
    with open(file_name, "rb") as pickle_file :
        sales_dict = pickle.load(pickle_file)
    
    return sales_dict

# Function to get dictionary containing 
# region wise sales data of each laptop model's sold percentage
def getRegionWiseSalesData_dict() :
    file_name = "RegionWise_dict.pickle"
    with open(file_name, "rb") as pickle_file :
        sales_dict = pickle.load(pickle_file)
        
    return sales_dict