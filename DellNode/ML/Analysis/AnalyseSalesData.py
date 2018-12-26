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
regions = ("CA", "CAJ", "SEA", "USC", "WSE")

# Tuple which stores the laptop models
laptop_models = ("AlienWare", "Inspiron", "XPS")

# Tuples which stores the laptop
laptop_generations = (1, 2, 3)

# Tuples which stores the various occupations of the customer
customer_occupations = ("Businessman", "Developer", "Farmer", "Gamer", "Manager", "Student")

# -------------------------- GETTERS FOR SALES DATA ------------------------  #

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

#Function to return dictionary containing
#region wise sales data of each laptop model's generation sold percentage
def getRegion_laptopGenWise_SalesData_dict(csv_file) :
    sales_dict = dict()
    
    # Read the csv file containing the dataset
    dataset = pd.read_csv(csv_file)
    
    for region in regions :
        sales_dict[region] = dict()
        
        for model in laptop_models :
            # Create a list to store the sold percentages of the each laptop model
            sales_dict[region][model] = list()
            
            # Extract selected model for current region
            model_region_data = extract_given_model_for_location(dataset, region, model)
            
            # Compute the nbr of units sold of the selected model in the current region
            model_total_units_sold = model_region_data.shape[0]
            
            for generation in laptop_generations :
                # Extract the model generation data
                model_gen_data = extract_given_model_gen_for_location(dataset, region, model, generation)
                
                # Compute the nbr of units sold of current generation
                gen_units_sold = model_gen_data.shape[0]
                
                # Compute the percentage sold
                percent_sold = (gen_units_sold / model_total_units_sold) * 100
                
                # Put the computed percentage into the sales dictionary for current model
                sales_dict[region][model].append(percent_sold)
    
    return sales_dict

#Function to return JSON containing
#region wise sales data of each laptop model's generation sold percentage
def getRegion_laptopGenWise_SalesData_json(csv_file) :
    # Get the dictionary containing region wise sales data of each laptop model's generation sold percentage
    sales_dict = getRegion_laptopGenWise_SalesData_dict(csv_file)
    
    # Converting dictionary to JSON
    sales_json = json.dumps(sales_dict)
    
    return sales_json

# Function to return dictionary containing
# sales data of each laptop model's generation sold percentage at Global Level
def getGlobal_laptopGenWise_SalesData_dict(csv_file) :
    sales_dict = dict()
    
    # Read the csv file containing the dataset
    dataset = pd.read_csv(csv_file)
    
    for model in laptop_models :
        # Create a list to store percentage sold of each generation of the selected model
        sales_dict[model] = list()
        
        # Extract the selected model sold globally
        global_model_info = extract_given_model_globally(dataset, model)
        
        # Compute the number of units sold of the current generation
        total_units_sold = global_model_info.shape[0]
        
        for generation in laptop_generations :
            # Extract the information of selected model generation at global level
            model_gen_info = extract_given_model_gen_globally(dataset, model, generation)
            
            # Compute the number of units sold of current generation at global level
            units_sold = model_gen_info.shape[0]
            
            # Compute the percentage sold
            percent_sold = (units_sold / total_units_sold) * 100
            
            # Put the percentage obtained in the list
            sales_dict[model].append(percent_sold)
    
    return sales_dict

# Function to return JSON containing
# sales data of each laptop model's generation sold percentage at Global level
def getGlobal_laptopGenWise_SalesData_json(csv_file) :
    sales_dict = getGlobal_laptopGenWise_SalesData_dict(csv_file)
    
    sales_json = json.dumps(sales_dict)
    
    return sales_json

# Function to return dictionary containing
# sales data of each laptop model distributed among various occupations
def getRegion_customerCategoryWise_SalesData_dict(csv_file) :
    sales_dict = dict()
    
    # Read the csv file containing the dataset
    dataset = pd.read_csv(csv_file)
    
    for region in regions :
        sales_dict[region] = dict()
        
        for model in laptop_models :
            # Create a list to store the sold percentages of the each laptop model
            sales_dict[region][model] = list()
            
            # Extract selected model for current region
            model_region_data = extract_given_model_for_location(dataset, region, model)
            
            # Compute the nbr of units sold of the selected model in the current region
            model_total_units_sold = model_region_data.shape[0]
            
            for customerType in customer_occupations :
                # Extract the model sales data based on customer occupation
                model_customer_dist = extract_given_model_for_customer_location(dataset, region, model, customerType)
                
                # Computer number of model sold among the current customer occupation
                units_sold = model_customer_dist.shape[0]
                
                # Computer the percentage sold
                percent_sold = (units_sold / model_total_units_sold) * 100
                
                # Put the percentage obtained into the sales list
                sales_dict[region][model].append(percent_sold)
    
    return sales_dict

