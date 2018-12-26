# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 23:12:34 2018

@author: Ayush
"""

# Importing the libraries
import pickle
import json
import pandas as pd

# Tuple which stores the regions
#regions = ("ANZ", "CAF", "EE", "SEA", "USC")
regions = ("CA", "CAJ", "SEA", "USC", "WSE")

# Tuple which stores the laptop models
#laptop_models = ("Alienware", "Inspiron", "XPS")
laptop_models = ("AlienWare", "Inspiron", "XPS")

# Function to get dictionary containing
# global level distribution sales data of each laptop model's sold percentage
def getGlobalLevelSalesData_dict(csv_file) :
    sales_dict = dict()
    
    # Read the csv file containing the dataset
    dataset = pd.read_csv(csv_file)
    
    for laptop_model in laptop_models :
        # Create a list to store the sold percentage of selected laptop at each region
        laptop_sales_list = list()
        
        # Extract the selected laptop informartion sold globally
        selected_laptop_global_data = extract_given_model_globally(dataset, laptop_model)
        
        # Compute the total units sold of selected laptop model at global level
        total_units_sold = selected_laptop_global_data.shape[0]
        
        for region in regions :
            # Extract the laptop model information for the selected region
            laptop_region_data = extract_given_model_for_location(dataset, region, laptop_model)
            
            # Compute the number of units sold of the laptop model for the selected region
            units_sold = laptop_region_data.shape[0]
            
            # Compute the unit sold in percentage
            percent_sold = (units_sold / total_units_sold) * 100
            
            # Putting the obtained percentage into the list
            laptop_sales_list.append(percent_sold)
        
        # Putting the list of laptop sales glboal distribution percentage into the dictionary
        sales_dict[laptop_model] = laptop_sales_list
    
    return sales_dict

# Function to return JSON String containing
# global level distribution sales data of each laptop model's sold percentage
def getGlobalLevelSalesData_json(csv_file) :
    # Get the dictionary containing global level distribution sales data of each laptop model's sold percentage
    sales_dict = getGlobalLevelSalesData_dict(csv_file)
    
    # Converting the dictionary to JSON
    sales_json = json.dumps(sales_dict)
    
    return sales_json

# Function to get dictionary containing 
# region wise sales data of each laptop model's sold percentage
def getRegionWiseSalesData_dict(csv_file) :
    sales_dict = dict() 
    
    # Read the csv file containing the dataset
    dataset = pd.read_csv(csv_file)
    
    for region in regions :
        # Create a list to store the sold percentages of the each laptop model
        laptop_sales_list = list()
        
        # Extract all laptop models sold in the selected region
        laptop_region_data = extract_all_model_for_location(dataset, region)
        
        # Compute the total units sold of laptops
        total_units_sold = laptop_region_data.shape[0]
        
        for laptop_model in laptop_models :
            # Extract the laptop model for the selected region
            laptop_model_data = extract_given_model_for_location(dataset, region, laptop_model)
            
            # Compute the number of units sold of the laptop model for the selected region
            units_sold = laptop_model_data.shape[0]
            
            # Compute the unit sold in percentage
            percent_sold = (units_sold / total_units_sold) * 100
            
            # Putting the obtained percentage into the list
            laptop_sales_list.append(percent_sold)
            
        # Putting the list of laptop sales percentage into the dictionary
        sales_dict[region] = laptop_sales_list
    
    return sales_dict

# Function to return json string containing
# region wise sales data of each laptop model's sold percentage
def getRegionWiseSalesData_json(csv_file) :
    # Get the dictionary containing region wise sales data of each laptop model's sold percentage
    sales_dict = getRegionWiseSalesData_dict(csv_file)
    
    # Converting the dictionary to JSON
    json_data = json.dumps(sales_dict)
    
    return json_data

# Function to extract information of all laptop models in the given location
def extract_all_model_for_location(dataset, location) :
    # Extract all models sold in the given location
    dataset_filter_location = dataset.loc[dataset['Location'] ==  location]
    
    return dataset_filter_location

# Function to extract information of given laptop model sold at Global level
def extract_given_model_globally(dataset, model_name) :
    # Extract given laptop model information at global level
    dataset_filter_model = dataset.loc[dataset['Model'] == model_name]
    
    return dataset_filter_model

# Function to extract information of given laptop model sold in given location
def extract_given_model_for_location(dataset, location, model_name) :
    # Extract all models sold in the given location
    dataset_filter_location = dataset.loc[dataset['Location'] ==  location]
    
    # Extract data of given model sold in the given location
    required_data = dataset_filter_location.loc[dataset_filter_location['Model'] == model_name]
    
    return required_data

def main(csv_file) :  
    # Get the region wise sales data
    
    region_wise_sales_dict = getRegionWiseSalesData_dict(csv_file)
    # Pickle the region wise sales dictionary
    region_wise_file_name_dict = "RegionWise_dict.pickle"    
    with open(region_wise_file_name_dict, "wb") as pickle_file :
        pickle.dump(region_wise_sales_dict, pickle_file)
        
    region_wise_sales_json = getRegionWiseSalesData_json(csv_file)
    # Pickle the region wise sales JSON
    region_wise_file_name_json = "RegionWise_json.pickle"
    with open(region_wise_file_name_json, "wb") as pickle_file :
        pickle.dump(region_wise_sales_json, pickle_file)
    
    # Get the global level sales data
    
    global_level_sales_dict = getGlobalLevelSalesData_dict(csv_file)
    # Pickle the global level sales dictionary
    global_level_file_name_dict = "GlobalLevel_dict.pickle"
    with open(global_level_file_name_dict, "wb") as pickle_file :
        pickle.dump(global_level_sales_dict, pickle_file)
        
    global_level_sales_json = getGlobalLevelSalesData_json(csv_file)
    # Pickle the global level sales JSON
    global_level_file_name_json = "GlobalLevel_json.pickle"
    with open(global_level_file_name_json, "wb") as pickle_file :
        pickle.dump(global_level_sales_json, pickle_file)
    
if __name__ == "__main__" :
    csv_file = "AssetsDellData.csv"
    main(csv_file)