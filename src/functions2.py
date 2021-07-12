import pandas as pd
from . import formatter, message
import numpy as np

def pandasMode(data:list, totalHeight:int, fromDict=True):
    """I do a consult of pandas dataframe and then iterate

    Args:
        data (list): List of data that will be combined
        
        totalHeight (int): Data provided by the user for the search
        
        fromDict (bool, optional): Tells us if the data that is entered is 
        with the data from the specified path or is a list of integers . 
        Defaults to True.
    """
    df = pd.DataFrame(data)
    acumulator = list()
    if fromDict:
        df['h_in'] = df['h_in'].astype(np.int64)
        cartesianProduct = df.merge(df, how='cross', suffixes=('_x', '_y'))
        cartesianProduct = cartesianProduct[cartesianProduct['h_in_x'] != cartesianProduct['h_in_y']]
        
        cartesianProduct['sum'] = cartesianProduct['h_in_x']+cartesianProduct['h_in_y']
        counter = 0
        for _, row in cartesianProduct[cartesianProduct['sum']==totalHeight].iterrows():
            uluju1 = row['first_name_x']+row['last_name_x']
            uluju2 = row['first_name_y']+row['last_name_y']
            if set([uluju1, uluju2]) not in acumulator:
                print(formatter(row['first_name_x'], row['last_name_x'], row['first_name_y'], row['last_name_y']))
                acumulator.append(set([uluju1, uluju2]))
            counter+=1
    else:
        cartesianProduct = df.merge(df, how='cross', suffixes=('_x', '_y'))
        cartesianProduct['sum'] = cartesianProduct['0_x']+cartesianProduct['0_y']
        counter = 0
        for _, row in cartesianProduct[cartesianProduct['sum']==totalHeight].iterrows():
            uluju = set([row["0_x"],row["0_y"]])
            if uluju not in acumulator:
                print(f'{row["0_x"]}-{row["0_y"]}')
                acumulator.append(uluju)
            counter+=1
    if counter < 1:
        print(message)