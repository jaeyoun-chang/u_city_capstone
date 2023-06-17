import numpy as np
import matplotlib.pyplot as plt
from vlookup import vlookup
from view_all import view_all

def dataset_summary (data, feature_desc, score_form, display = True):
    '''
    function to create the summary table of given dataframe,
    by applying describe and transpose methods
    
    data: dataframe
    score_form : str / list, dtypes of columns to be selected
    display: boolean, selection of result display
    '''
    # filter data    
    data_copy = data.select_dtypes(include = score_form)
    
    # extract summary of data by applying describe and transpose
    data_summary = data_copy.describe().T.reset_index()

    # merge Desc (information on Attribute) from feature_desc and add min_max_cat
    data_summary = data_summary.rename(columns = {'index' : 'Attribute'})
    data_summary = vlookup(data_summary, feature_desc, 'Attribute', 'Desc')
    # data_summary['null_portion'] = (1 - data_summary['count'] / data.shape[0]).map('{:.1%}'.format)    
    data_summary['null_portion'] = 1 - data_summary['count'] / data.shape[0]
    
    # add min_max_cat incase score_form in numeric
    if any(x in ['int', 'float'] for x in score_form):
        min_max_display = True
        data_summary['min_max_cat'] = data_summary[
            'min'].apply(lambda x: '{:_.0f}'.format(x)).astype(str) + ' to ' + data_summary[
            'max'].apply(lambda x: '{:_.0f}'.format(x)).astype(str)
    else:
        min_max_display = False
    
    if display:
        print (f'number of Attribute(s): {data_summary.Attribute.nunique()}')
        view_all(data_summary.iloc[:5])
        
        if min_max_display:
            print ('min_max Scores:', '\n', data_summary.min_max_cat.unique())
    
    return data_summary

def view_feature (data, feature_desc, feature, view_all = True, view_0_10 = True):
    '''
    function to view and check continuous numeric data
    feature : str, feature name
    view_0_10 : boolean for histogram display of value 0 to 10, default as True
    '''
    # create data_stat using 
    data_stat = dataset_summary(data, feature_desc, ['int', 'float'], display = False)

    min_val = data[feature].min()
    max_val = data[feature].max()
    bin_edges = np.arange(min_val, max_val + 10, 10)
    desc_val = data_stat[data_stat['Attribute'] == feature]['Desc'].values[0]

    if view_all:
        ax = data[feature].plot(
            kind = 'hist',
            figsize=(10, 1.5),
            color='gray',
            bins = bin_edges,
            align = 'mid',
            title = (f'histogram - {desc_val} - {feature}')
            );
        ax.set_xlabel('Scores - Min: ' + str(int(min_val)) + ', Max: ' + str(int(max_val)));
        plt.show()

    if view_0_10:
        ax = data[feature].plot(
            kind = 'hist',
            figsize=(10, 1.5),
            color='gray',
            bins = np.arange(-0.5, 11.5, 1),
            align = 'mid',
            title = (f'histogram - {desc_val} - {feature} - Score 0 to 10'),
            );
        ax.set_xlabel('Scores - Min: ' + str(int(min_val)) + ', Max: ' + str(int(max_val)));
        plt.show()
    
    # define the outlier thresholds by applying multiplier 1.5
    q1 = data_stat[data_stat['Attribute'] == feature]['25%'].values[0]
    q3 = data_stat[data_stat['Attribute'] == feature]['75%'].values[0]
    iqr = q3 - q1
    lower_threshold = q1 - 1.5 * iqr
    upper_threshold = q3 + 1.5 * iqr

    # identify outliers
    col_val = data[feature].values
    outliers = sorted(
        set([feature for feature in col_val if feature < lower_threshold or feature > upper_threshold]),
        reverse = True)

    # print outliers
    count_val = data_stat[data_stat['Attribute'] == feature].fillna(0)['count'].values[0]       
    outlier_list = [
        str(int(j)) + ': ' + '{:.1%}'.format((data[feature] == j).sum() / count_val)
        for j in outliers
        ]
    
    print('10 outliers (Score: %)', '\n',
          ', '.join(outlier_list[:5]), '…', ', '.join(outlier_list[-5:]))

    # for j in range(0, len(outlier_list), 10):
    #     print (', '.join(outlier_list[j : j+10]))
    
    print ('\n')