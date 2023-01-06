from sklearn.preprocessing import MinMaxScaler
import pickle
import pandas as pd
import numpy as np

with open('trained_model-001.pkl', 'rb') as file:
    model=pickle.load(file)


def predict_cost(response,model)->float:
    
    df=pd.DataFrame(answer,index=[0])
    return 

answer={"store_type":"Gourmet Supermarket","store_state":"Zacatecas","grocery_sqft":"15012","frozen_sqft":"4193","coffee_bar":"1","video_store":"0","prepared_food":"1","florist":"0","media_type":"Daily Paper","marital_status":"M","gender":"F","total_children":"5","education":"Partial College","member_card":"Bronze","occupation":"Professional","houseowner":"N","avg_cars_at home(approx)":"4","avg. yearly_income":"$90K - $110K","num_children_at_home":"4","SRP":"2.8","net_weight":"17.8","recyclable_package":"1","low_fat":"0","units_per_case":"32","food_family":"Food","unit_sales(in millions)":"1","promotion_name":"Price Smashers","sales_country":"USA"}
