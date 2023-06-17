import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from googletrans import Translator
import Levenshtein
from vlookup import vlookup
from view_all import view_all

def similar_feature (dict_key_1, dict_key_2, feature_dict):
    '''
    function to extract the most similar complement features
    of dict_key_1 of feature_dict from dict_key_2
    '''
    most_similar = {}
    for i in feature_dict[dict_key_1]:
        min_distance = float('inf')
        most_similar_element = None
        for j in feature_dict[dict_key_2]:
            distance = Levenshtein.distance(i, j)
            # if distance < min_distance:
            if (distance < min_distance) & (distance != 0):
                min_distance = distance
                most_similar_element = j
        most_similar[i] = [most_similar_element, min_distance]

    most_similar_df = pd.DataFrame(most_similar).T.reset_index()
    most_similar_df.columns = ['Attribute', dict_key_2, 'distance'] 

    most_similar_df['suffix_added'] = most_similar_df.apply(
        lambda x: 1 if x[dict_key_2] in x['Attribute'] else 0, axis=1)
    most_similar_df = most_similar_df.query('distance <= 3')
    
    return most_similar_df

def attribute_cat (data):
    '''
    function to add category values of Attribute 
    '''
    data['category_large'] = data['Attribute'].apply(
        lambda x: x.split('_')[0] if '_' in x else 'no_category')
    data['category_small'] = np.where(data['category_large'] == 'no_category',
                                            data['Attribute'],
                                            data['category_large'])
    return data

def str_to_num (number):
    '''
    function to change dtype of numbers in string form
    '''
    if isinstance(number, str) and (
        number.isdigit() or (number.startswith('-') and number[1:].isdigit())):
        return int(number)
    else:
        return number

def ger_to_eng (ger_text):
    '''
    function to translate German text
    '''
    translator = Translator(service_urls=['translate.google.com'])    
    try:
        translation = translator.translate(ger_text, src='de', dest='en')
        return translation.text        
    except:
        return np.nan

def pv_min_max(
    data, feature_desc, pv_idx = ['category_large', 'Attribute', 'Description', 'Desc', 'Additional notes'],
    display = True):
    '''
    function to display min/max values of Score after adding information from feature_desc
    
    data : dataframe to examine
    pv_idx: list of pivot_table index
    display: boolean, selection of result display
    '''
    data = vlookup(data, feature_desc, 'Attribute', ['Desc', 'Additional notes'], fill_na = 'no_info')
    pv = pd.pivot_table(
        data,
        index = pv_idx,
        values = 'Score',
        aggfunc = [min, max]
        )
        
    pv['min_max_cat'] = pv['min'].astype(int).astype(str) + ' to ' + pv['max'].astype(int).astype(str)
    pv = pv.sort_values(by = 'min_max_cat')
    
    pv = pd.DataFrame(pv.to_records())
    pv.columns = list(pv.columns[:-3]) + list(eval(i)[0] for i in pv.columns[-3:])
    print (f'number of Attribute(s): {data.Attribute.nunique()}')

    if display:
        print (pv.min_max_cat.unique())
    
    return pv

def pv_meaning_score(
    data, feature_desc,
    pv_idx = ['category_large', 'Attribute', 'Description', 'Desc', 'Additional notes'],
    pv_val = ['Meaning', 'Score'],
    display = True,
    ):
    '''
    function to display the summary of Meaning and Score values
    after adding information from feature_desc
    
    data : dataframe to examine
    pv_idx: list of pivot_table index
    pv_val: list of pivot_table value
    display: boolean, selection of result display
    '''
    data = vlookup(data, feature_desc, 'Attribute', ['Desc', 'Additional notes'], fill_na = 'no_info')
    pv = pd.pivot_table(
        data,
        index = pv_idx,
        values = pv_val,
        aggfunc = lambda x: list(x))
    
    pv = pd.DataFrame(pv.to_records())
    print (f'number of Attribute(s): {data.Attribute.nunique()}')
    
    if display:
        view_all(pv.iloc[:5])
    
    return pv

def pv_verify_null(
    data,
    feature_desc,
    null_list,
    pv_idx = ['category_large', 'Attribute', 'Description', 'Desc', 'Additional notes'], 
    pv_val = ['Meaning', 'Score'],    
    display = True
    ):
    '''
    function to display the summary of Meaning and Score values
    when Meaning values are in the list containing possibly null values 
    
    data: dataframe to examine
    null_list: list of possibly null values
    pv_idx: pivot_table index
    pv_val: list of pivot_table value
    display: boolean, selection of result display
    '''
    null_check_Attribute = data.query('Meaning in @null_list').Attribute.to_list()
    null_check = data.query('Attribute in @null_check_Attribute')
    
    pv = pv_meaning_score(null_check, feature_desc, pv_idx, pv_val, display)
    
    return pv