# Function to return JSON containing
# sales data of each laptop model distributed among various occupations
def getRegion_customerCategoryWise_SalesData_json(csv_file) :
    # Get the dictionary
    sales_dict = getRegion_customerCategoryWise_SalesData_dict(csv_file)
    
    # Converting to JSON
    sales_json = json.dumps(sales_dict)
    
    return sales_json

# Function to return dictionary containing
# sales data for each laptop model distributed among various occupations at Global Level
def getGlobal_customerCategoryWise_SalesData_dict(csv_file) :
    sales_dict = dict()
    
    # Read the csv file containing the dataset
    dataset = pd.read_csv(csv_file)
    
    for model in laptop_models :
        # Create a list to store percentage sold of each generation of the selected model
        sales_dict[model] = list()
        
        # Extract the selected model sold globally
        global_model_info = extract_given_model_globally(dataset, model)
        
        # Compute the number of units sold of the current generation
        total_units_sold = global_model_info.shape[0]
        
        for customerType in customer_occupations :
            # Extract the info of laptop model adopted by current customer type
            model_customerType_info = extract_given_model_for_customer_global(dataset, model, customerType)
            
            # Compute the number of units sold of current generation at global level
            units_sold = model_customerType_info.shape[0]
            
            # Compute the percentage sold
            percent_sold = (units_sold / total_units_sold) * 100
            
            # Put the percentage obtained in the list
            sales_dict[model].append(percent_sold)
    
    return sales_dict

# Function to return JSON containing
# sales data for each laptop model distributed among various occupations at Global Level
def getGlobal_customerCategoryWise_SalesData_json(csv_file) :
    # Get the dictionary
    sales_dict = getGlobal_customerCategoryWise_SalesData_dict(csv_file)
    
    # Converting dictionary to JSON
    sales_json = json.dumps(sales_dict)
    
    return sales_json
            
# ------------------------ EXTRACTORS --------------------------------------  #        

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

# Function to extract information of given laptop model of given generation sold in given location
def extract_given_model_gen_for_location(dataset, region, model_name, generation) :
    # Extract selected model for given location
    model_region_data = extract_given_model_for_location(dataset, region, model_name)
    
    # Extract data of given model generation
    required_data = model_region_data.loc[model_region_data['Generation'] == generation]
    
    return required_data

# Function to extract information of given laptop model of given generation sold globally
def extract_given_model_gen_globally(dataset, model_name, generation) :
    # Extract given model information at global level
    model_info_global = extract_given_model_globally(dataset, model_name)
    
    required_data = model_info_global.loc[model_info_global['Generation'] == generation]
    
    return required_data

# Function to extract information of given laptop mode for given customer occupation
def extract_given_model_for_customer_location(dataset, region, model_name, customer_occupation) :
    # Extract selected model for given location
    model_region_data = extract_given_model_for_location(dataset, region, model_name)
    
    # Extract data for model purchased by given customer occupation
    required_data = model_region_data.loc[model_region_data['Occupation'] == customer_occupation]
    
    return required_data

# Function to extract information of given laptop mode for given customer occupation at Global level
def extract_given_model_for_customer_global(dataset, model_name, customer_occupation) :
    # Extraction given model info at Global level
    model_info = extract_given_model_globally(dataset, model_name)
    
    # Extract those model adopted by given customer occupation
    required_data = model_info.loc[model_info['Occupation'] == customer_occupation]
    
    return required_data

# --------------------------- MAIN SCRIPT DRIVER ---------------------------- #

