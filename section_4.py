import numpy as np
import matplotlib.pyplot as plt

def miss_val_summary(df, axis_val = 'column', x_bin = 2, bar_chart = True):
    '''
    function to display summary, bar-chart (optional) and histogram
    of missing values by column or raw
    df: dataframe
    axis_val: str, selection of 'column' or 'row', 'column' as default
    x_bin: size of x bin, 2 as default
    bar_chart: option of bar chart display 
    '''
    # index of axis
    axis_idx = 0 if axis_val == 'column' else 1
    
    # % of missing values
    missing_pct = df.isnull().mean(axis = axis_idx) * 100
    df_desc = missing_pct.describe()

    # summary of missing value
    print (
        '% of missing value in ' + str(int(df_desc[0])) + ' ' + axis_val + 's of ' + df.name)
    print (df_desc[1:].to_string())
    
    # bar-chart of missing value
    if bar_chart:
        missing_pct.plot(
            kind = 'bar', figsize=(10, 3), color='gray',
            
            title = ('bar chart - ' + df.name + ': missing value by ' + axis_val),
            ylabel = '% of missing value',
            xlabel = (str(int(df_desc[0])) + ' columns'),
            xticks = [],
            );
        plt.show()
    
    # hist of missing value
    x_range = ((df_desc[-1] + 10) // 10) * 10 + x_bin
    # x_range = (df_desc[-1] // 10) * 10 + x_bin
    ax = missing_pct.plot(
        kind = 'hist', figsize=(10, 3), color='gray',
        
        bins = np.arange(0, x_range, x_bin),
        title = ('histogram - ' + df.name + ': missing value by ' + axis_val),
        xticks = np.arange(0, x_range, 10)
        )
    ax.set_xlabel('% of missing value');
    plt.show()