def main(csv_file) :  
    # Get the region wise sales data
    
    region_wise_sales_dict = getRegionWiseSalesData_dict(csv_file)  # Get the dictionary
    # Pickle the region wise sales dictionary
    region_wise_file_name_dict = "RegionWise_dict.pickle"    
    with open(region_wise_file_name_dict, "wb") as pickle_file :
        pickle.dump(region_wise_sales_dict, pickle_file)
        
    region_wise_sales_json = getRegionWiseSalesData_json(csv_file)  # Get the JSON
    # Pickle the region wise sales JSON
    region_wise_file_name_json = "RegionWise_json.pickle"
    with open(region_wise_file_name_json, "wb") as pickle_file :
        pickle.dump(region_wise_sales_json, pickle_file)
    
    # Get the global level sales data
    
    global_level_sales_dict = getGlobalLevelSalesData_dict(csv_file)    # Get the dictionary
    # Pickle the global level sales dictionary
    global_level_file_name_dict = "GlobalLevel_dict.pickle"
    with open(global_level_file_name_dict, "wb") as pickle_file :
        pickle.dump(global_level_sales_dict, pickle_file)
        
    global_level_sales_json = getGlobalLevelSalesData_json(csv_file)    # Get the dictionary
    # Pickle the global level sales JSON
    global_level_file_name_json = "GlobalLevel_json.pickle"
    with open(global_level_file_name_json, "wb") as pickle_file :
        pickle.dump(global_level_sales_json, pickle_file)
        
    # Get the laptop generation wise sales data for each Region
    
    generation_wise_sales_dict = getRegion_laptopGenWise_SalesData_dict(csv_file)   # Get the dictionary
    # Pickle the dictionary of laptop generation wise sales for each region
    generation_wise_file_name_dict = "RegionGenerationWise_dict.pickle"
    with open(generation_wise_file_name_dict, "wb") as pickle_file :
        pickle.dump(generation_wise_sales_dict, pickle_file)
        
    generation_wise_sales_json = getRegion_laptopGenWise_SalesData_json(csv_file)   # Get the JSON
    # Pickle the JSON of laptop generation wise sales for each region
    generation_wise_file_name_json = "RegionGenerationWise_json.pickle"
    with open(generation_wise_file_name_json, "wb") as pickle_file:
        pickle.dump(generation_wise_sales_json, pickle_file)

    # Get the laptop generation wise sales data       
    
    global_generation_wise_sales_dict = getGlobal_laptopGenWise_SalesData_dict(csv_file)    # Get the dictionary
    # Pickle the dictionary of laptop generation wise sales at Global level
    global_generation_wise_file_name_dict = "GlobalGenerationWise_dict.pickle"
    with open(global_generation_wise_file_name_dict, "wb") as pickle_file :
        pickle.dump(global_generation_wise_sales_dict, pickle_file)
        
    global_generation_wise_sales_json = getGlobal_laptopGenWise_SalesData_json(csv_file)    # Get the JSON
    # Pickle the JSON of laptop generation wise sales at Global level
    global_generation_wise_file_name_json = "GlobalGenerationWise_json.pickle"
    with open(global_generation_wise_file_name_json, "wb") as pickle_file :
        pickle.dump(global_generation_wise_sales_json, pickle_file)
        
    # Get the laptop sales data based on customer occupation region wise
    
    laptop_occupation_region_sales_dict = getRegion_customerCategoryWise_SalesData_dict(csv_file)
    # Pickle the dictionary of laptop sales data based on customer occupation region wise
    region_occuption_wise_file_name_dict = "RegionOccupationWise_dict.pickle"
    with open(region_occuption_wise_file_name_dict, "wb") as pickle_file :
        pickle.dump(laptop_occupation_region_sales_dict, pickle_file)
    
    laptop_occupation_region_sales_json = getRegion_customerCategoryWise_SalesData_json(csv_file)
    # Pickle the JSON of laptop sales data based on customer occupation region wise
    region_occuption_wise_file_name_json = "RegionOccupationWise_json.pickle"
    with open(region_occuption_wise_file_name_json, "wb") as pickle_file :
        pickle.dump(laptop_occupation_region_sales_json, pickle_file)
        
    # Get the laptop sales data based on customer occupation at Global Level
    
    laptop_occupation_global_sales_dict = getGlobal_customerCategoryWise_SalesData_dict(csv_file)
    # Pickle the dictionary of laptop sales data based on customer occupation globally
    global_occupation_wise_file_name_dict = "GlobalOccupationWise_dict.pickle"
    with open(global_occupation_wise_file_name_dict, "wb") as pickle_file:
        pickle.dump(laptop_occupation_global_sales_dict, pickle_file)
    
    laptop_occupation_global_sales_json = getGlobal_customerCategoryWise_SalesData_json(csv_file)
    # Pickle the JSON of laptop sales data based on customer occupation globally
    global_occupation_wise_file_name_json = "GlobalOccupationWise_json.pickle"
    with open(global_occupation_wise_file_name_json, "wb") as pickle_file :
        pickle.dump(laptop_occupation_global_sales_json, pickle_file)
    
if __name__ == "__main__" :
    csv_file = "AssetsDellData.csv"
    main(csv_file)